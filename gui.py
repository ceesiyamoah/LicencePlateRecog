# from tkinter import *

# root=Tk()

# e=Entry(root, width=50)
# e.pack()

# def myClick():
#     myLabel=Label(root,text='Choose a picture')
#     myLabel.pack()

# myButton=Button(root, text='here', command=myClick)
# myButton.pack()

# root.mainloop()





# DIRECTORY SELECTION
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askopenfilename()
print(folder_selected)
mainloop()



#Choosing between arrival and departure
# from tkinter import *

# root = Tk()

# v = IntVar()
# def radioChoice(value):
#     myLabel=Label(root, text=value)
#     myLabel.pack()
#     global val
#     v.set(value)
#     val=v.get()

# Radiobutton(root, text="Arrival", variable=v, value=1, command=lambda: radioChoice(v.get())).pack(anchor=W)
# Radiobutton(root, text="Departure", variable=v, value=0, command=lambda: radioChoice(v.get())).pack(anchor=W)

# myLabel=Label(root, text=v.get()).pack()
# OkButton=Button(root,text='submit',command=root.quit)
# OkButton.pack()


# mainloop()
# print('out',val)


#Image display
# from tkinter import *
# from PIL import ImageTk,Image

# root=Tk()
# myImg=ImageTk.PhotoImage(Image.open('licencePlate.png'))
# myImageLabel=Label(image=myImg)
# myImageLabel.pack()
# name='Cyril'
# myNameLabel=Label(root, text=name).pack()
# mainloop()