import Librarys.BasicFunctions as Bf, Librarys.AsciiEngine as Ae
Bf.cls()

#Info screen:
print(f"{Bf.ansi.italics}{Bf.ansi.blue}Game Test{Bf.ansi.standard}{Bf.ansi.white}(Version 0.1.1[2/3/2022])\n"
f"Created by, {Bf.ansi.green}Nomster Dude, and Mr. Spaceboy{Bf.ansi.white}\n"
"Supports: Windows, MacOS, Linux\n")
Bf.pause()
Bf.cls()

#Initialization:
Posx,Posy = "0","0"
user = ""
a010,a110,a210,a310,a410,a510,a610,a710,a810,a910,a1010 = ".",".",".",".",".",".",".",".",".",".","."
a09,a19,a29,a39,a49,a59,a69,a79,a89,a99,a109 = ".",".",".",".",".",".",".",".",".",".","."
a08,a18,a28,a38,a48,a58,a68,a78,a88,a98,a108 = ".",".",".",".",".",".",".",".",".",".","."
a07,a17,a27,a37,a47,a57,a67,a77,a87,a97,a107 = ".",".",".",".",".",".",".",".",".",".","."
a06,a16,a26,a36,a46,a56,a66,a76,a86,a96,a106 = ".",".",".",".",".",".",".",".",".",".","."
a05,a15,a25,a35,a45,a55,a65,a75,a85,a95,a105 = ".",".",".",".",".",".",".",".",".",".","."
a04,a14,a24,a34,a44,a54,a64,a74,a84,a94,a104 = ".",".",".",".",".",".",".",".",".",".","."
a03,a13,a23,a33,a43,a53,a63,a73,a83,a93,a103 = ".",".",".",".",".",".",".",".",".",".","."
a02,a12,a22,a32,a42,a52,a62,a72,a82,a92,a102 = ".",".",".",".",".",".",".",".",".",".","."
a01,a11,a21,a31,a41,a51,a61,a71,a81,a91,a101 = ".",".",".",".",".",".",".",".",".",".","."
a00,a10,a20,a30,a40,a50,a60,a70,a80,a90,a100 = ".",".",".",".",".",".",".",".",".",".","."

def Level1():
    loop = "1"
    Posx,Posy = "5","5"
    while loop == "1":
        global user
        #globals()[Ae.TakeInput(Posx,Posy)] = "."
        globals()[f'a{Posx}{Posy}'] = "."
        globals()[Ae.TakeInput(Posx,Posy,user)] = f"{Bf.ansi.green}@{Bf.ansi.white}"
        Posx,Posy = Ae.PosChangeX(Posx,user),Ae.PosChangeY(Posy,user)

        print(f"X={Posx} Y={Posy}\n",
        a010,a110,a210,a310,a410,a510,a610,a710,a810,a910,a1010,"\n",
        a09,a19,a29,a39,a49,a59,a69,a79,a89,a99,a109,"\n",
        a08,a18,a28,a38,a48,a58,a68,a78,a88,a98,a108,"\n",
        a07,a17,a27,a37,a47,a57,a67,a77,a87,a97,a107,"\n",
        a06,a16,a26,a36,a46,a56,a66,a76,a86,a96,a106,"\n",
        a05,a15,a25,a35,a45,a55,a65,a75,a85,a95,a105,"\n",
        a04,a14,a24,a34,a44,a54,a64,a74,a84,a94,a104,"\n",
        a03,a13,a23,a33,a43,a53,a63,a73,a83,a93,a103,"\n",
        a02,a12,a22,a32,a42,a52,a62,a72,a82,a92,a102,"\n",
        a01,a11,a21,a31,a41,a51,a61,a71,a81,a91,a101,"\n",
        a00,a10,a20,a30,a40,a50,a60,a70,a80,a90,a100,"\n")

        user = Bf.getch("w,a,s,d = Movment\n"
        "h = Help\n"
        "\nInput: ").lower()
        if user == "h":
            help()
        Bf.cls()
    
def help():
    Bf.cls()

    print("Controls:\n"
    "w = up\n"
    "s = down\n"
    "a = left\n"
    "d = right\n"
    "\n"
    "Information:\n"
    f"{Bf.ansi.green}@{Bf.ansi.white} = Player(You)\n"
    f"{Bf.ansi.red}@{Bf.ansi.white} = Enemy\n")

    Bf.pause()
    Bf.cls()
try:
    Level1()
except BaseException as error:
    Bf.debugerror(error)