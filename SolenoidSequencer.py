import GridStepSequencer, ArduinoSolManager

note_length = 0.75


def trigger(x,y,step):
    ArduinoSolManager.SolenoidController.trigger_note(y,step,note_length)

if __name__ == "__main__":
    SolenoidSequencer = GridStepSequencer(120, 0.075, trigger)

    loop = asyncio
    pass