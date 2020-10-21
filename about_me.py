from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import sys


path = r'C:\Users\darke\Downloads\b4f633d2e89c67cc3b0835424a5f3305.png'
background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open(path)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=500, y=500)


root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("200x120")
root.mainloop()


app_root.mainloop()

colours = ("#476042", "yellow")
box = []

for ratio in (0.2, 0.35):
    box.append((canvas_width * ratio,
                canvas_height * ratio,
                canvas_width * (1 - ratio),
                canvas_height * (1 - ratio)))

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

for i in range(2):
    w.create_rectangle(box[i][0], box[i][1], box[i][2], box[i][3], fill=colours[i])

w.create_line(0, 0,  # origin of canvas
              box[0][0], box[0][1],  # coordinates of left upper corner of the box[0]
              fill=colours[0],
              width=3)
w.create_line(0, canvas_height,  # lower left corner of canvas
              box[0][0], box[0][3],  # lower left corner of box[0]
              fill=colours[0],
              width=3)
w.create_line(box[0][2], box[0][1],  # right upper corner of box[0]
              canvas_width, 0,  # right upper corner of canvas
              fill=colours[0],
              width=3)
w.create_line(box[0][2], box[0][3],  # lower right corner pf box[0]
              canvas_width, canvas_height,  # lower right corner of canvas
              fill=colours[0], width=3)




master.mainloop()















date = datetime.now()

jahr = input("Wann bist du geboren? ")
wohnort = input("Wo wohnst du? ")
farbe = input("Was ist deine Lieblingsfarbe? ")
essen = input("Was ist dein Lieblingsessen? ")
getraenk = input("Was ist dein Lieblingsgetraenk? ")

print("† Du bist: ", int(date.year) - int(jahr))
print("Du wohnst in: ", wohnort)

print("       #")
print("         #")
print("        #")
print("       #")
print("       _")
print("     _|=|__________")
print("    /              \\")
print("   /                \\")
print("  /__________________\\")
print("   ||  || /--\ ||  ||")
print("   ||[]|| | .| ||[]||")
print(" ()||__||_|__|_||__||()")
print("^^^^^^^^^^====^^^^^^^^^^^")
print()

print("Deine Lieblingsfarbe ist: ", farbe)

print()

print("Am liebsten speist du: ", essen)

print("                   _")
print("                  / )")
print("            |||| / /")
print("            ||||/ /")
print("           \\__(_/")
print("            ||//")
print("            ||/")
print("            ||")
print("           (||")
print("            """)

print("Am liebsten schlürst du: ", getraenk)

print('''   
  .
 . .
  ...
\~~~~~/
 \   /
  \ /
   V
   |
   |
  ---''')

print("_" * 30)
