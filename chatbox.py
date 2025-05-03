     
import os
import time
import subprocess
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour

    if hour < 12:
        print("Good Morning Sir")
        speak("Good Morning Sir")
    elif 12 <= hour <= 16:
        print("Good Afternoon Sir")
        speak("Good Afternoon Sir")
    else:
        print("Good Evening Sir")
        speak("Good Evening Sir")

def date_time():
    current_time = time.localtime()
    print("The date and time is ")
    print(time.strftime("%Y-%m-%d %H:%M:%S", current_time))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\t\t\t<============================================= W E L C O M E ==========================================>")
    print("\t\t\t<============================================= I'M A STUDENT ==========================================>")
    print("\t\t\t<============================================= MY NAME IS Geetanjali ==========================================>")
    print("\t\t\t<============================================= I'M HERE TO HELP YOU ==========================================>\n")

    password = ""
    command = ""

    while True:
        print("=======================")
        print("| ENTER YOUR PASSWORD |")
        print("=======================\n")
        speak("Enter your password")

        password = input()

        if password == "Apple@123":
            print("\n<==================================================================================================>\n\n")
            wish_me()
            while True:
                print("\n<==================================================================================================>\n\n")
                print("How can I help you sir....\n")
                speak("How can I help you sir")

                command = input("Your query ===> ")
                print("\nHere is the result for your query ===> ")

                if command in ["hi", "hey", "hello"]:
                    print("Hello sir.....")
                    speak("Hello sir")
                elif command in ["bye", "stop", "exit"]:
                    print("Good Bye sir, have a nice day!!!!")
                    speak("Good Bye sir, have a nice day")
                    exit(0)
                elif command in ["who are you", "tell me about yourself", "about"]:
                    print("I'm a virtual assistant created by Geetanjali !!!")
                    speak("I am a virtual assistant created by Geetanjali")
                elif command in ["how are you", "whatsup", "how is your day"]:
                    print("I'm good sir, tell me how can I help you..")
                    speak("I'm good sir, tell me how can I help you")
                elif command in ["time", "date"]:
                    date_time()
                elif command == "open notepad":
                    print("Opening notepad.....")
                    speak("Opening notepad")
                    subprocess.Popen(['notepad.exe'])
                elif command == "open google":
                    print("Opening Google.....")
                    speak("Opening Google")
                    os.system("start https://www.google.com")
                elif command == "open youtube":
                    print("Opening YouTube.....")
                    speak("Opening YouTube")
                    os.system("start https://www.youtube.com")
                elif command == "open instagram":
                    print("Opening Instagram.....")
                    speak("Opening Instagram")
                    os.system("start https://www.instagram.com")
                else:
                    print("Sorry, could not understand your query. Please try again.")
                    speak("Sorry, could not understand your query. Please try again.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\t\t\t<============================= W E L C O M E=============================>")
            print("\t\t\t<============================= I'M A STUDENT =============================>")
            print("\t\t\t<============================= MY NAME IS GEETANJALI =============================>")
            print("\t\t\t<============================= I'M HERE TO HELP YOU AND MAKE YOUR LIFE EASY =============================>\n")
            print("======================")
            print("X Incorrect Password X")
            print("======================\n")
            speak("Incorrect Password, Please enter correct password")

if __name__ == "__main__":
    main()
