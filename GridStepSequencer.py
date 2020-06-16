import asyncio, monome, serial, StepSequenceGUI, threading, continuous_threading, multiprocessing

class GridSequencer(monome.GridApp):
    def __init__(self,tempo=120,noteLength=0.075,trigger_function=''):
        super().__init__() #('/monome') ##optional address causing problems##
        
        self.GUI = StepSequenceGUI.StepSequencerGUI()
        print("Debug 2")
        self.trigger = self.trigger_function

        self.tempo = tempo
        self.quarterNote = 60/self.tempo

        self.noteLength = noteLength

    def on_grid_ready(self):
        self.play_position = 0
        self.loopStart = 0
        self.loopEnd = self.grid.width-1
        self.playHead = 0
        self.firstKey = 0
        self.secndKey = 0
        self.keysPressed = 0

        

        print ("Grid connected: " + str(self.grid.width) + " x " + str(self.grid.height) )
        self.buffer = monome.GridBuffer(self.grid.width, self.grid.height)

        self.step = [[0 for col in range(self.grid.width)] for row in range(1,self.grid.height)]
        asyncio.ensure_future(self.play() )

    @asyncio.coroutine
    def play(self):
        while True:
            self.buffer.led_level_set(self.play_position,self.playHead,0)
            if self.play_position == self.loopEnd:
                self.play_position = self.loopStart
            else:
                self.play_position += 1
            self.buffer.led_level_set(self.play_position, self.playHead, 15)

            self.draw()

            yield from asyncio.sleep(self.getQuarterNoteInterval())
    
    # def trigger(self,x,y):
    #     #print ("Triggered: " + str(x) + " and " + str(y) + " which contains: " + str(self.step[y][x]))
    #     pass

    def getQuarterNoteInterval(self):
        self.tempo = self.GUI.tempo.get()
        self.quarterNote = 60/self.tempo
        return self.quarterNote
        
    def on_grid_key(self, x, y, s):
        if y == 0:
            if s > 0:
                self.keysPressed == 1
                self.loopEnd = self.grid.width-1
                self.buffer.led_set(self.play_position, self.playHead, 0)
                self.play_position = 0
            if self.keysPressed == 2:
                self.secndKey = x
                print("first key val: " + str(self.firstKey) + " second key val: " + str(self.secndKey))
                self.loopStart = min(self.firstKey,self.secndKey)
                self.loopEnd = max(self.firstKey,self.secndKey)
                self.buffer.led_set(self.play_position,self.playHead,0)
                self.play_position = self.loopStart
            else:
                self.keysPressed -= 1
        
        if s == 1 and y < 16 and y > 0:
            self.step[y][x] ^= 1

            self.draw()
    
    def draw(self):
        for x in range(self.grid.width):
            for y in range(1,15):
                currentNode = self.step[y][self.play_position]
                self.buffer.led_level_set(x,y,self.step[y][x]*15)
                if x == self.play_position and currentNode == 1:
                    
                    self.trigger(self.play_position,y,currentNode)
        self.buffer.render(self.grid)

    def trigger_function(self, x,y,step):
        print ("Triggered: " + str(x) + " and " + str(y) + " which contains: " + str(step))


def step_trigger(x,y,step):
    print("These bad boys got trigggggggggggggg: " + str(x) + " & " + str(y) )

if __name__ == "__main__":
    
    grid_sequencer = GridSequencer(120, 0.075)
    
    grid_sequencer.trigger = step_trigger

    tempo = 0.01

    loop = asyncio.get_event_loop()


    def serialosc_device_added(id, type, port):
        print('connected to {} ({})'.format(id,type))
        asyncio.ensure_future(grid_sequencer.grid.connect('127.0.0.1',port))
    
    def gui_loop():
        grid_sequencer.GUI.window.mainloop()

    def sequencer_loop():
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            grid_sequencer.grid.led_all(0)

    serialosc = monome.SerialOsc()
    serialosc.device_added_event.add_handler(serialosc_device_added)

    loop.run_until_complete(serialosc.connect())
    print("Debug 3")

    # guiProcess = multiprocessing.Process(target=gui_loop)

    # guiProcess.start()
    sequencerProcess = threading.Thread(target=sequencer_loop)

    print("Debug 4")
    sequencerProcess.start()
    print("Debug 5")
    gui_loop()    



