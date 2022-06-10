import Librarys.BasicFunctions as bf, Librarys.BlackjackProcess as bp, os, sys, datetime, time
bf.cls()

#Info screen:
print(f"{bf.ansi.blue}Blackjack{bf.ansi.white}(Version 0.5.5[5/2/2022])\n"
f"Created by: {bf.ansi.green}Nomster Dude{bf.ansi.white}\n"
"Supports: Windows, MacOS, Linux\n"
"Requires: Python 3.0+\n")
bf.pause()
bf.cls()

def initialinit():
    global data
    global errorlog
    global timedate
    global bet
    data = {"Name": "unknown", "Data Version": "0.1.1", "chips": 1000, "playercard": {}, "playervalue": 0, "dealercard": {}, "dealervalue": 0, "avai": bp.deck()}
    timedate = f'{datetime.date.today()} {time.strftime("%H-%M-%S", time.localtime())}'
    errorlog = {"Number of Errors": 0}
    init()
def init():
    data["playercard"], data["dealercard"], data["playervalue"], data["dealervalue"] = {},{},0,0
initialinit()

def errorlogging(error):#Logs errors to the variable "errorlog"
    if type(error).__name__ == "KeyboardInterrupt":#Allow for the user to exit via "KeyboardInterrupt"(ctrl+c)
        sys.exit("Exit command used via Keyboard(ctrl+c)")
    else:
        errortrace = error.__traceback__
        errorlog["Number of Errors"] = errorlog["Number of Errors"]+1
        errorlog[f"Error {str(errorlog['Number of Errors'])}"] = f"{type(error).__name__}(Line {errortrace.tb_lineno}): {error}"
        bf.save(f'{data["Name"]} {timedate}', errorlog, file_path=os.path.join(sys.path[0], "Save Data", "Error Logs"), indentation=3)

def login(attempt="0"):
    bf.cls()
    if attempt == "0":
        option = bf.getch(f"[{bf.ansi.blue}L{bf.ansi.white}] - Load Save\n"
        f"[{bf.ansi.blue}S{bf.ansi.white}] - Start New Save\n"
        "\n"
        "Option: ")

        if option.lower() == "l":
            loadgame()
        elif option.lower() == "s":
            savegamenew()
        else:
            login()
    if attempt == "LoadFail":
        option = bf.getch("Name does not exist!\n"
        f"[{bf.ansi.blue}L{bf.ansi.white}] - Load Save\n"
        f"[{bf.ansi.blue}S{bf.ansi.white}] - Start New Save\n"
        "\n"
        "Option: ")

        if option.lower() == "l":
            loadgame()
        elif option.lower() == "s":
            savegamenew()
        else:
            login("LoadFail")
    if attempt == "SaveFail":
        option = bf.getch("Name already exists!\n"
        f"[{bf.ansi.blue}L{bf.ansi.white}] - Load Save\n"
        f"[{bf.ansi.blue}S{bf.ansi.white}] - Start New Save\n"
        "\n"
        "Option: ")

        if option.lower() == "l":
            loadgame()
        elif option.lower() == "s":
            savegamenew()
        else:
            login("SaveFail")
def loadgame():
    global data
    bf.cls()
    Name = input("What was the name used in your save(Including caps): ")
    if os.path.exists(f'{os.path.join(sys.path[0], "Save Data", Name)}.json'):
        bf.cls()
        data = saveconvert(bf.load(Name))
        bf.save(Name, data, indentation=3)
        print("Your data has been loaded from:\n"
        f'{bf.ansi.italics}{bf.ansi.blue}./Save Data/{data["Name"]}.json{bf.ansi.standard}{bf.ansi.white}\n')
        bf.pause()
    else:
        login("LoadFail")
def savegamenew():
    bf.cls()
    Name = input("What would you like your name to be(Remember this): ")
    data["Name"] = Name
    if os.path.exists(f'{os.path.join(sys.path[0], "Save Data", Name)}.json'):
        login("SaveFail")
    else:
        bf.cls()
        bf.save(Name, data, indentation=3)
        print("Your data has been saved to:\n"
        f'{bf.ansi.italics}{bf.ansi.blue}./Save Data/{data["Name"]}.json{bf.ansi.standard}{bf.ansi.white}\n')
        bf.pause()
