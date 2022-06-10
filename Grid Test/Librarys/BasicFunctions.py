"""Commonly used functions compiled into one library to help keep your code organized

BasicFuntions.help() - Print library info in the console!"""


import os,sys,random,json;from os import system;from getpass import getpass
clsenable = True

class ansi:
    """A class that includes ANSI escape sequences for colors and text formatting.

    Example: print(f"{BasicFunctions.ansi.underline}Hello World!{BasicFunctions.ansi.standard}")

    Colors: black, blue, green, cyan, red, purple, yellow, white.
    Formatting: standard, bold, dim, italics, underline.
    """
    black = "\033[30m"
    blue = "\033[34m"
    green = "\033[32m"
    cyan = "\033[36m"
    red = "\033[31m"
    purple = "\033[35m"
    yellow = "\033[33m"
    white = "\033[37m"

    #Formatting(Could be implemented as a function, but this method is much cleaner.)
    standard = "\033[0m"
    bold = "\033[1m"
    dim = "\033[2m"
    italics = "\033[3m"
    underline = "\033[4m"
    #Standard Text Escape Code(White with no text formatting)
    #\033[0;37;48m

if os.name == "nt":#Defines Windows version of function.
    def cls():
        """Clear the console
        """
        if clsenable == True:
            system("cls")
else:#Defines Linux/MacOS version of function.
    def cls():
        """Clear the console
        """
        if clsenable == True:
            system("clear")

def clstoggle(input=True):
    """Disbale or Enable cls()

    Args:
        input (bool): True or False to Enable or Disable cls(). Defaults to True
    """
    global clsenable
    if type(input) == bool:
        clsenable = input
    else:
        clsenable = True
def pause(message=f"Press [{ansi.blue}Enter{ansi.white}] to continue..."):
    """Pause the console until the user presses [Enter]

    Args:
        message (str, optional): Prints a custom pause message to the console. Defaults to "Press [Enter] to continue...".
    """
    getpass(message)

if os.name == "nt":#Defines Windows version of function.
    from msvcrt import getch as getcha
    def getch(prompt=""):
        """Pauses the script until a key is pressed by the user

        Args:
            prompt (str, optional): Prints a prompt to the console. Defaults to "".

        Returns:
            str: Character pressed by the user.
        """
        if prompt != "":
            print(prompt, end="", flush=True)
        returnable = getcha().decode()
        print()
        return returnable
else:#Defines Linux/MacOS version of function.
    import tty,termios
    def getch(prompt=""):
        """Pauses the script until a key is pressed by the user

        Args:
            prompt (str, optional): Prints a prompt to the console. Defaults to "".

        Returns:
            str: Character pressed by the user.
        """
        if prompt != "":
            print(prompt, end="", flush=True)
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            returnable = sys.stdin.read(1)
            print()
            return returnable
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

def randomselect(var):
    """Returns a random selection from a given list, tuple, string or other iterable.

    Args:
        var (list, tuple, string or other iterable): A radnom selection will be returned from an iterable.

    Returns:
        str or int: Random selection from a given list, tuple, string or other iterable.
    """
    selection = random.choice(list(var))
    return selection

def save(file_name,var_data,file_path="",indentation=0):
    """Writes "var_data" to a json(.json) file. Non-existing files/file paths will be generated by the code

    Args:
        file_name (str): File name to write .json data too.
        var_data (any): Data to be written to a .json file.
        file_path (str, optional): File path to save data to. Defaults to "" or os.path/Save Data/.
        indentation (int, optional): Select .json file indentation level. Defaults to 0
    """
    if file_path == "":
        if not os.path.exists(f'{os.path.join(sys.path[0], "Save Data")}'):
            os.makedirs(f'{os.path.join(sys.path[0], "Save Data")}')
        with open(f'{os.path.join(sys.path[0], "Save Data", file_name)}.json', 'w') as savefile:
            json.dump(var_data,savefile,indent=indentation)
    else:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        with open(f'{os.path.join(file_path, file_name)}.json', 'w') as savefile:
            json.dump(var_data,savefile,indent=indentation)
