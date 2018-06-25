import time
import sys
import webbrowser
yes = "yes"
no = "no"
sad = "sad"
good = "good"
great = "great"
anxious = "anxious"
print("Howdy!")
time.sleep(2)
user = input("What should I call you? ")
print("I see! Nice to meet you,",user)
mood = input("How are you today? Possible answers: good, sad, great, anxious ")
if sad in mood:
    print("Sorry to hear that,",user,". Try and find something to make you happy, I promise it\'ll help. Maybe a hobby or a game?")
    print("As Kareena Kapoor Khan once said, \"Life is full of happiness and tears; be strong and have faith.\"")
    uplift = input("Would you like to hear an uplifting song? (yes/no)")
    if yes in uplift:
        print("Okay! Opening song now. Turn the volume up! Enjoy. This has been Emotions by Dafydd.")
        time.sleep(3)
        webbrowser.open('https://www.youtube.com/watch?v=C9iDBkJqxNg')
        time.sleep('3')
        print("Closing in 5 seconds.")
        time.sleep(5)
        sys.exit()
    if no in uplift:
        print('No worries! See you next time. Emotions by Dafydd')
        time.sleep('3')
        print("Closing in 5 seconds.")
        time.sleep(5)
        sys.exit()
if good in mood:
    print("Great to hear! :) Keep that up. A happier person is a better person! As Maharism Mahesh Yogi once said, \"Happiness radiates like the fragrance from a flower and draws all good things towards you.\"")
    print(":D")
    happy = input("Would you like to listen to a happy song? (yes/no)")
    if yes in happy:
        print("Okay! Opening song now. Turn the volume up! Enjoy. This has been Emotions by Dafydd.")
        time.sleep(3)
        webbrowser.open('https://www.youtube.com/watch?v=MOWDb2TBYDg')
        time.sleep('3')
        print("Closing in 5 seconds.")
        time.sleep(5)
        sys.exit()
    if no in happy:
        print('No worries! See you next time. Emotions by Dafydd')
        time.sleep(3)
        print("Closing in 5 seconds.")
        time.sleep(5)
        sys.exit()
if great in mood:
    print("FANTASTIC! As Omar Khayyam once said: \"Be happy for this moment. This moment is your life.\" ")
    happy = input("Would you like to listen to a happy song? (yes/no)")
    if yes in happy:
        print("Okay! Opening song now. Turn the volume up! Enjoy. This has been Emotions by Dafydd.")
        time.sleep(3)
        webbrowser.open('https://www.youtube.com/watch?v=MOWDb2TBYDg')
        time.sleep(3)
        print("Closing in 5 seconds.")
        time.sleep(5)
        sys.exit()
    if no in happy:
        print('No worries! See you next time. Emotions by Dafydd')
        time.sleep('3')
        print("Closing in 5 seconds.")
        time.sleep(5)
        sys.exit()
if anxious in mood:
    print("Sorry you\'re anxious. Try stimulatory activiies, your favourite songs or something to distract you.")
    print("Charles Spurgeon once said: \"Anxiety does not empty tomorrow of its sorrows, but only empties today of its strength.\"")
    anxs = input("Would you like to listen to a calm song? (yes/no)")
    if yes in anxs:
        print("Okay! Opening song now. Turn the volume up! Enjoy. This has been Emotions by Dafydd.")
        time.sleep(3)
        webbrowser.open('https://www.youtube.com/watch?v=mGQFZxIuURE')
        print("Closing in 5 seconds.")
        time.sleep(5)
        sys.exit()
    if no in anxs:
        print('No worries! See you next time. Emotions by Dafydd')
        time.sleep('3')
        print("Closing in 5 seconds.")
        time.sleep(5)
        sys.exit()
if mood is not sad or happy or great or good:
    print("Sorry, I don\'t understand",mood,". Ask Daf to add me! Restarting in 5 seconds.")
    time.sleep(5)
    mood = input("How are you today? Possible answers: good, sad, great, anxious ")
    if sad in mood:
        print("Sorry to hear that,",user,". Try and find something to make you happy, I promise it\'ll help. Maybe a hobby or a game?")
        print("As Kareena Kapoor Khan once said, \"Life is full of happiness and tears; be strong and have faith.\"")
    if good in mood:
        print("Great to hear! :) Keep that up. A happier person is a better person!")
        print(":D")
    if great in mood:
        print("FANTASTIC! As Omar Khayyam once said: \"Be happy for this moment. This moment is your life.\" ")
    if anxious in mood:
        print("Sorry you\'re anxious. Try stimulatory activiies, your favourite songs or something to distract you.")
        print("Charles Spurgeon once said: \"Anxiety does not empty tomorrow of its sorrows, but only empties today of its strength.\"")
