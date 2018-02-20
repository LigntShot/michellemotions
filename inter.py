from tkinter import *
from emotions import *

class Face(Tk):
    def __init__(self):
        super(Face, self).__init__()

        self.emotion = Reaction()

        self.label = Label(self)
        self.label.configure(image = self.emotion.face)
        self.label.pack()

        Button(self, text = 'Joy', command = lambda: self.change_emotion(Joy())).pack()
        Button(self, text = 'Horror', command = lambda: self.change_emotion(Horror()) ).pack()
        Button(self, text = 'Serenity', command = lambda: self.change_emotion(Serenity())).pack()
        Button(self, text = 'Delight', command = lambda: self.change_emotion(Delight())).pack()
        Button(self, text = 'Alarm', command = lambda: self.change_emotion(Alarm())).pack()
        Button(self, text = 'Boredom', command = lambda: self.change_emotion(Boredom())).pack()
        Button(self, text = 'Displeasure', command = lambda: self.change_emotion(Displeasure())).pack()
        Button(self, text = 'Disgust', command = lambda: self.change_emotion(Disgust())).pack()
        Button(self, text = 'Fear', command = lambda: self.change_emotion(Fear())).pack()
        Button(self, text = 'Annoyance', command = lambda: self.change_emotion(Annoyance())).pack()
        Button(self, text = 'Spite', command = lambda: self.change_emotion(Spite())).pack()
        Button(self, text = 'Anger', command = lambda: self.change_emotion(Anger())).pack()
        Button(self, text = 'Excitation', command = lambda: self.change_emotion(Excitation())).pack()
        Button(self, text = 'Surprise', command = lambda: self.change_emotion(Surprise())).pack()
        Button(self, text = 'Amazement', command = lambda: self.change_emotion(Amazement())).pack()
        Button(self, text = 'Sorrow', command = lambda: self.change_emotion(Sorrow())).pack()
        Button(self, text = 'Sadness', command = lambda: self.change_emotion(Sadness())).pack()
        Button(self, text = 'Grief', command = lambda: self.change_emotion(Grief())).pack()
        Button(self, text = 'Interest', command = lambda: self.change_emotion(Interest())).pack()
        Button(self, text = 'Expectation', command = lambda: self.change_emotion(Expectation())).pack()
        Button(self, text = 'Alertness', command = lambda: self.change_emotion(Alertness())).pack()
        Button(self, text = 'Adoption', command = lambda: self.change_emotion(Adoption())).pack()
        Button(self, text = 'Trust', command = lambda: self.change_emotion(Trust())).pack()
        Button(self, text = 'Admiration', command = lambda: self.change_emotion(Admiration())).pack()

    def change_emotion(self, emo):
        if self.emotion == emo:
            pass
        else :
            self.label.configure(image = emo.face)
            self.emotion = emo

if __name__ == '__main__':
    face = Face()
    face.mainloop()
