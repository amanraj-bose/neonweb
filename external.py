import keyboard
import time
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 177)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def press(buttons):
    keyboard.press_and_release(buttons)
def write(letter):
    keyboard.write(letter)
def zz(sleep):
    time.sleep(sleep)

press('windows + s')
zz(1)
write('folder: GitHub')
zz(1)
press('enter')
zz(1)
def down():
    press( "down" )
    zz( 1 )
    press( 'down' )
    zz( 1 )
    press( "down" )
    zz( 1 )
    press( 'down' )
    zz( 1 )
    press( 'down' )
    zz( 1 )
    press( 'enter' )
    zz( 1 )
    try:
        None
    except Exception as e:
        print(e)
if __name__ == '__main__':
    down()
press('down')
zz(1)
press('up')
zz(1)
press('enter')
zz(1)
press('f11')
zz(3)
with open(r'C:\Users\AMAN\Documents\GitHub\MontiSWebsitew\index.html') as f:
    sound = speak(f.read())
    zz(1)
    press('alt + f4')
