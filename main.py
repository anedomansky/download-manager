from tkinter import *
from tkinter import ttk
import pyperclip

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# clipboard test
def updateClipboard():
    cliptext = pyperclip.paste()
    processClipping(cliptext=cliptext)
    root.after(ms=100, func=updateClipboard)

def processClipping(cliptext):
    cliptextCleaned = cleanClipText(cliptext=cliptext)
    label["text"] = cliptextCleaned

def cleanClipText(cliptext):
    #Removing all characters > 65535 (that's the range for tcl)
    cliptext = "".join([c for c in cliptext if ord(c) <= 65535])
    return cliptext

def onClick(labelElem):
    labelText = labelElem["text"]
    print(labelText)
    pyperclip.copy(labelText)

if __name__ == '__main__':
    root = Tk()
    root.title("Feet to Meters")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    feet = StringVar()
    meters = StringVar()

    feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(W, E))

    ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

    ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

    # clipboard test
    ttk.Label(mainframe, text="clipboard content").grid(column=1, row=3, sticky=E)
    label = ttk.Label(mainframe, text="")
    label.bind("<Button-1>", lambda event, labelElem=label: onClick(labelElem))
    # label.pack()
    updateClipboard()


    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    feet_entry.focus()
    root.bind('<Return>', calculate)

    root.mainloop()
