from tkinter import *
from tkinter import messagebox
import pygame
import requests

root = Tk()

joy_values = []
bat_values = []
controller = None

def joy_start():
	global controller
	pygame.init()
	pygame.joystick.init()
	if pygame.joystick.get_count():
		controller = pygame.joystick.Joystick(0)
		messagebox.showinfo("Connected", controller.get_name())
		controller.init()
		update_joystick()
	else:
		messagebox.showwarning("Error", "No Joystick Found!")
		if controller != None:
			controller.quit()
		pygame.quit()

def joyFormat(value):
    value = (value * 100) + 100
    value = int(value)
    return value

def update_joystick():	
	global joyStop
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
		bat_values[x].configure(text = senValues[x])
		senValues[x] = ""

	joyStop = root.after(100, update_joystick)

def create_bat_panel():
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
	joy_labels = ['Left_X', 'Left_Y','Right_X','Right_Y']
	for num in range(4):
		joy_label = Label(root, text= joy_labels[num])
		joy_label.grid(row=7, column=num, padx=10)
		joy_value = Label(root, text= "100")
		joy_value.grid(row=8, column=num)
		joy_value.configure(borderwidth = 1, relief=SUNKEN, padx=8)
		joy_values.append(joy_value)

def create_menu():
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Start", command=joy_start)
	filemenu.add_command(label="Stop", command=stop_joy)
	filemenu.add_command(label="Quit", command=close_window)
	menubar.add_cascade(label="File", menu=filemenu)

	root.config(menu=menubar)

def close_window():
	controller.quit()
	pygame.quit()
	root.quit()

def stop_joy():
	controller.quit()
	pygame.quit()
	root.after_cancel(joyStop)

def main():
	root.geometry("600x400")
	root.title("ROV Controler")
	Label(root, text="Battery Cell Voltage Levels").grid(row=0,
	column=1, columnspan=3, sticky=W )
	Label(root, text="Temperature Zones Farhenheit").grid(row=3,
	column=1, columnspan=3, sticky=W)
	Label(root, text="Joystick Values").grid(row=6, column=1,
	columnspan=3,sticky=W)

	create_menu()
	create_bat_panel()
	create_temp_panel()
	create_joy_panel()

	root.mainloop()

if __name__=="__main__":
	main()

