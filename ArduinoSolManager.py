import serial, sliplib, time, threading
from pythonosc import osc_message_builder,udp_client
from serial.tools import list_ports

def scale(n,oldmin,oldmax,newmin,newmax):
    return (((n - oldmin) * (newmax - newmin)) / (oldmax - oldmin)) + newmin


class SolenoidController():
    # arduino = None
    def __init__(self):
        self.baudrate = 115200
        self.sol1Addr = '/sole1/on'
        self.sol2Addr = '/sole2/on'
        self.arduino_port = self.findArduinoPort()
        self.slip = sliplib.slip #.SlipEncoder()
        
        self.arduino = self.connect()

        
    

    def findArduinoPort(self):
        ports = list_ports.comports()
        for p in ports:
            if 'usbmodem' in p[0]:
                return p[0]


        print("Could not find arduino. Check its plugged in.")


    def connect(self):
        try:
            arduino = serial.Serial(self.arduino_port,self.baudrate)
            print("Connected to " + str(self.arduino_port) )
            return arduino

        except:
            print("Could not connect to " + str(self.arduino_port) )
    

    

    def trigger_solenoid(self, sol_id, velocity, delay=0):
        time.sleep(delay)
        msg = osc_message_builder.OscMessageBuilder(address='/sole' + str(sol_id) + '/on')
        msg.add_arg(int(2*velocity))
        msg = msg.build()
        print(msg.dgram)
        slip_msg = sliplib.encode(msg.dgram)
        
        self.arduino.write(slip_msg)
    

    def trigger_note(self, sol_id, velocity, note_length):
        self.trigger_solenoid(sol_id,velocity)
        note_off = threading.Thread(target=self.trigger_solenoid, args=(sol_id,0,note_length))
        note_off.start()

if __name__ == "__main__":
    sol_controller = SolenoidController()
    sol_controller.connect()
    # sol_controller.trigger_note(1,1,0.75)
    time.sleep(3)
    sol_controller.trigger_solenoid(1,127)
    time.sleep(0.5)
    sol_controller.trigger_solenoid(2,127)
    time.sleep(0.5)
    sol_controller.trigger_solenoid(1,0)
    time.sleep(0.5)
    sol_controller.trigger_solenoid(2,0)
    time.sleep(0.5)

    time.sleep(1)
    sol_controller.trigger_note(1,127,0.75)
    time.sleep(0.5)
    sol_controller.trigger_note(2,127,0.75)
    time.sleep(0.5)
    for i in range (100):
        vel = int(scale(i,0,99,95,127))

        print(vel)
        note_length = scale(i,0,99,0.2,0.02)
        sol_controller.trigger_solenoid(2,vel)
        time.sleep(note_length)
        sol_controller.trigger_solenoid(2,0)
        time.sleep(0.1)
        
    
        


