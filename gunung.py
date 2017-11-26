from Tkinter import *

form = Tk()
form.geometry(("800x400"))

kanvas = Canvas(width="800", height="400", bg="#00aaff")
kanvas.pack()

# gunun sebelah kiri
kanvas.create_oval(0, 200, 400, 700, fill="green")
# gunung sebelah kanan
kanvas.create_oval(350, 150, 800, 650, fill="green")

# matahari
kanvas.create_oval(300, 100, 400, 200, fill="yellow")

form.mainloop()
