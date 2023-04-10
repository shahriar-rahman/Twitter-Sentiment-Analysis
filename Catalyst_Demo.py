from tkinter import *
import random
import tkinter;
import csv;

class Catalyst_Demo :

    def __init__(self):
        print("hello");

    def type(self):
        print("yay")


    def WelcomeScreen(self):
        self.WindowWelcome = tkinter.Tk();
        self.WindowWelcome.title("Reminder Menu");
        self.WindowWelcome.geometry("1920x1080");
        self.WindowWelcome.state('zoomed');
        photoImages = tkinter.PhotoImage(file="December/BG/#5.png", master=self.WindowWelcome);
        BgImages = tkinter.Label(self.WindowWelcome, image=photoImages);
        self.TextReminder = tkinter.StringVar();
        self.TextHour = tkinter.StringVar();
        self.TextMin = tkinter.StringVar();
        self.TextFormat = tkinter.StringVar();
        self.Reminder = tkinter.Entry(self.WindowWelcome, textvariable=self.TextReminder, bg="white", fg="#050529",
                                 font=("Agency FB bold", 30), width="5");
        self.Reminder.place(relx="0.3", rely="0.5");
        self.Hour = tkinter.Entry(self.WindowWelcome, textvariable=self.TextHour, bg="white", fg="#050529",
                             font=("Agency FB bold", 30), width="5");
        self.Hour.place(relx="0.4", rely="0.5");
        self.Min = tkinter.Entry(self.WindowWelcome, textvariable=self.TextMin, bg="white", fg="#050529",
                            font=("Agency FB bold", 30), width="5");
        self.Min.place(relx="0.5", rely="0.5");
        self.Format = tkinter.Entry(self.WindowWelcome, textvariable=self.TextFormat, bg="white", fg="#050529",
                               font=("Agency FB bold", 30), width="5");
        self.Format.place(relx="0.6", rely="0.5");
        self.SaveButton = tkinter.Button(self.WindowWelcome, width="16", text="Save", bg="dark red", fg="white",
                                    font=("Agency FB bold", 22), command=self.SaveDetails);
        self.SaveButton.place(relx="0.475", rely="0.70");
        BgImages.pack();
        self.WindowWelcome.mainloop();

    def SaveDetails(self):
        TextReminder = self.TextReminder.get();
        TextHour=self.TextHour.get();
        TextMin = self.TextMin.get();
        TextFormat=self.TextFormat.get();
        #print(TextFormat);
        ReminderFileSave = open("December/Memory/Reminders/ShortReminder.txt", "w");
        ReminderFileSave.write("reminder,Hour,Min,Format");
        ReminderFileSave.write("\n");
        ReminderFileSave.write(TextReminder+","+TextHour+","+TextMin+","+TextFormat);
        ReminderFileSave.close();

    def showMoodResults(self):
        CombinedText = "";
        self.WindowWelcome = tkinter.Tk();
        self.WindowWelcome.title("Mental Status Results");
        self.WindowWelcome.geometry("1920x1080");
        self.WindowWelcome.state('zoomed');
        photoImages = tkinter.PhotoImage(file="December/BG/#5.png", master=self.WindowWelcome);
        BgImages = tkinter.Label(self.WindowWelcome, image=photoImages);
        with open('December/Memory/CurrentSession.txt', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file);
            i = 0;
            for row in csv_reader:
                i = i + 1;
                polarity = row["polarity"];
                value = row["value"];
                newLine = "\n";
                Text = "Mood Results at try " + str(i) + " : ";
                CombinedText = CombinedText+Text + value + " : " + polarity + newLine;
                #CombinedText=CombinedText+polarity+value;
        LabelSentencePolarity = tkinter.Label(self.WindowWelcome, text=CombinedText, bg="BLACK",
                                              fg="dark red", font=("Agency FB bold", 28), width="50", height="15")
        LabelSentencePolarity.place(relx="0.25", rely="0.05");
        BgImages.pack();
        print(CombinedText)
        self.WindowWelcome.mainloop();

CatObj = Catalyst_Demo();
CatObj.showMoodResults();




