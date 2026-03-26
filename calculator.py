#BUILDING CALCULATOR USING PYTHON 
#BY- SHREYA SINGH

#CODE- 
import tkinter as tk #importing tkinter for creating gui

root= tk.Tk()
root.title("Calculator") 

entry = tk. Entry(root,width =20, font=("Arial",30)) #formatting the look of calculator
entry.grid(row=0,column=0, columnspan=4) 

def click(value): #function for entering and adding more values
    current= entry.get()
    entry.delete(0,tk.END)
    entry.insert(0, current+ value)
    
def clear(): #function for clearing values
    entry.delete(0,tk.END)
    
def equal():
    try:
        expression = entry.get().replace('%', '/100')   # Convert % to /100
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def backspace(): #function for backspacing one value
    current =entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current[:-1])
    
def square(): #function for squaring any written value
    try:
        value= float(entry.get())
        result=value**2
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")
        
#defining every button 

#row 1
tk.Button(root, text="x²",width=8,height=3, bg="#87cefa", fg="black", bd=2, relief="solid",command=square).grid(row=1,column=0, sticky="nsew") #command as the function for squaring values
tk.Button(root, text="%", width=8, height=3, bg="#87cefa", fg="black", bd=2, relief="solid",  command=lambda: click("%")).grid(row=1, column=1, sticky="nsew") #command as the function for calculating %
tk.Button(root, text="⌫", width=8,height=3, bg="#87cefa", fg="black", bd=2, relief="solid", command=backspace).grid(row=1, column=2, sticky="nsew") #command as the function for backspacing
tk.Button(root, text="C", bg="#87cefa", fg="black" ,width=8, height=3, bd=2, relief="solid",  command=clear).grid(row=1, column=3, sticky="nsew") #command as the function for clearing values

#row 2
tk.Button(root, text="7", width=8, height=3, bg="#F5F5DC", fg="black", bd=2, relief="solid",   command=lambda: click("7")).grid(row=2, column=0, sticky="nsew")
tk.Button(root, text="7", width=8, height=3, bg="#F5F5DC", fg="black",  bd=2, relief="solid",  command=lambda: click("7")).grid(row=2, column=0, sticky="nsew")
tk.Button(root, text="8", width=8, height=3, bg="#F5F5DC", fg="black", bd=2, relief="solid", command=lambda: click("8")).grid(row=2, column=1, sticky="nsew")
tk.Button(root, text="9", width=8, height=3, bg="#F5F5DC", fg="black", bd=2, relief="solid",  command=lambda: click("9")).grid(row=2, column=2, sticky="nsew")
tk.Button(root, text="/", bg="#87cefa", fg="black", width=8, height=3, bd=2, relief="solid",command=lambda: click("/")).grid(row=2, column=3, sticky="nsew")

#row 3
tk.Button(root, text="4", width=8, height=3, bg="#F5F5DC", fg="black", bd=2, relief="solid",   command=lambda: click("4")).grid(row=3, column=0, sticky="nsew")
tk.Button(root, text="5", width=8, height=3, bg="#F5F5DC", fg="black", bd=2, relief="solid",   command=lambda: click("5")).grid(row=3, column=1, sticky="nsew")
tk.Button(root, text="6", width=8, height=3, bg="#F5F5DC", fg="black",bd=2, relief="solid",   command=lambda: click("6")).grid(row=3, column=2, sticky="nsew")
tk.Button(root, text="*",  bg="#87cefa", fg="black" ,width=8, height=3, bd=2, relief="solid",   command=lambda: click("*")).grid(row=3, column=3, sticky="nsew")

#row 4 
tk.Button(root, text="1", width=8, height=3, bg="#F5F5DC", fg="black", bd=2, relief="solid",   command=lambda: click("1")).grid(row=4, column=0, sticky="nsew")
tk.Button(root, text="2", width=8, bg="#F5F5DC", fg="black", bd=2, relief="solid", command=lambda: click("2")).grid(row=4, column=1, sticky="nsew")
tk.Button(root, text="3", width=8, bg="#F5F5DC", fg="black",bd=2, relief="solid",  command=lambda: click("3")).grid(row=4, column=2, sticky="nsew")
tk.Button(root, text="-", bg="#87cefa", fg="black", width=8, height=3,bd=2, relief="solid",command=lambda: click("-")).grid(row=4, column=3, sticky="nsew")

#row 5
tk.Button(root, text="0", bg="#F5F5DC", fg="black", bd=2, relief="solid",  command=lambda: click("0")).grid(row=5, column=0, sticky="nsew")
tk.Button(root, text=".",  bg="#87cefa", fg="black" ,width=8, height=3, bd=2, relief="solid",   command=lambda: click(".")).grid(row=5, column=1, sticky="nsew")
tk.Button(root, text="=",  bg="#87cefa", fg="black" ,width=8, height=3, bd=2, relief="solid", command=equal).grid(row=5, column=2, sticky="nsew") #command as the function for resulting final value
tk.Button(root, text="+", bg="#87cefa", fg="black"  ,width=8, height=3, bd=2, relief="solid", command=lambda: click("+")).grid(row=5, column=3, sticky="nsew")

root.mainloop()
    