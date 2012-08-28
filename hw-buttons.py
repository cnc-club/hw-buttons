#!/usr/bin/env python
  # -*- coding: utf-8 -*-
# Задаем кол-во кнопок v - вертикальные, h - горизонтальные
vbuttons_num = 7
hbuttons_num = 7

import hal_glib, hal


class HWButtons:

	def __init__(self, halcomp, builder, useropts):
		# __init__ вызывается при создании объекта класса 
		
		# сохраняем параметры в теле объекта, т.к. будем использовать их в будущем.
		self.builder = builder
		self.comp = halcomp
		self.useropts = useropts
		
		# вычисляем ссылки на notepad содержащие кнопки
		self.vbuttons = self.builder.get_object("vbuttons")
		self.hbuttons = self.builder.get_object("hbuttons")
		
		# в этих массивах буду тхранится ссылки на пины vbutton.XX и hbutton.XX 
		self.vtriggers = []
		self.htriggers = []
		
		# заполняем массивы
		for i in range(vbuttons_num) :
			# создаем пин и добавляем его в массив
			self.vtriggers.append(hal_glib.GPin(halcomp.newpin('vbutton.%s'%i, hal.HAL_BIT, hal.HAL_IN)))
			# присоединяем сигнал на изменение значения к пину, функция обработки - click_button, с 
			# параметрами notebook в котором кнопка и номер кнопки 
			self.vtriggers[-1].connect("value-changed",self.click_button, self.vbuttons, i)
			
		# тоже самое со вторым массивом	
		for i in range(hbuttons_num) :
			self.htriggers.append(hal_glib.GPin(halcomp.newpin('hbutton.%s'%i, hal.HAL_BIT, hal.HAL_IN)))
			self.htriggers[-1].connect("value-changed",self.click_button, self.hbuttons, i)
		
		
	def click_button(self, pin, notebook, num) :
		# Функция нажать на кнопку
		# Параметры
		# pin - вызывающий пин
		# notebook - notebook содержащий кнопку
		# num - номер кнопки
		
		# если значение пина стало 1
		if pin.value == True :
			# берем Box от странницы notebook с номером = активной странице
			box = notebook.get_nth_page(notebook.get_current_page())
			
			# берем список кнопок в Box в странице
			button_list = box.get_children()
			
			# если номер запрашиваемой кнопки попадает в длинну списка
			if 0<=num<len(button_list) :
				# назначаем переменную кнопки 
				button = button_list[num]
			else :
				# иначе выводим ошибку
				self.error("Button list range error on num = %s"%num)
				return
				
			# Генерируем сигнал нажатия на кнопку, после этого сработает обработчик кнопки	
			button.emit("clicked")


	def set_hal_pin(self, obj, pin, value) :
		# эта функция задумывалась для простой установки пинов в нужные значения, 
		# т.е. ее можно использовать в connect, например:
		# button.connect("clicked",set_hal_pin, "home-z",1) 
		if pin in self.comp :
			self.comp[pin] = value
		else :
			self.error("There's no such pin in the comp '%s'!"%pin)
			
	def error(self, s) :
		# функция реакции на ошибки - просто выводим в еконсоль информацию
		print "HWButtons Error: %s"%s


def get_handlers(halcomp,builder,useropts):
	# эта функция вызывается GladeVCP после создания формы, в качестве параметров передаются 
	# компонент hal, builder - ссылка на структуру UI, и пользовательские параметры. 
	
	# после получения всех этих параметров создаем объект нашего класса
	hwbuttons = HWButtons(halcomp,builder,useropts)	
	
	return []

