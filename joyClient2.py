from tkinter import *
import pygame
import requests

pygame.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()
root = Tk()

joy_values = []

def joyFormat(value):
    value = (value * 100) + 100
    value = int(value)
    return value

def update_joystick():
	global joy_values
	joyKeys = ['LV', 'LH', 'RV', 'RH']
	butKeys = ['B1', 'B2', 'B3', 'B4']
	senValues = ['0','0','0','0']
	joyValues = [0,0,0,0] 
	butValues = [0,0,0,0] 
	senIndex = 0
	pygame.event.pump()
	for x in range (0, 4):
		joyValues[x] = controller.get_axis(x)
		joyValues[x] = joyFormat(joyValues[x])
		joy_values[x].configure(text = joyValues[x])
	for x in range (0, 4):
		butValues[x] = controller.get_button(x)
	joyDict = dict(zip(joyKeys, joyValues))
	butDict = dict(zip(butKeys, butValues))
	print(joyDict)
	print(butDict)
	payload = joyDict
	status = requests.get('http://192.168.1.8/drive/',params=payload)
	for x in range (0, len(status.text)):
		if status.text[x].isdigit():
			senValues[senIndex] += status.text[x]
		elif status.text[x] == ',':
			senIndex += 1
		elif status.text[x] == 'T':
			break

	for x in range (0, 4):
		print (senValues[x])
		senValues[x] = ""

	root.after(100, update_joystick)

def create_bat_panel():
	bat_values = []
	for num in range(4):
		bat_label = Label(root, text= "Cell_" + str(num))
		bat_label.grid(row=1, column=num, padx=10)
		bat_value = Label(root, text= "5.00")
		bat_value.grid(row=2, column=num)
		bat_value.configure(borderwidth = 1, relief=SUNKEN, padx=8)
		bat_values.append(bat_value)

def create_temp_panel():
	temp_labels = ['Motor1', 'Motor2','Motor3','Ambient','Processor']
	temp_values = []
	for num in range(5):
		temp_label = Label(root, text= temp_labels[num])
		temp_label.grid(row=4, column=num, padx=10)
		temp_value = Label(root, text= "5.00")
		temp_value.grid(row=5, column=num)
		temp_value.configure(borderwidth = 1, relief=SUNKEN, padx=8)
		temp_values.append(temp_value)

def create_joy_panel():
	joy_labels = ['Left_X', 'Left_Y','Right_X','Right_X']
#	joy_values = []
	for num in range(4):
		joy_label = Label(root, text= joy_labels[num])
		joy_label.grid(row=7, column=num, padx=10)
		joy_value = Label(root, text= "100")
		joy_value.grid(row=8, column=num)
		joy_value.configure(borderwidth = 1, relief=SUNKEN, padx=8)
		joy_values.append(joy_value)

def main():
#	pygame.init()
#	pygame.joystick.init()
#	controller = pygame.joystick.Joystick(0)
#	controller.init()
#	root = Tk()
	root.geometry("600x400")
	Label(root, text="Battery Cell Voltage Levels").grid(row=0, column=0, columnspan=4)
	Label(root, text="Temperature Zones Farhenheit").grid(row=3, column=0, columnspan=5)
	Label(root, text="Joystick Values").grid(row=6, column=0, columnspan=5)
	create_bat_panel()
	create_temp_panel()
	create_joy_panel()
	update_joystick()

	root.mainloop()
#update_count()
#create_text()

if __name__=="__main__":
	main()