def load(file_name,file_path=""):
    """Returns data from a json(.json) file

    Args:
        file_name (str): File name to retrieve data from.
        file_path (str, optional): File path to retrieve data from. Defaults to "" or os.path/Save Data/.

    Returns:
        json object: data stored in a .json file.
    """
    if file_path == "":
        with open(f'{os.path.join(sys.path[0], "Save Data", file_name)}.json', 'r') as savefile:
            return json.load(savefile)
    else:
        with open(f'{os.path.join(file_path, file_name)}.json', 'r') as savefile:
            return json.load(savefile)

def textcolor(color="white"):#Uses ANSI escape sequences for each color
    """Change the color of text printed after the function is called.

    Args:
        color (str): Choose a color to change printed text to. Defaults to "white"

    Colors: black, blue, green, cyan, red, purple, yellow, white.
    """
    if color == "black":
        print("\033[30m", end='')
    elif color == "blue":
        print("\033[34m", end='')
    elif color == "green":
        print("\033[32m", end='')
    elif color == "cyan":
        print("\033[36m", end='')
    elif color == "red":
        print("\033[31m", end='')
    elif color == "purple":
        print("\033[35m", end='')
    elif color == "yellow":
        print("\033[33m", end='')
    elif color == "white":
        print("\033[37m", end='')
    else:
        textcolor()

def debugerror(error):
    """Print error info in the console in laymans terms.

    Args:
        error (exception): Used to define the errortype.
    Returns:
        error: The error arg is returned
    Ignores "KeyboardInterrupt".

    Example:\n
    try:
        "Your_Code"
    except BaseException as error:
        BasicFunctions.debugerror(error)
    """
    errortype = type(error).__name__
    errortrace = error.__traceback__
    cls()
    print(f'Exception on line {errortrace.tb_lineno} in file "{errortrace.tb_frame.f_code.co_filename}"\n\n'
        f'{errortype}:')
    if errortype == "AssertionError":
        print("Raised when the assert statement fails.")
    elif errortype == "AttributeError":
        print("Raised on the attribute assignment or reference fails.")
    elif errortype == "EOFError":
        print("Raised when the input() function hits the end-of-file condition.")
    elif errortype == "FloatingPointError":
        print("Raised when a floating point operation fails.")
    elif errortype == "GeneratorExit":
        print("Raised when a generator's close() method is called.")
    elif errortype == "ImportError":
        print("Raised when a specified function can not be found.")
    elif errortype == "IndexError":
        print("Raised when the index of a sequence is out of range.")
    elif errortype == "KeyError":
        print("Raised when a key is not found in a dictionary.")
    elif errortype == "KeyboardInterrupt":
        sys.exit("Exit command used via Keyboard(ctrl+c)")
    elif errortype == "MemoryError":
        print("Raised when an operation runs out of memory.")
    elif errortype == "ModuleNotFoundError":
        print("Raised when a module is not found.")
    elif errortype == "NameError":
        print("Raised when a variable is not found in the local or global scope.")
    elif errortype == "NotImplementedError":
        print("Raised by abstract methods.")
    elif errortype == "OSError":
        print("Raised when a system operation causes a system-related error.")
    elif errortype == "OverflowError":
        print("Raised when the result of an arithmetic operation is too large to be represented.")
    elif errortype == "ReferenceError":
        print("Raised when a weak reference proxy is used to access a garbage collected referent.")
    elif errortype == "RuntimeError":
        print("Raised when an error does not fall under any other category.")
    elif errortype == "StopIteration":
        print("Raised by the next() function to indicate that there is no further item to be returned by the iterator.")
    elif errortype == "SyntaxError":
        print("Raised by the parser when a syntax error is encountered.")
    elif errortype == "IndentationError":
        print("Raised when there is an incorrect indentation.")
    elif errortype == "TabError":
        print("Raised when the indentation consists of inconsistent tabs and spaces.")
    elif errortype == "SystemError":
        print("Raised when the interpreter detects internal error.")
    elif errortype == "TypeError":
        print("Raised when a function or operation is applied to an object of an incorrect type")
    elif errortype == "UnboundLocalError":
        print("Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.")
    elif errortype == "UnicodeError":
        print("Raised when a Unicode-related encoding or decoding error occurs.")
    elif errortype == "UnicodeEncodeError":
        print("Raised when a Unicode-related error occurs during encoding.")
    elif errortype == "UnicodeDecodeError":
        print("Raised when a Unicode-related error occurs during decoding.")
    elif errortype == "UnicodeTranslateError":
        print("Raised when a Unicode-related error occurs during translation.")
    elif errortype == "ValueError":
        print("Raised when a function gets an argument of correct type but improper value.")
    elif errortype == "ZeroDivisionError":
        print("Raised when the second operand of a division or module operation is zero.")
    print(f'\n{error}\n')
    pause()
    return error

