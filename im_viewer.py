from tkinter import *
from PIL import Image, ImageTk
from os import listdir
from os.path import isfile, join
from image_cut import cut_image
from image_resize import resize
import pssh

root = Tk()
root.title("Image Preview")
root.resizable(0, 0)
# create frame
frame=Frame(root, width=1800, height=1200, bg='white', relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)

# Get all the image filenames in the folder
onlyfiles = [f for f in listdir("/Users/zheyu/Downloads/COMP 89/Presentation") if isfile(join("/Users/zheyu/Downloads/COMP 89/Presentation", f))]
images = []
for filename in onlyfiles:
    if not filename.startswith('.'):
        pathname = "Presentation/"+filename
        images.append( ImageTk.PhotoImage(Image.open(pathname)))

print(images)
resize()
# configure the image to the Label in frame
i = 0
image_label = Label(frame, image=images[i])
image_label.pack()
# create functions to display
# previous an next images
def previous():
    global i
    i = i - 1
    try:
        image_label.config(image=images[i])
        cut_image("Presentation/"+onlyfiles[i])
        pssh.main()
    except:
        i = 0
        previous()
def next():
    global i
    i = i + 1
    try:
        image_label.config(image=images[i])
        cut_image("Presentation/"+onlyfiles[i])
        pssh.main()
    except:
        i = -1
        next()
# create buttons    
btn1 = Button(root, text="Previous", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=previous)
btn1.pack(side=LEFT, padx=60, pady=5)
btn2 = Button(root, text="Next", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=next)
btn2.pack(side=LEFT, padx=60, pady=5)
btn3 = Button(root, text="Exit", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
btn3.pack(side=LEFT, padx=60, pady=5)
root.mainloop()
