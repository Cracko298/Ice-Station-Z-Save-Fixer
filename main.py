import os.path
import os
import sys
import tkinter
from tkinter import *

root1 = Tk()
root1.title('ISZ - Save Data Fixer')
root1.geometry("360x480")

root2 = Tk()
root2.title('Output - Debugger')
root2.geometry("375x480")

data_in_byte = b'\x01'
def myClick1():
    message1 = Label(root2, text="Fixed Data Open-Sector.")
    message1.pack()
    message1 = Label(root2, text="Debug Information: x00x01; x16x00000001.")
    message1.pack()
    message1 = Label(root2, text="------------")
    message1.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x01' 
    #Bytes to write to file
    Data = "Data" 
    #Name of file

    with open(Data, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(00) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

myButton0 = Button(root1, text="Fix: Save-Data Open Sector", command=myClick1, fg="white", bg="black")
myButton0.pack()

print("!!!ERROR WINDOW!!!")
print(" ")
print("All Error(s)/Error-Code(s) Will Appear Here.")
print(" ")
print("If You Encounter An Error/Error-Code. Please Contact Cracko298 (via) GitHub.")
print(" ")
print("https://github.com/Cracko298 (or) https://cracko298.xyz/")
print(" ")

root1.mainloop()
root2.mainloop()