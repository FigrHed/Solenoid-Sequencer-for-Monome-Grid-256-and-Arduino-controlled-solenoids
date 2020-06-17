from tkinter import *


class StepSequencerGUI:
    def __init__(self, tempo=90, note_length=0.075, velocity=100):
        #declare tools
        self.window = Tk()
        self.window.geometry("400x300")
        self.tempo = DoubleVar()
        self.note_length = DoubleVar()
        self.velocity = DoubleVar()
        #initialize elements
        #tempo elements
        self.tempo.set(tempo)
        self.tempoSlider = Scale( self.window, variable = self.tempo, from_ = 30, to = 250, orient = HORIZONTAL, command = self.showTempo, width=25, length=200, showvalue=0, resolution=0.1)
        self.tempoLabel = Label(self.window, text = "Tempo")
        self.tempoDisplay = Label(self.window)
        
        #notelength elements
        self.note_length.set(note_length)
        self.noteLengthSlider = Scale (self.window, variable = self.note_length, from_ = 0.01, to = 0.5, orient = HORIZONTAL, command = self.showNoteLength, width=25, length=200, showvalue=0, resolution=0.001)
        self.noteLengthLabel = Label(self.window, text = "Note Length")
        self.noteLengthDisplay = Label(self.window)
        
        #velocity elements
        self.velocity.set(velocity)
        self.velocity_slider = Scale (self.window, variable = self.velocity, from_ = 0, to = 127, orient = HORIZONTAL, command = self.show_velocity, width=25, length=200, showvalue=0, resolution=1)
        self.velocity_label = Label(self.window, text = "Velocity")
        self.velocity_display = Label(self.window)
        

        #pack, make visible
        self.tempoSlider.pack(anchor = CENTER)
        self.tempoLabel.pack()
        self.tempoDisplay.pack()
        
        self.noteLengthSlider.pack(anchor = CENTER)
        self.noteLengthLabel.pack()
        self.noteLengthDisplay.pack()
        
        self.velocity_slider.pack(anchor = CENTER)
        self.velocity_label.pack()
        self.velocity_display.pack()

        #start
        # self.window.mainloop()


    def showTempo(self,tempoVal):
        sel = "Tempo: " + str(self.tempo.get())
        self.tempoDisplay.config(text=sel, font = ("Courier", 14))
        

    def showNoteLength(self,noteLengthVal):
        sel = "Note Length: " + str(self.note_length.get())
        self.noteLengthDisplay.config(text=sel, font = ("Courier", 14))

    def show_velocity(self,velocity):
        sel = "Velocity: " + str(self.velocity.get())
        self.velocity_display.config(text=sel, font = ("Courier", 14))
    
    def get_tempo(self):
        return self.tempo.get()
    
    def set_tempo(self, newTempo):
         self.tempo.set(newTempo)

    def get_note_length(self):
        return self.note_length.get()

    def set_note_length(self, new_note_length):
        self.note_length.set(new_note_length)

    def get_velocity(self):
        return self.velocity.get()

    def set_velocity(self, new_velocity):
        self.velocity.set(velocity)

    def get_all_values(self):
        return((self.tempo, self.note_length, self.velocity))


#noteLengthSlider = Scale(window, variable = note_length, )

# def printTempo():
#     print(stepGUI.tempo)

if __name__ == "__main__":
    stepGUI = StepSequencerGUI()

    # otherWindow = Tk()
    # btn = Button(otherWindow,Text="push the tempo",  bg="black", fg="white")#command=print(stepGUI.tempo),
    # btn.pack()
    # otherWindow.mainloop()




    