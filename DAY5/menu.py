import os
import pyttsx3
from espeakng import ESpeakNG
os.system("tput setaf 1")
print("\t\t\t Welcome to the Linux World")
os.system("tput setaf 7")
print("\t\t\t--------------------")
while True:
    
    print("""\t\t\t
         \t\t\ttype 1 to see date
         \t\t\ttype 2 to see calendar
        \t\t\ttype 3 to see time
        \t\t\ttype 4 to see calendar of next month
        \t\t\ttype 5 to open GVIM
        \t\t\ttype 6 to open firefox
        \t\t\ttype 7 to create a file
        \t\t\ttype 8 to make it speak whatever you want
        """
        )
    esng = ESpeakNG()
    esng.voice = 'en-us'
    esng.speed = 170
    esng.pitch = 200
    text = 'Choose your option'
    esng.say(text)

    x = int(input(""))
    if x == 1:
        os.system("date")
    elif x == 2: 
        os.system("cal")
    elif x == 3:
        os.system("date +%T")
    elif x == 4:
        os.system("cal 7 2023")
    elif x==5:
        os.system("gvim")
    elif x==6:
        os.system("firefox")
    elif x==7:
        x=input("enter the name of the file")
        os.system("touch "+x)
    elif x==8:
        x=input("What do you want it to say?")
        esng.say(x)
    else:
        print("INVALID")

    y = int(input("""
                1 - exit 
                0 - continue 
            """
              ))
    if y == 1:
        y="Thanks for using our app"
        esng.say(y)
        break

    else:
        os.system("clear")
        continue