def saveconvert(olddata):#Converts data to new format to avoid breaking the game after an update
    try:
        convertedsave = {"Name": olddata["Name"], "Data Version": "0.1.1", "chips": olddata["chips"], "playercard": {}, "playervalue": 0, "dealercard": {}, "dealervalue": 0, "avai": bp.deck()}
        return convertedsave
    except KeyError as error:
        errorlogging(error)
        convertedsave = {"Name": olddata["Name"], "Data Version": "0.1.1", "chips": 1000, "playercard": {}, "playervalue": 0, "dealercard": {}, "dealervalue": 0, "avai": bp.deck()}
        return convertedsave
try:
    login()
except BaseException as error:
    bf.cls()
    errorlogging(error)
    print(f'{bf.ansi.red}An error has forced the program to shut down{bf.ansi.white}:\n'
    f'{bf.ansi.blue}./Save Data/Error Logs/{data["Name"]} {timedate}{bf.ansi.white}')
    raise SystemExit

def save():
    bf.cls()
    bf.save(data["Name"],data)
    print("Your data has been saved to:\n"
    f'{bf.ansi.italics}{bf.ansi.blue}./Save Data/{data["Name"]}.json{bf.ansi.standard}{bf.ansi.white}\n')
    bf.pause()

def beta():
    random = bf.randomselect(data["avai"])
    print(f'{data["avai"][random]["value"]}{data["avai"][random]["suit"]}\n'
    f'{random} = {data["avai"][random]}\n')
    bf.pause()

def debug():
    bf.cls()
    print(f"Welcome to {bf.ansi.green}Debug Mode{bf.ansi.white}!\n"
    "\n"
    f"{bf.ansi.green}Player data:{bf.ansi.white}")
    for a,b in data.items():
        if a != "avai":
            print(f"{a}: {b}")
    print(f'\nPlayer data location: {bf.ansi.italics}{bf.ansi.blue}./Save Data/{data["Name"]}.json{bf.ansi.standard}{bf.ansi.white}\n'
    "\n"
    f"{bf.ansi.green}Error data:{bf.ansi.white}\n"
    f'Number of errors: {bf.ansi.red}{errorlog["Number of Errors"]}{bf.ansi.white}')
    if errorlog["Number of Errors"] != 0:
        print(f"Error-Log location: {bf.ansi.italics}{bf.ansi.blue}./Save Data/Error Logs/{data['Name']} {timedate}.json{bf.ansi.standard}{bf.ansi.white}")
    print()
    print(f'{bf.ansi.green}Avaiable cards {bf.ansi.italics}(Saved to "player data"!){bf.ansi.standard}{bf.ansi.green}:{bf.ansi.white}')
    for i in data["avai"]:
        print(f'{data["avai"][i]["value"]}{data["avai"][i]["suit"]} {data["avai"][i]}')
    print()
    bf.pause()
    bf.cls()

def select(player):
    try:
        selection = bf.randomselect(data["avai"])
        if player == "player":
            data["playercard"][len(data["playercard"].keys())] = data["avai"][selection]
            data["playervalue"] = bp.checkvalues(data,"player")
        elif player == "dealer":
            data["dealercard"][len(data["dealercard"].keys())] = data["avai"][selection]
            data["dealervalue"] = bp.checkvalues(data,"dealer")
        del data["avai"][selection]
    except BaseException as error:
        errorlogging(error)
        select(player=player)

