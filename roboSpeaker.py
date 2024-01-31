import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker Created by Esha Chauhan.")

    engine=pyttsx3.init()

    while True:
        x=input("Enter what you want me to speak: ")
        if x.lower() == "quit":
            engine.say("Say 'bye bye Friend'")
            engine.runAndWait()
            break
        else:
            engine.say(x)
            engine.runAndWait()
