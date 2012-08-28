#!/usr/bin/env python 
vbuttons_num = 7
hbuttons_num = 7

import hal_glib, hal


class HWButtons:
	def __init__(self, halcomp, builder, useropts):
		self.builder = builder
		self.comp = halcomp
		self.useropts = useropts
		self.vbuttons = self.builder.get_object("vbuttons")
		self.hbuttons = self.builder.get_object("hbuttons")
		
		self.vtriggers = []
		self.htriggers = []
		
		for i in range(vbuttons_num) :
			self.vtriggers.append(hal_glib.GPin(halcomp.newpin('vbutton.%s'%i, hal.HAL_BIT, hal.HAL_IN)))
			self.vtriggers[-1].connect("value-changed",self.click_button, self.vbuttons, i)
		for i in range(hbuttons_num) :
			self.htriggers.append(hal_glib.GPin(halcomp.newpin('hbutton.%s'%i, hal.HAL_BIT, hal.HAL_IN)))
			self.htriggers[-1].connect("value-changed",self.click_button, self.hbuttons, i)
		
	def click_button(self, obj, notebook, num) :
		box = notebook.get_nth_page(notebook.get_current_page())
		button_list = box.get_children()
		if 0<=num<len(button_list) :
			button = button_list[num]
		else :
			self.error("Button list range error on num = %s"%num)
			return
		button.emit("clicked")

	def set_hal_pin(self, obj, pin, value) :
		if pin in self.comp :
			self.comp[pin] = value
		else :
			self.error("There's no such pin in the comp '%s'!"%pin)
			
	def error(self, s) :
		print "HWButtons Error: %s"%s


def get_handlers(halcomp,builder,useropts):
	hwbuttons = HWButtons(halcomp,builder,useropts)	
	
	return []

	



    

