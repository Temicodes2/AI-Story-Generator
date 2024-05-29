import pyttsx4

# initialisation
engine = pyttsx4.init()
import Setup

# finish imports
airesponse = ""
# airesponse ^
while airesponse == "":
    apikey = input(
        "YOUR GOOGLE API KEY FROM HERE: (https://aistudio.google.com/app/) (YOU MUST HAVE A GOOGLE API KEY TO USE THIS PROJECT): ")
    Setup.genai.configure(api_key=apikey)
    yourresponse = input(
        "your story topic: ") + "(Make a scene/story about this topic, put what the topic is before the story)"
    voice = input("Do you want an AI voice to say out the story for you? y/n")

    message = Setup.convo.send_message(yourresponse)
    airesponse = Setup.convo.last.text
    print(airesponse)
    if voice == "y":
        engine.say(airesponse)
        engine.runAndWait()
    else:
        pass
# ai generation
