import datetime
import locale

 
try:
    locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')
except locale.Error:
    locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')

an = datetime.datetime.now()

print(an.strftime('%Y'))      
print(an.strftime('%X'))   
print(an.strftime('%A'))         
print(an.strftime('%B'))               
print(an.strftime('%d %B %Y'))       
print(an.strftime('%d.%m.%Y tarihinde buluşalım.'))