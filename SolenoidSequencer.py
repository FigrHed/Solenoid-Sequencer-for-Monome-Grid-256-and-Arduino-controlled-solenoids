import GridStepSequencer, ArduinoSolManager, asyncio, monome, threading, StepSequenceGUI

# note_length = 0.75

class SolenoidSequencer(GridStepSequencer.GridSequencer, ArduinoSolManager.SolenoidController, StepSequenceGUI.StepSequencerGUI):
    tempo = 120
    note_length = 0.075
    velocity = 110
    quarter_note = 60/tempo

    def __init__(self, tempo=120, note_length=0.075):
        super().__init__( tempo=tempo, note_length=note_length)
        GridStepSequencer.GridSequencer.__init__(self)
        ArduinoSolManager.SolenoidController.__init__(self)
        StepSequenceGUI.StepSequencerGUI.__init__(self)
        self.velocity = 110
        

    def trigger(self, x, y, step):
        print(self.note_length)
        ArduinoSolManager.SolenoidController.trigger_note(self,y,self.velocity,self.note_length)

    @asyncio.coroutine
    def play(self):
        print("this")
        return super().play()


    def get_quarter_note_interval(self):
        self.quarter_note = 60/(self.tempo*4)
        return self.quarter_note

    def get_note_length(self):
        self.note_length = self.GUI.get_note_length()
        # GridStepSequencer.GridSequencer.set_note_length(self,self.note_length)
        return self.note_length

    def get_velocity(self):
        self.velocity = self.GUI.get_velocity()
        # GridStepSequencer.GridSequencer.set_note_length(self,self.note_length)
        return self.velocity
    
    def parse_all_values(self):
        vals= self.get_all_values()
        tempo = vals[0]
        note_lengths = vals[1]
        self.tempo = tempo
        self.get_quarter_note_interval()
        self.note_length = vals[1]
        self.velocity = vals[2]
        

    def draw(self):
        self.parse_all_values()
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
        solenoid_sequencer.window.mainloop()

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
    
