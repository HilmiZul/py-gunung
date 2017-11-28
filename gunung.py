from Tkinter import *

form = Tk()

lebar = "800"
tinggi = "400"
form.geometry((lebar+"x"+tinggi))

kanvas = Canvas(width=lebar, height=tinggi, bg="#00aaff")
kanvas.pack()

# gunun sebelah kiri
kanvas.create_oval(0, 200, 400, 700, fill="green")
# gunung sebelah kanan
kanvas.create_oval(350, 150, 800, 650, fill="green")

# matahari
kanvas.create_oval(300, 100, 400, 200, fill="yellow")

# awan
kanvas.create_oval(0, -50, 100, 50, fill="#fff")
kanvas.create_oval(100, -50, 200, 50, fill="#fff")
kanvas.create_oval(200, -50, 300, 50, fill="#fff")
kanvas.create_oval(300, -50, 400, 50, fill="#fff")
kanvas.create_oval(400, -50, 500, 50, fill="#fff")
kanvas.create_oval(500, -50, 600, 50, fill="#fff")
kanvas.create_oval(600, -50, 700, 50, fill="#fff")
kanvas.create_oval(700, -50, 800, 50, fill="#fff")

form.mainloop()
