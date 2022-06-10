try:
    import Modules.BasicFunctions as bf
except ModuleNotFoundError as error:
    import BasicFunctions as bf

class suit:
    spade = "\u2660"
    heart = "\u2661"
    diamond = "\u2662"
    club = "\u2663"
def deck():
    fulldeck = {
    1:{"value":"A","suit":suit.spade},
    2:{"value":"2","suit":suit.spade},
    3:{"value":"3","suit":suit.spade},
    4:{"value":"4","suit":suit.spade},
    5:{"value":"5","suit":suit.spade},
    6:{"value":"6","suit":suit.spade},
    7:{"value":"7","suit":suit.spade},
    8:{"value":"8","suit":suit.spade},
    9:{"value":"9","suit":suit.spade},
    10:{"value":"10","suit":suit.spade},
    11:{"value":"J","suit":suit.spade},
    12:{"value":"Q","suit":suit.spade},
    13:{"value":"K","suit":suit.spade},
    14:{"value":"A","suit":suit.diamond},
    15:{"value":"2","suit":suit.diamond},
    16:{"value":"3","suit":suit.diamond},
    17:{"value":"4","suit":suit.diamond},
    18:{"value":"5","suit":suit.diamond},
    19:{"value":"6","suit":suit.diamond},
    20:{"value":"7","suit":suit.diamond},
    21:{"value":"8","suit":suit.diamond},
    22:{"value":"9","suit":suit.diamond},
    23:{"value":"10","suit":suit.diamond},
    24:{"value":"J","suit":suit.diamond},
    25:{"value":"Q","suit":suit.diamond},
    26:{"value":"K","suit":suit.diamond},
    27:{"value":"A","suit":suit.club},
    28:{"value":"2","suit":suit.club},
    29:{"value":"3","suit":suit.club},
    30:{"value":"4","suit":suit.club},
    31:{"value":"5","suit":suit.club},
    32:{"value":"6","suit":suit.club},
    33:{"value":"7","suit":suit.club},
    34:{"value":"8","suit":suit.club},
    35:{"value":"9","suit":suit.club},
    36:{"value":"10","suit":suit.club},
    37:{"value":"J","suit":suit.club},
    38:{"value":"Q","suit":suit.club},
    39:{"value":"K","suit":suit.club},
    40:{"value":"A","suit":suit.heart},
    41:{"value":"2","suit":suit.heart},
    42:{"value":"3","suit":suit.heart},
    43:{"value":"4","suit":suit.heart},
    44:{"value":"5","suit":suit.heart},
    45:{"value":"6","suit":suit.heart},
    46:{"value":"7","suit":suit.heart},
    47:{"value":"8","suit":suit.heart},
    48:{"value":"9","suit":suit.heart},
    49:{"value":"10","suit":suit.heart},
    50:{"value":"J","suit":suit.heart},
    51:{"value":"Q","suit":suit.heart},
    52:{"value":"K","suit":suit.heart}}
    return fulldeck

def chips(mode,data,value=""):
    if mode == "r":
        bf.cls()
        print(f'{bf.ansi.green}Chip Menu{bf.ansi.white}:\n'
        f'[{bf.ansi.blue}R{bf.ansi.white}]Reset Chip Count to {bf.ansi.green}$1000{bf.ansi.white}\n'
        f'[{bf.ansi.blue}C{bf.ansi.white}]Custom Chip Count\n'
        f'[{bf.ansi.blue}E{bf.ansi.white}]Exit Chip Menu\n')
        
        option = bf.getch("Option: ")
        bf.cls()

        if option.lower() == "r":
            data["chips"] = 1000
            print(f'Chip Count = {bf.ansi.green}$1000{bf.ansi.white}\n')
            bf.pause()
            return data["chips"]
        elif option.lower() == "c":
            return chips("custom",data)
        elif option.lower() == "e":
            return data["chips"]
        else:
            print(option)
            return chips(mode,data,value)
    elif mode == "custom":
        bf.cls()
        if value == "":
            try:
                data["chips"] = float(input("Choose chip amount(in dollars): "))
                bf.cls()

                print(f'Chip Count = {bf.ansi.green}${data["chips"]}{bf.ansi.white}\n')
                bf.pause()    
                return data["chips"]
            except ValueError as error:
                return chips("custom",data,"error")
        elif value == "error":
            try:
                print(f'{bf.ansi.red}That number did not work!{bf.ansi.white}')
                data["chips"] = float(input("Choose chip amount(number): "))
                bf.cls()
                print(f'Chip Count = {bf.ansi.green}${data["chips"]}{bf.ansi.white}\n')
                bf.pause()    
                return data["chips"]
            except ValueError as error:
                return chips("custom",data,"error")
    elif mode == "add":
        data["chips"] += value
        return data["chips"]

def checkvalue(value):
    try:
        return int(value)
    except ValueError as error:
        if value == "A":
            return 11
        if value == "J" or value == "Q" or value == "K":
            return 10
def checkvalues(data,player):
    list = []
    for i in data[f'{player}card']:
        try:
            list.append(int(data[f'{player}card'][i]["value"]))
        except ValueError as error:
            pass
    for i in data[f'{player}card']:
        try:
            int(data[f'{player}card'][i]["value"])
        except ValueError as error:
            if data[f'{player}card'][i]["value"] != "A":
                list.append(data[f'{player}card'][i]["value"])
    for i in data[f'{player}card']:
        try:
            int(data[f'{player}card'][i]["value"])
        except ValueError as error:
            if data[f'{player}card'][i]["value"] == "A":
                list.append(data[f'{player}card'][i]["value"])

    if player == "player":
        data["playervalue"] = 0
        for a in list:
            data["playervalue"] += checkvalue(a)
            if a == "A":
                if data["playervalue"] > 21:
                    data["playervalue"] += -10
        return data["playervalue"]
    elif player == "dealer":
        data["dealervalue"] = 0
        for a in list:
            if a != "A":
                data["dealervalue"] += checkvalue(a)
        for a in list:
            if a == "A":
                if data["dealervalue"] > 21:
                    data["dealervalue"] += -10
        return data["dealervalue"]
    

def wincheck(value,stage="0",player="0"):
    if stage == "0":
        if value["playervalue"] == 21:
            return "4"
        else:
            return "0"
    else:
        if value["playervalue"] == 21:
            if value["dealervalue"] == 21:
                return "3"
            else:
                return "1"
        elif value["playervalue"] == value["dealervalue"]:
            return "3"
        elif value["playervalue"] > value["dealervalue"]:
            return "1"
        else:
            return "2"
