# -*- coding: utf-8 -*-
import ImageTk,os,sys,platform
import time,webbrowser,smtplib
from smtplib import SMTPException
from Tkinter import *
from json import load
from urllib2 import urlopen
from urllib2 import URLError
import tkMessageBox
from socket import *
from socket import gethostbyname, gaierror
class gui():
		
		def __init__(self):
			self.gui()
	
		
			
		def delete(self):
			self.text.delete('1.0',END)
		def call_fb(self,event=None):
			webbrowser.open_new(r"https://www.facebook.com/python-azcom-318346491536536/")
		def call_gt(self,event=None):
			webbrowser.open_new(r"https://github.com/techaz")
	
			
				
		def smtp_gmail(self):
			From=self.entry_from.get()
			To=self.entry_to.get()
			Text=self.text.get(1.0,END)
			key=self.entry_key.get()
			try:
				session=smtplib.SMTP('smtp.gmail.com',587)
				session.ehlo()
				session.starttls()
				session.ehlo()
				session.login(From,str(key))
				session.sendmail(From,To,Text)
				self.listbox.delete(0,END)

				self.listbox.insert(0,'Message send succesfully')
				session.quit()
			except smtplib.SMTPException:
				self.listbox.delete(0,END)
				self.listbox.insert(0,'[-] Error')
		def smtp_live(self):
			From=self.entry_from.get()
			To=self.entry_to.get()
			Text=self.text.get(1.0,END)
			key=self.entry_key.get()
			try:
				session=smtplib.SMTP('smtp.live.com',587)
				session.ehlo()
				session.starttls()
				session.ehlo()
				session.login(From,str(key))
				session.sendmail(From,To,Text)
				self.listbox.delete(0,END)

				self.listbox.insert(0,'Message send succesfully')
				session.quit()
			except smtplib.SMTPException:
				self.listbox.delete(0,END)
				self.listbox.insert(0,'[-] Error')
		def smtp_yahoo(self):
			From=self.entry_from.get()
			To=self.entry_to.get()
			Text=self.text.get(1.0,END)
			key=self.entry_key.get()
			try:
				session=smtplib.SMTP('smtp.mail.yahoo.com',465)
				session.ehlo()
				session.starttls()
				session.ehlo()
				session.login(From,str(key))
				session.sendmail(From,To,Text)
				self.listbox.delete(0,END)

				self.listbox.insert(0,'Message send succesfully')
				session.quit()
			except smtplib.SMTPException:
				self.listbox.delete(0,END)
				self.listbox.insert(0,'[-] Error')
		def toplevel(self):
			self.toplevel=Toplevel()
			self.toplevel.title('Sendmail')
			self.toplevel.geometry('700x800')
			self.img=PhotoImage(file="sms.png")
			
			try:
				
				ip = load(urlopen('http://httpbin.org/ip'))['origin']
				self.label_ip=Label(self.toplevel,text='[+]'+' '+ip,fg='green')
				self.label_ip.place(relx=0.18,rely=0.03)
			except URLError, e:	
				self.label_ip=Label(self.toplevel,text='[-] check you internet',fg='red')
				self.label_ip.place(relx=0.18,rely=0.03)
			self.label_youip=Label(self.toplevel,text='IP :',fg='#0606F4')
			self.label_youip.place(relx=0.08,rely=0.03)	
			self.panel=Label(self.toplevel,image=self.img,height=220)
			self.panel.place(relx=0.45,rely=0.02)
			self.label_from=Label(self.toplevel,text='From')
			self.label_from.place(relx=0.08,rely=0.12)
			self.label_to=Label(self.toplevel,text='To')
			self.label_to.place(relx=0.08,rely=0.18)
			self.label_key=Label(self.toplevel,text='Key')
			self.label_key.place(relx=0.08,rely=0.24)
			self.label_text=Label(self.toplevel,text='Text',font='bold')
			self.label_text.place(relx=0.08,rely=0.3)
			self.entry_from=Entry(self.toplevel)
			self.entry_from.place(relx=0.14,rely=0.12)
			self.entry_to=Entry(self.toplevel)
			self.entry_to.place(relx=0.14,rely=0.18)
			self.entry_key=Entry(self.toplevel,show="*")
			self.entry_key.place(relx=0.14,rely=0.24)
			self.text=Text(self.toplevel,width=80,height=13,bg='#3A2C2C')
			self.text.place(relx=0.08,rely=0.36)
			self.button_send=Button(self.toplevel,text='Send',bg='#152D15'\
			,cursor='hand2',width=5,command=self.smtp_gmail)
			self.button_send.place(rely=0.65,relx=0.09)
			
			self.button_del=Button(self.toplevel,text='clear',width=5,command=self.delete)
			self.button_del.place(relx=0.195,rely=0.65)
			self.button_refr=Button(self.toplevel,text='Refresh'\
			,bg='red',fg='black',cursor='hand2')
			self.button_refr.place(relx=0.3,rely=0.65)
			self.listbox=Listbox(self.toplevel,width=33,height=15,bg='black')
			self.listbox.place(relx=0.5,rely=0.65)
			self.label_contact=Label(self.toplevel,text='Contact mail :',fg='white')
			self.label_contact.place(relx=0.08,rely=0.9)
			self.label_mail=Label(self.toplevel,text='pythonaz@yahoo.com'\
			,fg='#4F4F9E')
			self.label_mail.place(relx=0.08,rely=0.93)
		def toplevel1(self):
			self.toplevel=Toplevel()
			self.toplevel.title('Sendmail')
			self.toplevel.geometry('700x800')
			self.img=PhotoImage(file="sms.png")
			
			try:
				
				ip = load(urlopen('http://httpbin.org/ip'))['origin']
				self.label_ip=Label(self.toplevel,text='[+]'+' '+ip,fg='green')
				self.label_ip.place(relx=0.18,rely=0.03)
			except URLError, e:	
				time.sleep(5)
				self.label_ip=Label(self.toplevel,text='[-] check you internet',fg='red')
				self.label_ip.place(relx=0.18,rely=0.03)
			
					
			
			
			self.label_youip=Label(self.toplevel,text='IP :',fg='#0606F4')
			self.label_youip.place(relx=0.08,rely=0.03)	
			self.panel=Label(self.toplevel,image=self.img,height=220)
			self.panel.place(relx=0.45,rely=0.02)
			self.label_from=Label(self.toplevel,text='From')
			self.label_from.place(relx=0.08,rely=0.12)
			self.label_to=Label(self.toplevel,text='To')
			self.label_to.place(relx=0.08,rely=0.18)
			self.label_key=Label(self.toplevel,text='Key')
			self.label_key.place(relx=0.08,rely=0.24)
			self.label_text=Label(self.toplevel,text='Text',font='bold')
			self.label_text.place(relx=0.08,rely=0.3)
			self.entry_from=Entry(self.toplevel)
			self.entry_from.place(relx=0.14,rely=0.12)
			self.entry_to=Entry(self.toplevel)
			self.entry_to.place(relx=0.14,rely=0.18)
			self.entry_key=Entry(self.toplevel,show="*")
			self.entry_key.place(relx=0.14,rely=0.24)
			self.text=Text(self.toplevel,width=80,height=13,bg='#3A2C2C')
			self.text.place(relx=0.08,rely=0.36)
			self.button_send=Button(self.toplevel,text='Send',bg='#152D15'\
			,cursor='hand2',width=5,command=self.smtp_live)
			self.button_send.place(rely=0.65,relx=0.09)
			
			self.button_del=Button(self.toplevel,text='clear',width=5,command=self.delete)
			self.button_del.place(relx=0.195,rely=0.65)
			self.button_refr=Button(self.toplevel,text='Refresh'\
			,bg='red',fg='black',cursor='hand2')
			self.button_refr.place(relx=0.3,rely=0.65)
			self.listbox=Listbox(self.toplevel,width=33,height=15,bg='black')
			self.listbox.place(relx=0.5,rely=0.65)
			self.label_contact=Label(self.toplevel,text='Contact mail :',fg='white')
			self.label_contact.place(relx=0.08,rely=0.9)
			self.label_mail=Label(self.toplevel,text='pythonaz@yahoo.com'\
			,fg='#4F4F9E')
			self.label_mail.place(relx=0.08,rely=0.93)
		def toplevel2(self):
			self.toplevel=Toplevel()
			self.toplevel.title('Sendmail')
			self.toplevel.geometry('700x800')
			self.img=PhotoImage(file="sms.png")
			
			try:
				
				ip = load(urlopen('http://httpbin.org/ip'))['origin']
				self.label_ip=Label(self.toplevel,text='[+]'+' '+ip,fg='green')
				self.label_ip.place(relx=0.18,rely=0.03)
			except URLError, e:	
				time.sleep(5)
				self.label_ip=Label(self.toplevel,text='[-] check you internet',fg='red')
				self.label_ip.place(relx=0.18,rely=0.03)
			
					
			
			
			self.label_youip=Label(self.toplevel,text='IP :',fg='#0606F4')
			self.label_youip.place(relx=0.08,rely=0.03)	
			self.panel=Label(self.toplevel,image=self.img,height=220)
			self.panel.place(relx=0.45,rely=0.02)
			self.label_from=Label(self.toplevel,text='From')
			self.label_from.place(relx=0.08,rely=0.12)
			self.label_to=Label(self.toplevel,text='To')
			self.label_to.place(relx=0.08,rely=0.18)
			self.label_key=Label(self.toplevel,text='Key')
			self.label_key.place(relx=0.08,rely=0.24)
			self.label_text=Label(self.toplevel,text='Text',font='bold')
			self.label_text.place(relx=0.08,rely=0.3)
			self.entry_from=Entry(self.toplevel)
			self.entry_from.place(relx=0.14,rely=0.12)
			self.entry_to=Entry(self.toplevel)
			self.entry_to.place(relx=0.14,rely=0.18)
			self.entry_key=Entry(self.toplevel,show="*")
			self.entry_key.place(relx=0.14,rely=0.24)
			self.text=Text(self.toplevel,width=80,height=13,bg='#3A2C2C')
			self.text.place(relx=0.08,rely=0.36)
			self.button_send=Button(self.toplevel,text='Send',bg='#152D15'\
			,cursor='hand2',width=5,command=self.smtp_yahoo)
			self.button_send.place(rely=0.65,relx=0.09)
			
			self.button_del=Button(self.toplevel,text='clear',width=5,command=self.delete)
			self.button_del.place(relx=0.195,rely=0.65)
			self.button_refr=Button(self.toplevel,text='Refresh'\
			,bg='red',fg='black',cursor='hand2')
			self.button_refr.place(relx=0.3,rely=0.65)
			self.listbox=Listbox(self.toplevel,width=33,height=15,bg='black')
			self.listbox.place(relx=0.5,rely=0.65)
			self.label_contact=Label(self.toplevel,text='Contact mail :',fg='white')
			self.label_contact.place(relx=0.08,rely=0.9)
			self.label_mail=Label(self.toplevel,text='pythonaz@yahoo.com'\
			,fg='#4F4F9E')
			self.label_mail.place(relx=0.08,rely=0.93)
		def host(self):
			try:
				
				target=self.entry_host.get()
				targetIP=gethostbyname(target)
				ip = load(urlopen('http://httpbin.org/ip'))['origin']
				self.listbox_host.delete(0,END)
				self.listbox_host.insert(0,'Your IP :'+ip)
				self.listbox_host.insert(0,'Host IP :'+targetIP)
				
				for i in range(20,1025):
					s=socket(AF_INET, SOCK_STREAM)
					result=s.connect_ex((targetIP, i))
					if(result ==0):
						self.listbox_host.insert(0,'Port OPEN')
						self.listbox_host.insert(0,i)
					s.close()
						
			except gaierror:
				self.listbox_host.insert(0,'unknown host name or')
				self.listbox_host.insert(0,'check your connect')
			except URLError, e:
			 	time.sleep(3)
			 	self.listbox_host.delete(0,END)
				self.listbox_host.insert(0,'Please connect to the internet')
				
			
		def gui(self):
			# all label for root gui
			self.label=Label(root,text='-'*195,fg='black')
			self.label.place(relx=0.01,rely=0.03)
			self.label_sosial=Label(root,text='Sosial network',fg='white')
			self.label_sosial.place(relx=0.01,rely=0.08)
			self.label_fb=Label(text='Facebook',cursor='hand2',fg='#4F4F9E')#facebook
			self.label_fb.place(relx=0.01,rely=0.12)
			self.label_fb.bind("<Button-1>",self.call_fb)
			self.label_gt=Label(text='Github',cursor='hand2',fg='#4F4F9E')#twitter
			self.label_gt.place(relx=0.1,rely=0.12)
			self.label_gt.bind("<Button-1>",self.call_gt)
			self.label_op=Label(root,text='Operation system : %s'%platform.system(),\
			fg='#107FEB',font='bold') #operation system
			self.label_op.place(relx=0.64,rely=0.06)
			self.label_time=Label(root,text='Time : %s'%time.ctime(),fg='#107FEB',font='bold')
			self.label_time.place(relx=0.64,rely=0.1)
			self.label_contact=Label(root,text='Contact mail')
			self.label_contact.place(relx=0.3,rely=0.08)
			self.label_mail=Label(root,text='pythonaz@yahoo.com',fg='#4F4F9E')
			self.label_mail.place(relx=0.3,rely=0.12)
			self.label_host=Label(root,text='Host name :')
			self.label_host.place(relx=0.01,rely=0.2)
			self.entry_host=Entry(root,relief=GROOVE,bg='black',fg='white')
			self.entry_host.place(relx=0.1,rely=0.2)
			self.button_host=Button(root,text='start',command=self.host)
			self.button_host.place(relx=0.335,rely=0.2)
			self.listbox_host=Listbox(root,width=40,height=14,bg='black',fg='green')
			self.listbox_host.place(relx=0.535,rely=0.2)
			#button root gui
			self.button_gmail=Button(text='gmail',cursor='hand2',bg='#154E15',width=5,command=self.toplevel)
			self.button_gmail.place(relx=0.01,rely=0.48)
			self.button_live=Button(root,text='hotmail',cursor='hand2',bg='green',command=self.toplevel1)
			self.button_live.place(relx=0.1,rely=0.48)
			self.button_yahoo=Button(root,text='yahoo',cursor='hand2',bg='green',width=5,command=self.toplevel2)
			self.button_yahoo.place(relx=0.2,rely=0.48)
			self.button_quit=Button(root,text='quit',cursor='hand2',bg='red',command=root.destroy,width=5)
			self.button_quit.place(relx=0.29,rely=0.48)

root=Tk()
root.title('Send-Mail')
root.geometry('800x700')
root.tk_setPalette('#121E2A')
termf = Label(root,height=18,width=300)
termf.place(relx=0.01,rely=0.55)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 120x200 -sb &' % wid)

if __name__ == '__main__':
	app=gui()
	root.mainloop()
