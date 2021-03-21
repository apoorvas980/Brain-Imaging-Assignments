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
    Subject_Response_3 = event.waitKeys(keyList=['1'])
    print(Subject_Response_3)
    if '1' in Subject_Response_3:
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
        
          Cue_2 = visual.TextStim(mywin, 'NUMBER', color=(1,1,1), colorSpace='rgb')
          Cue_2.draw()
          mywin.update()
          core.wait(1.5)
          Trial_2 = visual.TextStim(mywin, 'H4', color=(1,1,1), colorSpace='rgb')
          Trial_2.draw()
          mywin.update()
          Trial_Response_2 = event.waitKeys(keyList=['e','o'])
          print(Trial_Response_2)
          
          Exp_Instructions = visual.TextStim(mywin, 'Trial over. Press 1 when ready', color=(1,1,1), colorSpace='rgb')
          Exp_Instructions.draw()
          mywin.update()
          Exp_Response = event.waitKeys(keyList=['1'])
          print(Exp_Response)
          core.wait(2.0)
          
          if '1' in Exp_Response:
            C1 = visual.TextStim(mywin, 'LETTER')
            C1.draw()
            mywin.update()
            core.wait(1.5)
            T1 = visual.TextStim(mywin, '8Y')
            T1.draw()
            mywin.update()
            R1 = event.waitKeys(keyList=['c','v'])
            print(R1)
            
            C2 = visual.TextStim(mywin, 'NUMBER')
            C2.draw()
            mywin.update()
            core.wait(1.5)
            T2 = visual.TextStim(mywin, 'F4')
            T2.draw()
            mywin.update()
            R2= event.waitKeys(keyList=['e','o'])
            print(R2)
            
            C3 = visual.TextStim(mywin, 'NUMBER')
            C3.draw()
            mywin.update()
            core.wait(1.5)
            T3 = visual.TextStim(mywin, 'S9')
            T3.draw()
            mywin.update()
            R3= event.waitKeys(keyList=['e','o'])
            print(R3)
            
            C4 = visual.TextStim(mywin, 'NUMBER')
            C4.draw()
            mywin.update()
            T4= visual.TextStim(mywin, 'K7')
            T4.draw()
            mywin.update()
            R4= event.waitKeys(keyList=['e','o'])
            print(R4)
            
            C5 = visual.TextStim(mywin, 'LETTER')
            C5.draw()
            mywin.update()
            T5 = visual.TextStim(mywin, '6V')
            T5.draw()
            mywin.update()
            R5 = event.waitKeys(keyList=['c','v'])
            print(R5)
            
            C6 = visual.TextStim(mywin, 'NUMBER')
            C6.draw()
            mywin.update()
            T6=visual.TextStim(mywin, 'L9')
            T6.draw()
            mywin.update()
            R6= event.waitKeys(keyList=['o','e'])
            print(R6)
            
            C7 = visual.TextStim(mywin, 'LETTER')
            C7.draw()
            mywin.update()
            T7 = visual.TextStim(mywin, 'F3')
            T7.draw()
            mywin.update()
            R7 = event.waitKeys(keyList=['c','v'])
            print(R7)
            
            C8 = visual.TextStim(mywin, 'LETTER')
            C8.draw()
            mywin.update()
            T8 = visual.TextStim(mywin, '5B')
            T8.draw()
            mywin.update()
            R8 = event.waitKeys(keyList=['c','v'])
            print(R8)
            
            C9 = visual.TextStim(mywin, 'NUMBER')
            C9.draw()
            mywin.update()
            T9 = visual.TextStim(mywin, '8L')
            T9.draw()
            mywin.update()
            R9 = event.waitKeys(keyList=['e','o'])
            print(R9)
            
            C10 = visual.TextStim(mywin, 'LETTER')
            C10.draw()
            mywin.update()
            T10 = visual.TextStim(mywin, '1S')
            T10.draw()
            mywin.update()
            R10 = event.waitKeys(keyList=['c','v'])
            print(R10)
            
            
