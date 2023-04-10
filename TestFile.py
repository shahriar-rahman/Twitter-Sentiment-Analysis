#QUICK_LINK#1 : https://notevibes.com/
from pynput.keyboard import Key, Controller
import webbrowser;
from time import *;
import os;
import requests;
from textblob import TextBlob;

#os.system("start /wait cmd /c {command}");
import csv;
from playsound import playsound
import datetime;

alphabet = "search excaliburs of space"
formatText="I am not doing alright";

if "search for" in alphabet:
    data=alphabet.split("search for ");
    arr = str(data).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
else :
    data=alphabet.split("search ");
    arr = str(data).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
print(arr);
###############################################################
Polarity = 0;
Analysis = TextBlob(formatText);
Polarity += Analysis.sentiment.polarity;
formatText=formatText.lower();
if "feeling" in formatText or "doing" in formatText:
    print(formatText)
    if "ok" in formatText or "okay" in formatText or "alright" in formatText and "not" in formatText or "don't" in formatText or "do not" in formatText:
        Polarity = -1 * Polarity - 0.2;
        print(Polarity);
    elif "good"in formatText and "not" in formatText or "don't" in formatText or "do not" in formatText:
        Polarity=-1*Polarity*0.75;
        print(Polarity);
    elif "well"in formatText and "not" in formatText or "don't" in formatText or "do not" in formatText:
        Polarity=-1*(0.60)*0.75;
        print(Polarity);
    elif "great"in formatText and "not" in formatText or "don't" in formatText or "do not" in formatText:
        Polarity=-1*Polarity*0.5;
        print(Polarity);
    elif "awesome"in formatText and "not" in formatText or "don't" in formatText or "do not" in formatText:
        Polarity=-1*Polarity*0.25;
        print(Polarity);
    elif Polarity>0:
        print(Polarity);
    # POSITIVE FIXES/ADDONS
    elif "well" in formatText:
        Polarity = 0.60;
        print(Polarity);
        #EOL
    elif Polarity<0:
        print(Polarity);
    #NEGATIVE FIXES/ADDONS
    elif "dislike" in formatText or "disliked" in formatText:
        Polarity = -0.60; print(Polarity);
    elif "depressed" in formatText or "depression" in formatText or "very depressed" in formatText or "huge depression" in formatText:
        Polarity = -0.80; print(Polarity);
        # EOL
    #STORE SENTIMENT VALUE
    CurrentSession = open('December/Memory/CurrentSession.txt', 'w');
    OverallSession = open('December/Memory/OverallSession.txt', 'a');
    CurrentSession.write("polarity,value"+"\n");
    CurrentSession.write(str(Polarity)); CurrentSession.write(",");CurrentSession.write(formatText);CurrentSession.write("\n")
    OverallSession.write(str(Polarity));OverallSession.write(",");OverallSession.write(formatText);OverallSession.write("\n");
    CurrentSession.close();OverallSession.close();
    #RESPONSE
    if Polarity==0:
        playsound("December/Voice/Feel0.mp3" );
    elif Polarity>0 and Polarity <=0.80:
        playsound("December/Voice/Feel+1.mp3");
    elif Polarity > 0.80 and Polarity <= 2:
        playsound("December/Voice/Feel+2.mp3");
    elif Polarity<0:
        FileType = "Feel-";
        FileExtension = ".mp3"
        from random import randint; number = str(randint(1, 4));
        playsound("December/Voice/"+FileType+number+FileExtension);
    #if







