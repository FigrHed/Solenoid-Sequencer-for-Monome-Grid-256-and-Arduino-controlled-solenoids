from tkinter import *


class StepSequencerGUI:
    def __init__(self, tempo=90, noteLength=0.075):
        #declare tools
        self.window = Tk()
        self.window.geometry("400x300")
        self.tempo = DoubleVar()
        self.noteLength = DoubleVar()
        #initialize elements
        #tempo elements
        self.tempo.set(tempo)
        self.tempoSlider = Scale( self.window, variable = self.tempo, from_ = 30, to = 250, orient = HORIZONTAL, command = self.showTempo, width=25, length=200, showvalue=0, resolution=0.1)
        self.tempoLabel = Label(self.window, text = "Tempo")
        
        self.tempoDisplay = Label(self.window)
        #notelength elements
        self.noteLength.set(noteLength)
        self.noteLengthSlider = Scale (self.window, variable = self.noteLength, from_ = 0.01, to = 0.5, orient = HORIZONTAL, command = self.showNoteLength, width=25, length=200, showvalue=0, resolution=0.001)
        self.noteLengthLabel = Label(self.window, text = "Note Length")
        self.noteLengthDisplay = Label(self.window)

        

        #pack, make visible
        self.tempoSlider.pack(anchor = CENTER)
        self.tempoLabel.pack()
        # self.displayTempoButton.pack()
        self.tempoDisplay.pack()
        self.noteLengthSlider.pack(anchor = CENTER)
        self.noteLengthLabel.pack()
        # self.displayNoteLengthButton.pack()
        self.noteLengthDisplay.pack()

        #start
        # self.window.mainloop()


    def showTempo(self,tempoVal):
        sel = "Tempo: " + str(self.tempo.get())
        self.tempoDisplay.config(text=sel, font = ("Courier", 14))
        

    def showNoteLength(self,noteLengthVal):
        sel = "Note Length: " + str(self.noteLength.get())
        self.noteLengthDisplay.config(text=sel, font = ("Courier", 14))



#noteLengthSlider = Scale(window, variable = noteLength, )

# def printTempo():
#     print(stepGUI.tempo)

if __name__ == "__main__":
    stepGUI = StepSequencerGUI()

    # otherWindow = Tk()
    # btn = Button(otherWindow,Text="push the tempo",  bg="black", fg="white")#command=print(stepGUI.tempo),
    # btn.pack()
    # otherWindow.mainloop()




    