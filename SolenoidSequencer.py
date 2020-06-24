import GridStepSequencer, ArduinoSolManager, asyncio, monome, threading, StepSequenceGUI

# note_length = 0.75
class Model():
    def __init__(self, tempo, note_length, velocity):
        self.tempo = tempo
        self.note_length = note_length
        self.velocity = velocity
        self.quarter_note = 60/(tempo*4)
    
    def get_tempo(self):
        return self.tempo
    
    def set_tempo(self, new_tempo):
        self.tempo = new_tempo
        self.set_quarter_note(new_tempo)

    def get_quarter_note(self):
        return self.quarter_note
    
    def set_quarter_note(self, new_tempo):
        self.quarter_note = 60/(new_tempo*4)

    def get_note_length(self):
        return self.note_length
    
    def set_note_length(self, new_note_length):
        self.note_length = new_note_length

    def get_velocity(self):
        return self.velocity
    
    def set_velocity(self, new_velocity):
        self.velocity = new_velocity



class SolenoidSequencer(GridStepSequencer.GridSequencer):
    
    arduino = None
    velocity = 100

    def __init__(self, tempo=120, note_length=0.075):
        super().__init__( tempo=tempo, note_length=note_length)
        GridStepSequencer.GridSequencer.__init__(self)
        # StepSequenceGUI.StepSequencerGUI.__init__(self)
        self.arduino = ArduinoSolManager.SolenoidController()
        self.model = Model(tempo, note_length, self.velocity)
        self.gui = StepSequenceGUI.StepSequencerGUI(self.model)
        

        

    def trigger(self, x, y, step):
        # print(self.note_length)
        self.arduino.trigger_note(y,self.model.get_velocity(),self.model.get_note_length())


    def update_all_values(self):
        self.tempo = self.model.get_tempo()
        self.quarter_note = self.model.get_quarter_note()
        self.note_length = self.model.get_note_length()
        self.velocity = self.model.get_velocity()
        

    def draw(self):
        self.update_all_values()
        return super().draw()





# def trigger(x,y,step):
#     ArduinoSolManager.SolenoidController.trigger_note(y,step,note_length)

if __name__ == "__main__":
    solenoid_sequencer = SolenoidSequencer(120, 0.075)

    loop = asyncio.get_event_loop()

    def serial_device_added(id, type, port):
        if type == "monome 256":
            print('connected to {} ({})'.format(id,type))
            asyncio.ensure_future(solenoid_sequencer.grid.connect('127.0.0.1',port))

    def gui_loop():
        solenoid_sequencer.gui.window.mainloop()

    def sequencer_loop():
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            solenoid_sequencer.grid.led_all(0)
    
    serialosc = monome.SerialOsc()
    serialosc.device_added_event.add_handler(serial_device_added)

    loop.run_until_complete(serialosc.connect())

    sequencer_thread = threading.Thread(target=sequencer_loop)
    sequencer_thread.start()
    gui_loop()
    
