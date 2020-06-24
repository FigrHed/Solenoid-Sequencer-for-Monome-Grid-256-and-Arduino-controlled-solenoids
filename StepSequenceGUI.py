from tkinter import *
from SolenoidSequencer import *



class StepSequencerGUI:
    def __init__(self, model):
        #declare tools
        self.window = Tk()
        self.window.geometry("400x300")
        self.model = model


        #the native parameters
        self.gui_tempo = DoubleVar()
        self.gui_note_length = DoubleVar()
        self.gui_velocity = DoubleVar()
        #initialize elements
        #gui_tempo elements
        self.gui_tempo.set(self.model.tempo)
        self.gui_tempo_slider = Scale( self.window, variable = self.gui_tempo, from_ = 30, to = 250, orient = HORIZONTAL, command = self.showgui_Tempo, width=25, length=200, showvalue=0, resolution=0.1)
        self.gui_tempo_label = Label(self.window, text = "Tempo")
        self.gui_tempo_display = Label(self.window)
        
        #gui_note_length_ elements
        self.gui_note_length.set(self.model.note_length)
        self.gui_note_length_slider = Scale (self.window, variable = self.gui_note_length, from_ = 0.01, to = 0.5, orient = HORIZONTAL, command = self.showgui_note_length_, width=25, length=200, showvalue=0, resolution=0.001)
        self.gui_note_length_label = Label(self.window, text = "Note Length")
        self.gui_note_length_display = Label(self.window)
        
        #gui_velocity elements
        self.gui_velocity.set(self.model.velocity)
        self.gui_velocity_slider = Scale (self.window, variable = self.gui_velocity, from_ = 0, to = 127, orient = HORIZONTAL, command = self.show_gui_velocity, width=25, length=200, showvalue=0, resolution=1)
        self.gui_velocity_label = Label(self.window, text = "Velocity")
        self.gui_velocity_display = Label(self.window)
        

        #pack, make visible
        self.gui_tempo_slider.pack(anchor = CENTER)
        self.gui_tempo_label.pack()
        self.gui_tempo_display.pack()
        
        self.gui_note_length_slider.pack(anchor = CENTER)
        self.gui_note_length_label.pack()
        self.gui_note_length_display.pack()
        
        self.gui_velocity_slider.pack(anchor = CENTER)
        self.gui_velocity_label.pack()
        self.gui_velocity_display.pack()

        #start
        # self.window.mainloop()


    def showgui_Tempo(self,gui_tempo_val):
        self.model.set_tempo(self.gui_tempo.get())
        sel = "Tempo: " + str(gui_tempo_val)
        self.gui_tempo_display.config(text=sel, font = ("Courier", 14))
        

    def showgui_note_length_(self,gui_note_length_val):
        self.model.set_note_length(self.gui_note_length.get())
        sel = "Note Length: " + str(gui_note_length_val)
        self.gui_note_length_display.config(text=sel, font = ("Courier", 14))


    def show_gui_velocity(self,gui_velocity_val):
        self.model.set_velocity(self.gui_velocity.get())
        sel = "Velocity: " + str(gui_velocity_val)
        self.gui_velocity_display.config(text=sel, font = ("Courier", 14))
    
    




#gui_note_length_Slider = Scale(window, variable = gui_note_length, )

# def printgui_Tempo():
#     print(stepGUI.gui_tempo)

if __name__ == "__main__":
    model = Model(75,0.08,90)
    stepGUI = StepSequencerGUI(model)
    stepGUI.window.mainloop()
    # otherWindow = Tk()
    # btn = Button(otherWindow,Text="push the gui_tempo",  bg="black", fg="white")#command=print(stepGUI.gui_tempo),
    # btn.pack()
    # otherWindow.mainloop()




    