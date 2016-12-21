# -*- coding: utf-8 -*-
import ImageTk,os,sys,platform
import time
from Tkinter import *
class gui():
		def __init__(self):
			self.graf()	
			
		def wordlist(self):
			self.toplevel=Toplevel()
			self.toplevel.geometry('600x400')
			
		def graf(self):
			self.label=Label(root,text='-'*195,fg='green')
			self.label.place(relx=0.01,rely=0.03)
			self.label3=Label(root,text='Operation system : %s'%platform.system())
			self.label3.place(relx=0.01,rely=0.06)
			self.label4=Label(root,text='Time : %s'%time.ctime())
			self.label4.place(relx=0.01,rely=0.1)
			self.label
root=Tk()
root.title('Omega')
root.geometry('800x700')
root.tk_setPalette('#333342')
log=ImageTk.PhotoImage(file='omega.jpg')
label=Label(root,image=log)
label.place(relx=0.38,rely=0.04)
termf = Label(root,height=18,width=300)
termf.place(relx=0.01,rely=0.55)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 120x200 -sb &' % wid)
if __name__ == '__main__':
	app=gui()
	root.mainloop()
