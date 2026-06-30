import webbrowser
import datetime


def greet():
    return "Hello Sumit, how are you?"


def introduce():
    return "Hello, I am your personal assistant Jarvis!"


def goodbye():
    return "Goodbye Sumit!"


def opengoogle():
    webbrowser.open("https://google.com")
    return "Opening Google!"


def openyoutube():
    webbrowser.open("https://youtube.com")
    return "Opening YouTube!"


def opengithub():
    webbrowser.open("https://github.com")
    return "Opening GitHub!"


def telltime():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    return f"The current time is {current_time}"


def telldate():
    today = datetime.datetime.now()
    date = today.strftime("%d %B %Y")
    return f"Today's date is {date}"


def tellday():
    today = datetime.datetime.now()
    day = today.strftime("%A")
    return f"Today is {day}"