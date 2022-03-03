from tkinter import *

def RunEntry():
    root = Tk()
    root.geometry("100x80")

    WordSpace = Entry(root, width=40)
    WordSpace.pack()

    def WriteWord():
        file = open("word.txt", "w")
        word = WordSpace.get()
        file.write(word)
        file.close()

    enter = Button(text="ENTER", command=WriteWord)
    enter.pack()

    root.mainloop()

    print("FINE")
    file = open("word.txt", "w")
    file.truncate(0)

RunEntry()