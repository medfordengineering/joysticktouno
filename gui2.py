from tkinter import *

count = 0

#def update_count():
#	global count
#	global labels
#	count += 1
#	labels[0].configure(text = count)
#	root.after(1000, update_count)

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


root = Tk()

root.geometry("600x400")
Label(root, text="Battery Cell Voltage Levels").grid(row=0, column=0, columnspan=4)
Label(root, text="Temperature Zones Farhenheit").grid(row=3, column=0, columnspan=5)
create_bat_panel()
create_temp_panel()
#update_count()
#create_text()

root.mainloop()