def comingsoon():
    """Print "Coming Soon!" in the console
    """
    cls()
    print("Coming soon!\n")
    pause()

def help(function="help"):
    """Prints library/function info in the console

    Args:
        function (str, optional): Pick a specific function or class to get help on. Defaults to "help".
    """
    cls()
    if function=="help":
        print(f"{ansi.italics}{ansi.blue}Basic Functions{ansi.standard}{ansi.white}(Version 0.5.0[5/26/2022])\n"
        f"Created by: {ansi.green}Nomster Dude{ansi.white}\n"
        f"Supports: Windows, MacOS, and Linux\n"
        "Requires: Python 3.0+\n"
        '\n'
        'Functions:\n'
        f'{ansi.purple}cls{ansi.white}({ansi.blue}{ansi.white})                     - Clear the console\n'
        f'{ansi.purple}clstoggle{ansi.white}({ansi.blue}"on/off"{ansi.white})       - Enable/disable the cls() function\n'
        f'{ansi.purple}pause{ansi.white}({ansi.blue}{ansi.white})                   - Pause the program until the user presses [Enter] in the console\n'
        f'{ansi.purple}getch{ansi.white}(prompt)             - Returns the key pressed by the user\n'
        f'{ansi.purple}randomselect{ansi.white}(var)         - Returns a random selection from a given list, tuple, string or other iterable\n'
        f'{ansi.purple}save{ansi.white}(file_name, var_data) - Writes data to a json(.json) file\n'
        f'{ansi.purple}load{ansi.white}(file_name)           - Returns data from a json(.json) file\n'
        f'{ansi.purple}textcolor{ansi.white}({ansi.blue}"color"{ansi.white})        - Change the color of text printed in the console\n'
        f'{ansi.purple}debugerror{ansi.white}({ansi.blue}"error"{ansi.white})       - Convert error messages to laymans terms\n'
        f'{ansi.purple}comingsoon{ansi.white}({ansi.blue}{ansi.white})              - Display a "Coming Soon" message to the user in the console\n'
        f'{ansi.purple}help{ansi.white}({ansi.blue}"function_name"{ansi.white})     - Function argument is optional(also accepts classes), describes how to use a function(s)'
        '\n'
        'Classes:\n'
        f'{ansi.yellow}ansi{ansi.white}                     - Includes ansi escape sequences for colors and text formatting')
        
    elif function=="cls":
        print("Explanation: Used to clear the console.\n"
        "\n"
        "Input:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}cls{ansi.white}()\n'
        "\n"
        'Output(Variable): No output.\n'
        'Output(Console): Clears console.')
    elif function=="clstoggle":
        print(f"Explanation: Disables the {ansi.purple}cls{ansi.white}() function to stop the console from clearing when you run functions like help() and comingsoon().\n"
        "\n"
        "Input:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}clstoggle{ansi.white}({ansi.blue}"on or off"{ansi.white})\n'
        "\n"
        'Output(Variable): Sets clsenable to "0" or "1" within the BasicFunctions library(Does not effect your scripts variables).\n'
        'Output(Console): No output.')
    elif function=="pause":
        print("Explanation: Pauses the console until the user presses [Enter].\n"
        "\n"
        "Input:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}pause{ansi.white}({ansi.blue}"message"{ansi.white})\n'
        "\n"
        'Output(Variable): No output.\n'
        'Output(Console): Prints "Press [Enter] to continue..." to the console. or a custom message.')
    elif function=="getch":
        print("Explanation: Pause the script until a key is pressed by the user.\n"
        "\n"
        "Input:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}getch{ansi.white}()\n'
        "\n"
        "Example:\n"
        f'your_variable {ansi.red}= {ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}getch{ansi.white}({ansi.blue}"What is your favorite letter: "{ansi.white})\n'
        f'{ansi.red}if{ansi.white} your_variable {ansi.red}== {ansi.blue}"x"{ansi.white}\n'
        f'  {ansi.purple}print{ansi.white}(your_variable)\n'
        "\n"
        "Example Output if you press [x](Console):\n"
        f'What is your favorite letter: \n'
        f'x\n'
        "\n"
        'Output(Variable): Returns the key pressed in a string.\n'
        'Output(Console): Prints prompt that is provided as an argument(optional).')
    elif function=="randomselect":
        print("Explanation: Returns a random selection from a given list, tuple, string or other iterable\n"
        "\n"
        "Input:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}randomselect{ansi.white}(var)\n'
        "\n"
        "Example:\n"
        f'var {ansi.red}={ansi.white}[{ansi.blue}"1"{ansi.white},{ansi.blue}"2"{ansi.white},{ansi.blue}"3"{ansi.white}]\n'
        f'{ansi.purple}print{ansi.white}({ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}randomselect{ansi.white}(var))\n'
        "\n"
        "Example Output(Console):\n"
        f'3\n'
        "\n"
        'Output(Variable): Returns a random selection\n'
        'Output(Console): No output.')
    elif function=="save":
        print("Explanation: Writes data to a json(.json) file\n"
        'Data is automatically written to the running files path in a folder called "Save Data"\n'
        'Unless another path is specified via the argument "file_path"\n'
        "\n"
        "Input:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}save{ansi.white}({ansi.blue}"file_name", "var_data"{ansi.white})\n'
        "\n"
        "Example:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}save{ansi.white}({ansi.blue}"file_name_example", "Hello World!"{ansi.white})\n'
        "\n"
        "Example Output(./Save Data/file_name_example.json):\n"
        f'"Hello World!"\n'
        "\n"
        'Output(Variable): Writes data to a json(.json) file.\n'
        'Output(Console): No output.')
    elif function=="load":
        print("Explanation: Returns data from a json(.json) file\n"
        "\n"
        "Input:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}load{ansi.white}({ansi.blue}"file_name"{ansi.white})\n'
        "\n"
        "Example:\n"
        f'variable {ansi.red}= {ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}load{ansi.white}({ansi.blue}"file_name_example"{ansi.white})\n'
        f'{ansi.purple}print{ansi.white}(variable)\n'
        "\n"
        "Example Output(Console):\n"
        f'Hello World!\n'
        "\n"
        'Output(Variable): Returns data stored in a json(.json) file.\n'
        'Output(Console): No output.')
    elif function=="textcolor":
        print("Explanation: Change the color of text printed after the function is called.\n"
        "\n"
        "Input:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}textcolor{ansi.white}({ansi.blue}"color"{ansi.white})\n'
        "\n"
        "Example:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}textcolor{ansi.white}({ansi.blue}"green"{ansi.white})\n'
        f'{ansi.purple}print{ansi.white}({ansi.blue}"Hello World!"{ansi.white})\n'
        "\n"
        "Example Output(Console):\n"
        f'{ansi.green}Hello World!{ansi.white}\n'
        "\n"
        'Output(Variable): No output.\n'
        'Output(Console): Changes color of printed text until it is changed again.')
    elif function=="debugerror":
        print("Explanation: Prints error info in the console in laymans terms.\n"
        "\n"
        "Input:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}debugerror{ansi.white}({ansi.blue}"error"{ansi.white})\n'
        "\n"
        "Example:\n"
        f'{ansi.red}try{ansi.white}:\n'
        f'  Your_Code\n'
        f'{ansi.red}except {ansi.yellow}BaseException {ansi.red}as {ansi.white}error:\n'
        f'  {ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}debugerror{ansi.white}(error)\n'
        "\n"
        "Example Output(Console):\n"
        'NameError:\n'
        'Raised when a variable is not found in the local or global scope.\n'
        '\n'
        "name 'Your_Code' is not defined\n"
        '\n'
        'Press [Enter] to continue...\n'
        "\n"
        'Output(Variable): No output.\n'
        'Output(Console): Prints error info then pauses the console until the user presses [Enter]. Ignores keyboard interrupt.')
    elif function=="comingsoon":
        print('Explanation: Prints "Coming Soon!" in the console\n'
        "\n"
        "Input:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}comingsoon{ansi.white}()\n'
        "\n"
        'Output(Variable): No output.\n'
        'Output(Console): Prints "Coming soon!" then pauses the console.')
    elif function=="ansi":
        print("Explanation: A python class that includes ansi escape sequences for colors and text formatting\n"
        "\n"
        "Input:\n"
        '{BasicFunctions.ansi.color_or_formatting_option}\n'
        "\n"
        "Example:\n"
        'print(f"{BasicFunctions.ansi.underline}Hello World!{BasicFunctions.ansi.standard} Hello World!")\n'
        "\n"
        "Example Output(Console):\n"
        f'{ansi.underline}Hello World!{ansi.standard} Hello World!\n'
        "\n"
        'Output(Variable): No output.\n'
        'Output(Console): Changes color/formatting of printed text until it is changed again.')
    elif function=="Null":
        print("Explanation:\n"
        "\n"
        "Input:\n"
        f'{ansi.yellow}BasicFunctions{ansi.white}.{ansi.purple}function_name{ansi.white}({ansi.blue}{ansi.white})\n'
        "\n"
        "Example:\n"
        f'\n'
        "\n"
        'Output(Variable):\n'
        'Output(Console):')
    else:
        print(f"{ansi.italics}{ansi.blue}Basic Functions{ansi.standard}{ansi.white}(Version 0.5.0[5/2/2022])\n"
        f"Created by: {ansi.green}Nomster Dude{ansi.white}\n"
        f"Supports: Windows, MacOS, and Linux\n"
        "Requires: Python 3.0+\n"
        '\n'
        f'{ansi.bold}{ansi.red}Function or Class "{function}" does not exist! Try again with an option below!{ansi.standard}{ansi.white}\n'
        'Functions:\n'
        'cls          - Clear the console\n'
        'clstoggle    - Enable/disable the cls() function\n'
        'pause        - Pause the program until the user presses [Enter] in the console\n'
        'getch        - Returns the key pressed by the user\n'
        'randomselect - Returns a random selection from a given list, tuple, string or other iterable\n'
        'save         - Writes data to a json(.json) file\n'
        'load         - Returns data from a json(.json) file\n'
        'textcolor    - Change the color of text printed in the console\n'
        'debugerror   - Convert error messages to laymans terms\n'
        'comingsoon   - Display a "Coming Soon" message to the user in the console\n'
        'help         - Function argument is optional(also accepts classes), describes how to use a function(s)'
        '\n'
        'Classes:\n'
        'ansi         - Includes ansi escape sequences for colors and text formatting')

    print()
    pause()