def pause():
    bf.cls()
    print(f'{bf.ansi.green}Game paused{bf.ansi.white}: Logged in as {data["Name"]}\n'
    f'{bf.ansi.blue}Chips{bf.ansi.white}: {bf.ansi.green}${data["chips"]}{bf.ansi.white}\n'
    f'[{bf.ansi.blue}M{bf.ansi.white}]Main Menu\n'
    "\n"
    f'[{bf.ansi.blue}R{bf.ansi.white}]Resume Game\n'
    f'[{bf.ansi.blue}S{bf.ansi.white}]Save Game\n'
    f'[{bf.ansi.blue}C{bf.ansi.white}]Chip Menu\n')

    option = bf.getch("Option: ")
    if option.lower() == "m":
        mainmenu()
    elif option.lower() == "r":
        pass
    elif option.lower() == "s":
        save()
    elif option.lower() == "c":
        data["chips"] = bp.chips("r",data)
    elif option.lower() == "d":
        debug()
    else:
        pause()

def table(mode="",option=""):
    try:
        global bet
        bf.cls()
        if data["chips"] < 0 or data["chips"] == 0:
            data["chips"] = 1000
            print(f'Chip count reset to {bf.ansi.green}$1000{bf.ansi.white} due to being 0 or lower than 0!\n')
            bf.pause()
            bf.cls()
        print(f'{bf.ansi.green}Game table{bf.ansi.white}: Logged in as {data["Name"]}\n'
        f'{bf.ansi.blue}Chips{bf.ansi.white}: {bf.ansi.green}${data["chips"]}{bf.ansi.white}\n'
        f'[{bf.ansi.blue}P{bf.ansi.white}]Pause/Options\n')

        if mode == "":
            print(f'[{bf.ansi.blue}S{bf.ansi.white}]Start New Hand\n')
        elif mode == "activestart":
            init()
            data["avai"] = bp.deck()
            for i in range(2):
                select("player")
            select("dealer")
            mode = "active"
        elif mode == "active":
            print(f'Bet: {bf.ansi.green}${bet}{bf.ansi.white}\n'
            "\n"
            f'{bf.ansi.green}Your cards{bf.ansi.white}:')
            for i in range(len(data["playercard"].keys())):
                print(f'{data["playercard"][i]["value"]}{data["playercard"][i]["suit"]}',end=" ")
            print(f'\nScore: {data["playervalue"]}')
            print(f'{bf.ansi.green}Dealers cards{bf.ansi.white}:')
            print(f'{data["dealercard"][0]["value"]}{data["dealercard"][0]["suit"]}\n'
            f'Score: {data["dealervalue"]+1} - {data["dealervalue"]+11}\n'
            "\n"
            f'[{bf.ansi.blue}H{bf.ansi.white}]Hit\n'
            f'[{bf.ansi.blue}S{bf.ansi.white}]Stand\n')
        elif mode == "showdown":
            if data["dealervalue"] < 17:
                select("dealer")
                table(mode="showdown")
            elif data["dealervalue"] > 21:
                table(mode="won")
            elif data["playervalue"] > data["dealervalue"]:
                table(mode="won")
            elif data["dealervalue"] > data["playervalue"]:
                table(mode="lost")
        elif mode == "lost":
            bf.cls()
            data["chips"] -= bet

            print(f'{bf.ansi.green}You lost!{bf.ansi.white}: Logged in as {data["Name"]}\n'
            f'{bf.ansi.blue}Chips{bf.ansi.white}: {bf.ansi.green}${data["chips"]}{bf.ansi.white}\n')
            print(f'You lost {bf.ansi.green}${bet}{bf.ansi.white}\n'
            "\n"
            f'{bf.ansi.green}Your cards{bf.ansi.white}:')
            for i in range(len(data["playercard"].keys())):
                print(f'{data["playercard"][i]["value"]}{data["playercard"][i]["suit"]}',end=" ")
            print(f'\nScore: {data["playervalue"]}')
            print(f'{bf.ansi.green}Dealers cards{bf.ansi.white}:')
            for i in range(len(data["dealercard"].keys())):
                print(f'{data["dealercard"][i]["value"]}{data["dealercard"][i]["suit"]}',end=" ")
            print(f'\nScore: {data["dealervalue"]}\n')

            bf.pause()
            table()
        elif mode == "won":
            bf.cls()
            data["chips"] += bet*(1/2)

            print(f'{bf.ansi.green}You won!{bf.ansi.white}: Logged in as {data["Name"]}\n'
            f'{bf.ansi.blue}Chips{bf.ansi.white}: {bf.ansi.green}${data["chips"]}{bf.ansi.white}\n')
            print(f'You won {bf.ansi.green}${3*(bet/2)}{bf.ansi.white}\n'
            "\n"
            f'{bf.ansi.green}Your cards{bf.ansi.white}:')
            for i in range(len(data["playercard"].keys())):
                print(f'{data["playercard"][i]["value"]}{data["playercard"][i]["suit"]}',end=" ")
            print(f'\nScore: {data["playervalue"]}')
            print(f'{bf.ansi.green}Dealers cards{bf.ansi.white}:')
            for i in range(len(data["dealercard"].keys())):
                print(f'{data["dealercard"][i]["value"]}{data["dealercard"][i]["suit"]}',end=" ")
            print(f'\nScore: {data["dealervalue"]}\n')

            bf.pause()
            table()
        
        if option == "":
            option = bf.getch("Option: ")

        if option.lower() == "p":
            pause()
        elif option.lower() == "d":
            debug()
        if mode == "":
            if option.lower() == "s":
                bf.cls()
                bet = 0
                print(f'{bf.ansi.blue}Chips{bf.ansi.white}: {bf.ansi.green}${data["chips"]}{bf.ansi.white}\n')
                try:
                    bet = float(input("How many chips would you like to bet(0 to cancel): "))
                except ValueError as error:
                    table(option="s")
                bf.cls()
                if bet == 0:
                    table(mode=mode)
                elif bet < 0 or bet > data["chips"]:
                    table(mode=mode, option="s")
                init()
                data["avai"] = bp.deck()
                for i in range(2):
                    select("player")
                select("dealer")
                option = ""
                mode = "active"
        elif mode == "active":
            if option.lower() == "h":
                select("player")
                if data["playervalue"] > 21:
                    table(mode="lost")
                elif data["playervalue"] == 21:
                    table(mode="won")
            if option.lower() == "s":
                table(mode="showdown")
        elif mode == "showdown":
            pass
        table(mode=mode)
    except BaseException as error:
        errorlogging(error)
        table(mode=mode,option=option)

