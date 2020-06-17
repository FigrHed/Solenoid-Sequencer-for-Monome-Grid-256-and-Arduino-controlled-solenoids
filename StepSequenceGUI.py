from tkinter import *


class StepSequencerGUI:
    def __init__(self, gui_tempo=90, gui_note_length=0.075, gui_velocity=100):
        #declare tools
        self.window = Tk()
        self.window.geometry("400x300")
        
        #probably not used (test)
        self.tempo = 91
        self.note_length = 0.076
        self.velocity = 111
        #the native parameters
        self.gui_tempo = DoubleVar()
        self.gui_note_length = DoubleVar()
        self.gui_velocity = DoubleVar()
        #initialize elements
        #gui_tempo elements
        self.gui_tempo.set(gui_tempo)
        self.gui_tempo_slider = Scale( self.window, variable = self.gui_tempo, from_ = 30, to = 250, orient = HORIZONTAL, command = self.showgui_Tempo, width=25, length=200, showvalue=0, resolution=0.1)
        self.gui_tempo_label = Label(self.window, text = "Tempo")
        self.gui_tempo_display = Label(self.window)
        
        #gui_note_length_ elements
        self.gui_note_length.set(gui_note_length)
        self.gui_note_length_slider = Scale (self.window, variable = self.gui_note_length, from_ = 0.01, to = 0.5, orient = HORIZONTAL, command = self.showgui_note_length_, width=25, length=200, showvalue=0, resolution=0.001)
        self.gui_note_length_label = Label(self.window, text = "Note Length")
        self.gui_note_length_display = Label(self.window)
        
        #gui_velocity elements
        self.gui_velocity.set(gui_velocity)
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
        self.tempo = self.gui_tempo.get()
        sel = "Tempo: " + str(gui_tempo_val)
        self.gui_tempo_display.config(text=sel, font = ("Courier", 14))
        

    def showgui_note_length_(self,gui_note_length_val):
        sel = "Note Length: " + str(gui_note_length_val)
        self.note_length = self.gui_note_length.get()
        self.gui_note_length_display.config(text=sel, font = ("Courier", 14))

    def show_gui_velocity(self,gui_velocity_val):
        sel = "Velocity: " + str(gui_velocity_val)
        self.velocity = self.gui_velocity.get()
        self.gui_velocity_display.config(text=sel, font = ("Courier", 14))
    
    def get_gui_tempo(self):
        # return self.gui_tempo.get()
        # print("THIS IS GET GUI TEMPO TYPE: ", type(self.tempo))
        # print("AND ITS VALUE IS: ", self.tempo)
        return self.tempo
    
    def set_gui_tempo(self, new_gui_Tempo):
         self.tempo = new_gui_Tempo

    def get_gui_note_length(self):
        return self.note_length

    def set_gui_note_length(self, new_gui_note_length):
        self.note_length = new_gui_note_length

    def get_gui_velocity(self):
        return self.velocity

    def set_gui_velocity(self, new_gui_velocity):
        self.velocity = new_gui_velocity

    def get_all_values(self):
        tempo = self.tempo
        note_length = self.note_length
        velocity = self.velocity
        return((tempo, note_length, velocity))


#gui_note_length_Slider = Scale(window, variable = gui_note_length, )

# def printgui_Tempo():
#     print(stepGUI.gui_tempo)

if __name__ == "__main__":
    stepGUI = StepSequencerGUI()

    # otherWindow = Tk()
    # btn = Button(otherWindow,Text="push the gui_tempo",  bg="black", fg="white")#command=print(stepGUI.gui_tempo),
    # btn.pack()
    # otherWindow.mainloop()




    