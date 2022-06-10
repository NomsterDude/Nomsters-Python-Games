try:
    import Librarys.BasicFunctions as be
except ModuleNotFoundError:
    import BasicFunctions as be

def TakeInput(PosX,PosY,input="",option=""):
    if input == "w":
        nPosX,nPosY = int(PosX),int(PosY)+1
        if nPosY == 11:
            return f"a{nPosX}10"
        return f"a{nPosX}{nPosY}"
    if input == "a":
        nPosX,nPosY = int(PosX)-1,int(PosY)
        if nPosX == -1:
            return f"a0{nPosY}" 
        return f"a{nPosX}{nPosY}"
    if input == "s":
        nPosX,nPosY = int(PosX),int(PosY)-1
        if nPosY == -1:
            return f"a{nPosX}0"
        return f"a{nPosX}{nPosY}"
    if input == "d":
        nPosX,nPosY = int(PosX)+1,int(PosY)
        if nPosX == 11:
            return f"a10{nPosY}"
        return f"a{nPosX}{nPosY}"
    else:
        nPosX,nPosY = int(PosX),int(PosY)
        return f"a{nPosX}{nPosY}"
def PosChangeX(PosX,input=""):
    if input == "w":
        nPosX = int(PosX)
        return nPosX
    if input == "a":
        nPosX = int(PosX)-1
        if nPosX == -1:
           return 0
        return nPosX
    if input == "s":
        nPosX = int(PosX)
        return nPosX
    if input == "d":
        nPosX = int(PosX)+1
        if nPosX == 11:
           return 10
        return nPosX
    else:
        nPosX = int(PosX)
        return nPosX
    
def PosChangeY(PosY,input=""):
    if input == "w":
        nPosY = int(PosY)+1
        if nPosY == 11:
           return 10
        return nPosY
    if input == "a":
        nPosY = int(PosY)
        return nPosY
    if input == "s":
        nPosY = int(PosY)-1
        if nPosY == -1:
           return 0
        return nPosY
    if input == "d":
        nPosY = int(PosY)
        return nPosY
    else:
        nPosY = int(PosY)
        return nPosY