def mainmenu():
    bf.cls()

    print(f'{bf.ansi.green}Main Menu{bf.ansi.white}: Logged in as {data["Name"]}\n'
    f'[{bf.ansi.blue}S{bf.ansi.white}]Save Game\n'
    "\n"
    f'[{bf.ansi.blue}G{bf.ansi.white}]Join Game Table\n'
    f'[{bf.ansi.blue}R{bf.ansi.white}]Reset Chips: You currently have {bf.ansi.green}${data["chips"]}{bf.ansi.white}\n')
    option = bf.getch("Option: ").lower()
    bf.cls()

    if option.lower() == "g":
        table()
    if option.lower() == "t":
        beta()
    if option.lower() == "s":
        save()
    if option.lower() == "r":
        data["chips"] = bp.chips("r",data)
    '''if option.lower() == "r":
        print(f'{bf.ansi.red}Do you want to reset the card deck!{bf.ansi.white}:\n'
        "\n"
        f'[{bf.ansi.blue}Y{bf.ansi.white}]Yes\n'
        f'[{bf.ansi.blue}N{bf.ansi.white}]No\n')
        if bf.getch("Option: ").lower() == "y":
            data["avai"] = bp.deck()
        else:
            pass'''
    if option.lower() == "d":
        debug()
    mainmenu()
try:
    mainmenu()
except BaseException as error:
    bf.cls()
    errorlogging(error)
    print(f'{bf.ansi.red}An error has forced the program to shut down{bf.ansi.white}:\n'
    f'{bf.ansi.blue}./Save Data/Error Logs/{data["Name"]} {timedate}{bf.ansi.white}')
    raise SystemExit
