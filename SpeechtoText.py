import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please talk.")
    audio_text = r.listen(source)
    print("Time is up, thanks.") 
    try:
        print("Text: "+r.recognize_google(audio_text))
    except:
        print("Sorry, I did not get that.")