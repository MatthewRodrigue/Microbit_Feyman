from microbit import *
import random

while True:
   if button_a.is_pressed():
       temperatura=random.randint(-10,100)
       display.scroll(str(temperatura))
       if temperatura >90:
           display.scroll("HOT!")
           display.show(Image.HEART)  
       elif temperatura >75:
           display.show(Image.HEART)
       elif temperatura < 0:
           display.show(Image.SAD)
       elif temperatura <30:
           display.scroll("MEH!")
       else:
           display.clear()
   if button_b.is_pressed():
       display.off()