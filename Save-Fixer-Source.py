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

#=======================#

data_in_byte = b'\x01\x00\x00\x00' #From V1 (UI Writes bytes to file.)
def myClick0():
    message0 = Label(root2, text="Fixed Data Open-Sector.")
    message0.pack()
    message0 = Label(root2, text="Debug Information: x00x01; x16x00000001.")
    message0.pack()
    message0 = Label(root2, text="------------")
    message0.pack()
    data_in_byte = b'\x01\x00\x00\x00' 
    Data = "Data" 

    with open(Data, 'rb+') as binary_file:
      binary_file.seek(00) 
      binary_file.write(data_in_byte) 
      
    with open(Data, 'rb+') as binary_file:
      binary_file.seek(16) 
      binary_file.write(data_in_byte) 

myButton0 = Button(root1, text="Fix: Save-Data Open Sector", command=myClick0, fg="white", bg="black")
myButton0.pack()

#=======================#

data_in_byte = b'\x01\x00\x00\x00' #From V2 (UI writes bytes to file)
def myClick1():
    message1 = Label(root2, text="Fixed: Clothes/Apparel-Data Sector.")
    message1.pack()
    message1 = Label(root2, text="Debug Information: x52x00000000.")
    message1.pack()
    message1 = Label(root2, text="Debug Information: x56x10000000.")
    message1.pack()
    message1 = Label(root2, text="Debug Information: x60x20000000.")
    message1.pack()
    message1 = Label(root2, text="------------")
    message1.pack()
    data_in_byte = b'\x01\x00\x00\x00' 
    Data = "Data" 

    data_in_byte = b'\x00\x00\x00\x00'
    with open(Data, 'rb+') as binary_file:
      binary_file.seek(52) 
      binary_file.write(data_in_byte) 

    data_in_byte = b'\x01\x00\x00\x00'
    with open(Data, 'rb+') as binary_file:
      binary_file.seek(56) 
      binary_file.write(data_in_byte) 

    data_in_byte = b'\x02\x00\x00\x00'
    with open(Data, 'rb+') as binary_file:
      binary_file.seek(60) 
      binary_file.write(data_in_byte) 

myButton1 = Button(root1, text="Fix: Clothes/Apparel-Data Sector", command=myClick1, fg="white", bg="black")
myButton1.pack()

      
#=======================#

data_in_byte = b'\xE4\x44\x94\x89\xF1\x41\x83\x9E\xC9\xC4' #From V3 (UI writes bytes to file)
def myClick2():
    message2 = Label(root2, text="Fixed: Spawn/Coordinate Sector.")
    message2.pack()
    message2 = Label(root2, text="Debug Information: x22x00000000.")
    message2.pack()
    message2 = Label(root2, text="------------")
    message2.pack()
    data_in_byte = b'\xE4\x44\x94\x89\xF1\x41\x83\x9E\xC9\xC4' 
    Data = "Data" 

    data_in_byte = b'\xE4\x44\x94\x89\xF1\x41\x83\x9E\xC9\xC4'
    with open(Data, 'rb+') as binary_file:
      binary_file.seek(22) 
      binary_file.write(data_in_byte) 

myButton2 = Button(root1, text="Fix: Spawn/Coordinate Sector", command=myClick2, fg="white", bg="black")
myButton2.pack()

#=======================#

print("!!!ERROR WINDOW!!!") #From V1 (console)
print(" ")
print("All Error(s)/Error-Code(s) Will Appear Here.")
print(" ")
print("If You Encounter An Error/Error-Code. Please Contact Cracko298 (via) GitHub.")
print(" ")
print("https://github.com/Cracko298 (or) https://cracko298.xyz/")
print(" ")

root1.mainloop()
root2.mainloop()