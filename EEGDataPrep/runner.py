from tkinter import *
from front.front import MyWindow
#build the front, always start from the front


window = Tk() #open a new window
MyWin= MyWindow(window)
window.title('Brainput') #תכונה של החלון- לקבוע את השם שלו
window.geometry("680x350")  #קובע גודל

window.mainloop() #דואג לתקשורת בין הקובץ הנוכחי לחלון שלי