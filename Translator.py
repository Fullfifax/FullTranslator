# Compile this file if you want to launch the application

import tkinter
from tkinter import ttk, messagebox
from Traducteur import Traduction


application = tkinter.Tk()
application.minsize(860, 640)
application.title("Fulltranslator Reflect")
application.wm_iconbitmap("icon.ico")       

def get():
	source = choiceLanguage1.get()
	destination = choiceLanguage2.get()
	message = insertText.get(1.0, tkinter.END)
	translation = Traduction()
	textes = translation.translation(txt = message, src = source, dest = destination)
	showText.delete(1.0, tkinter.END)
	showText.insert(tkinter.END, textes)


mainFrame = tkinter.Frame(application)
mainFrame.pack(fill = tkinter.BOTH)

header = tkinter.Label(application, text="#Fulltranslator :)",
						fg="white", font=("Times new roman", 25), bg='teal', height=2) 
header.pack(fill = tkinter.BOTH)

languageList = Traduction().languageList


frame_languageList1 = tkinter.Frame(application, bg ="lightseagreen", bd = 5)
frame_languageList1.place(relx = 0.41, rely = 0.18, relwidth = 0.78, 
						relheight = 0.08, anchor = "n")
label_languageList1 = tkinter.Label(frame_languageList1, text = "Choose the language to translate",
									fg = "teal", bg = "white", font = ("Arial", 12))
label_languageList1.place(relwidth = 0.65, relheight = 1)
choiceLanguage1 =  ttk.Combobox(frame_languageList1, values = languageList, font = 10)
choiceLanguage1.set("french")
choiceLanguage1.place(relx = 0.7, relwidth = 0.3, relheight = 1)

frame_insertText = tkinter.Frame(application, bg = "lightseagreen", bd = 10)
frame_insertText.place(relx = 0.41, rely = 0.25, 
						relwidth = 0.78, relheight = 0.2, anchor = "n")
insertText = tkinter.Text(frame_insertText, font = ("Arial", 12)) 
insertText.place(relwidth = 1, relheight = 1)

scroll = ttk.Scrollbar(frame_insertText, orient=tkinter.VERTICAL, command=insertText.yview)
scroll.pack(side = tkinter.RIGHT, fill = tkinter.Y)
insertText.config(yscrollcommand = scroll.set)

#---------------------------------------------------------------------------------------------------------

button = tkinter.Button(application, text = "Traduire",  
						bg = "white", fg = "teal", font = ("Arial", 12), command = get)
button.place(relx = 0.40, rely = 0.49, width = 80, anchor = "n")

#---------------------------------------------------------------------------------------------------------

frame_languageList2 = tkinter.Frame(application, bg ="lightseagreen", bd = 5)
frame_languageList2.place(relx = 0.41, rely = 0.58, 
							relwidth = 0.78, relheight = 0.08, anchor = "n")
label_languageList2 = tkinter.Label(frame_languageList2, text = "Choose the language for the translation",
									fg = "teal", bg = "white", font = ("Arial", 12))
label_languageList2.place(relwidth = 0.65, relheight = 1)
choiceLanguage2 =  ttk.Combobox(frame_languageList2, values = languageList, font = 10)
choiceLanguage2.set("english")
choiceLanguage2.place(relx = 0.7, relwidth = 0.3, relheight = 1)

frame_showText = tkinter.Frame(application, bg = "lightseagreen", bd = 10)
frame_showText.place(relx = 0.41, rely = 0.65, 
						relwidth = 0.78, relheight = 0.2, anchor = "n")
showText = tkinter.Text(frame_showText, font = ("Arial", 12)) 
showText.place(relwidth = 1, relheight = 1)

scroll = ttk.Scrollbar(frame_showText, orient=tkinter.VERTICAL, command=showText.yview)
scroll.pack(side = tkinter.RIGHT, fill = tkinter.Y)
showText.config(yscrollcommand = scroll.set)

#------------------------------------------------------------------------------------------------------------------------------

frameMenu = tkinter.Frame(application, bg = "teal", bd = 5)
frameMenu.pack(fill = tkinter.BOTH, side = "right")

def show_info():
	messagebox.showinfo("About", "Fulltranslator is a simple translator application developped by Fullfifax")

menu1 = tkinter.Button(frameMenu, text = "About", fg = "teal", font = ("Arial", 10),
						bg = "white", width = 14, command = show_info)
menu1.grid(row = 3, column = 1, pady = 45)

menu2 = tkinter.Button(frameMenu, text = "Quit", fg = "teal", font = ("Arial", 10),
						bg = "white", width = 14, command = application.quit)
menu2.grid(row = 4, column = 1)

#------------------------------------------------------------------------------------------------------------------------------

application.mainloop()