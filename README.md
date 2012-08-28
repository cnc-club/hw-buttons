HW-buttons is  GgladeVCP panel that realises hardware buttons 
connected to defined places on the screen. 

It should work similar to the buttons that are used in commercial
cnc pedants like fanuc or siemens.

For more info see: http://cnc-club.ru/forum/viewtopic.php?f=15&t=2047&p=35455#p35417 (Russian language)

To test you can run the following having already started LinuxCNC. 

gladevcp  -u hw-buttons.py   -H hw-buttons.hal   hw-buttons.ui
