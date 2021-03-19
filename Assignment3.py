#importing different libraries from psychopy.
from psychopy import visual, core, logging, event
#to get timestamps, import datetime library
from datetime import datetime 
#import keyboard library
from psychopy.hardware import keyboard
kb=keyboard.Keyboard()
mywin= visual.Window([800,600], monitor ='myexteriment", units="degs")
Participant_Instruction= visual.TextStim(mywin, 'Welcome to the experiment. Press 1 to continue',color=(1,1,1), colorSpace='rgb')
Participant_Instruction,draw()
mywin.update()
Subject_Response = event.waitKeys(keyList=['1','2'])
print(Subject_Response)
