#importing different libraries from psychopy.
from psychopy import visual, core, logging, event
#to get timestamps, import datetime library
from datetime import datetime 
#import keyboard library
from psychopy.hardware import keyboard
kb=keyboard.Keyboard()
mywin= visual.Window([800,600], monitor ="myexperiment", units="degs")
Participant_Instruction= visual.TextStim(mywin, 'Welcome to the experiment. Press 1 to continue',color=(1,1,1), colorSpace='rgb')
Participant_Instruction.draw()
mywin.update()
Subject_Response = event.waitKeys(keyList=['1'])
print(Subject_Response)
if '1' in Subject_Response:
  Participant_Instruction_2 = visual.TextStim(mywin, 'You will be shown a pair of digits, containing one number and one letter', color=(1,1,1), colorSpace='rgb')
  Participant_Instruction_2.draw()
  mywin.update()
  Subject_Response_2 = event.waitKeys(keyList=['1'])
  print(Subject_Response_2)
  if '1' in Subject_Response_2:
    Participant_Instruction_3 = visual.TextStim(mywin, 'If your cue says LETTER, press c if the letter in the pair is a consonant and v if it is a vowel', color=(1,1,1), colorSpace='rgb')
    Participant_Instruction_3.draw()
    mywin.update()
    Subject_response_3 = event.waitKeys(keyList=['1'])
    print(Subject_Response_3)
    if ' 1' in Subject_Response_3:
      Participant_Instruction_4 = visual.TextStim(mywin, 'If your cue says NUMBER, press o if the number in the pair is odd and e if it is even', color=(1,1,1), colorSpace='rgb')
      Participant_Instruction_4.draw()
      mywin.update()
      Subject_Response_4 = event.waitKeys(keyList=['1'])
      print(Subject_Response_4)
      if '1' in Subject_Response_4:
        Participant_Instruction_5 = visual.TextStim(mywin, 'Here is a trial. Get Ready.', color=(1,1,1), colorSpace='rgb')
        Participant_Instruction_5.draw()
        mywin.update()
        Subject_Response_5 = event.waitKeys(keyList=['1'])
        print(Subject_Response_5)
        if '1' in Subject_Response_5:
          Cue_1 = visual.TextStim(mywin, 'LETTER', color=(1,1,1), colorSpace='rgb')
          Cue_1.draw()
          mywin.update()
          core.wait(1.5)
          Trial_1 = visual.TextStim(mywin, '3P', color=(1,1,1), colorSpace='rgb')
          Trial_1.draw()
          mywin.update()
          Trial_Response_1 = event.waitKeys(keyList=['c','v'])
          print(Trial_Response_1)
          core.wait(2.0)
          Cue_2 = visual.TextStim(mywin, 'NUMBER', color(1,1,1), colorSpace='rgb')
          Cue_2.draw()
          mywin.update()
          core.wait(1.5)
          Trial_2 = visual.TextStim(mywin, 'H4', color(1,1,1), colorSpace='rgb')
          Trial_2.draw()
          mywin.update()
          Trial_Response_2 =  event.waitKeys(keyList=['e','o'])
          print(Trial_Response_2)
          core.wait(2.0)
