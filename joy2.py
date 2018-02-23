from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("ROV")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)
		
        self.batValue = Label(self, text="bat")
        self.batValue.place(x=0, y=0)
        self.count = 0
        self.update_label()

        file = Menu(menu)

        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)

        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=file)

    def update_label(self):
        self.batValue.configure(text = self.count)
        self.batValue.after(1000, self.update_label)
        self.count += 1

    def client_exit(self):
        loop_active = False
        exit()

root = Tk()

root.geometry("400x300")
app = Window(root)

root.mainloop()
