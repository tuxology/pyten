#!/usr/bin/env python

# PyTen - Python Task Evaluaton
#--------------------------------------------------------------------------------
#
# Copyright (C) 2010 Suchakra <suchakra@fedoraproject.org> , <suchakra@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
#---------------------------------------------------------------------------------
#
# Known Issues : Many :-(
#

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import string
import sys
import datetime

now = datetime.datetime.now()

class PyTen(object):

	def on_window_main_destroy(self, widget, data=None):
		gtk.main_quit()

	def __init__(self):
		builder = gtk.Builder()
		builder.add_from_file("PyTen.glade")
		self.window_main = builder.get_object("window_main")
		builder.connect_signals(self)
		self.dialog_checkin = builder.get_object("dialog_checkin")
		self.dialog_checkout = builder.get_object("dialog_checkout")
		self.dialog_about = builder.get_object("dialog_about")
        	self.fileviewer = builder.get_object("fileviewer")
        	self.textview = builder.get_object("textview1")
        	self.buffer = builder.get_object("textbuffer1")
        	self.checkin_label = builder.get_object("checkin_label")
	       	self.checkout_label = builder.get_object("checkout_label")
	       	self.entry1 = builder.get_object("entry1")
	       	self.entry2 = builder.get_object("entry2")
	       	self.entry3 = builder.get_object("entry3")
	       	self.entry4 = builder.get_object("entry4")
	       	self.entry5 = builder.get_object("entry5")
	       	self.entry6 = builder.get_object("entry6")

# Show Check-In dialog. Open "tasks.txt" in 'w' mode and write Check-In entry.

	def on_checkin_clicked(self, widget):
		self.dialog_checkin.show()
		self.checkin_label.set_text(now.strftime("Checked In : %Y-%m-%d %H:%M"))
		f = open("tasks.txt" , 'w')
		f.write("\n------------------------------------------------------\n")
		f.write(now.strftime("Checked In	: %H:%M on %d-%m-%Y"))
		f.write("\n------------------------------------------------------\n")
		f.close()

# Show Check-Out dialog. Open "tasks.txt" in 'a' mode and append Check-Out entry.

	def on_checkout_clicked(self, widget):
		self.dialog_checkout.show()
		self.checkout_label.set_text(now.strftime("Checked Out : %Y-%m-%d %H:%M"))
		f = open("tasks.txt" , 'a')
		f.write("\n------------------------------------------------------\n")
		f.write(now.strftime("Checked Out	: %H:%M on %d-%m-%Y"))
		f.write("\n------------------------------------------------------\n")
		f.close()


# Closing Check-in and Check-out dialog when "Ok" clicked
		
	def on_ok2_clicked(self, widget):
		self.dialog_checkout.destroy()

	def on_ok1_clicked(self, widget):
		self.dialog_checkin.destroy()
		
# Show "tasks.txt" file when "View Report" is clicked. Text send to 'buffer' first.

	def on_viewfile_clicked(self, widget):
		self.fileviewer.show()
		f = open("tasks.txt" , 'r')
		txt = f.read()
		self.buffer.set_text(txt)
		f.close()

# Show "About" dialog

	def on_about_clicked(self, wiget):
		self.dialog_about.show()

	def on_dialog_about_close(self, wiget):
		self.dialog_about.destroy()

# Checking if each tick is clicked. Append the task name, task number, time of completion 
# for each task tick clicked to the tasks.txt file 

	def on_tick1_clicked(self, wiget):
		txt = self.entry1.get_text()
		f = open("tasks.txt" , 'a')
		f.write("1.	") 
		f.write(txt)
		f.write(now.strftime("	:	%H:%M\n"))
		f.close()

	def on_tick2_clicked(self, wiget):
		txt = self.entry2.get_text()
		f = open("tasks.txt" , 'a')
		f.write("2. 	") 
		f.write(txt)
		f.write(now.strftime("	:	%H:%M\n"))
		f.close()

	def on_tick3_clicked(self, wiget):
		txt = self.entry3.get_text()
		f = open("tasks.txt" , 'a')
		f.write("3. 	") 
		f.write(txt)
		f.write(now.strftime("	:	%H:%M\n"))
		f.close()
	
if __name__ == "__main__":
	app = PyTen()
	app.window_main.show()
	gtk.main()



