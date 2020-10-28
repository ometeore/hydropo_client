import led
import schedule


def receive(message):
	led.blink_party()
	print("we are in the receive functio of manager") 

	
def runing_schedule():
	var_glob_file = open("glob.txt","r")
