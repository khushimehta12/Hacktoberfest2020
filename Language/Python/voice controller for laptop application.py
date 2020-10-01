import pyttsx3
import os
while True:
	print("********************************Hey welcome to my chat world**************************************")
	p=input("chat with me with your requirments:",end='')
	
	if("run" in p) or ("launch" in p) and ("chrome " in p):
		os.system("chrome")
		print("hey u launch it succesfully")

	elif("run" in p) or ("launch" in p) and ("notepad " in p) :
		os.system("notepad")
		print("hey u launch it succesfully")

	elif("run" in p) or("launch" in p) and ("player " in p) and ("media" in p):
		os.system("wmplayer")
        print("hey u launch it succesfully")

	elif("run" in p) or ("launch" in p) and ("calculator " in p) or ("calci" in p):
		os.system("calc") 
		print("hey u launch it succesfully")	 

	elif("exit" in p) and ("quit" in p):
		break
	else:
	    print("does not support")	
