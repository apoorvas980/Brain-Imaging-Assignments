#importing different libraries from psychopy.
from psychopy import visual, core, logging, event
#to get timestamps, import datetime library
from datetime import datetime
#to get timestamp and include it in the log file ExpLog
timestamp=datetime.now().strftime("%d%m%Y-%H%M%S")
lastLog = logging.LogFile("ExpLog_"+timestamp+".log", level=logging.INFO, filemode ='w')
#import keyboard library
from psychopy.hardware import keyboard
#to get a text file where participant responses will be exported and further analysis can be done based on reaction time 
#Name of the file can be changed accroding to the number of the participant eg. Participant_1_Bilingual
dataFile = open('Participant Response Record.csv', 'w')
#create keyboard object
kb=keyboard.Keyboard()

#Create a window and give the specifications
#For this experiment, following speicifications were used 
#AspectRatio: 1024 X 786
#Screen Distance: 30cm
#Screen Width: 30cm
mywin= visual.Window([800,600], monitor ="myexperiment", units="degs")

#Welcome message
Participant_Instruction= visual.TextStim(mywin, 'Welcome to the experiment. Press 1 to continue',color=(1,1,1), colorSpace='rgb') #specifying the colour of the text as white
Participant_Instruction.draw()  #for instructions to be drawn on the screen
mywin.update()   #updating the monitor
Subject_Response = event.waitKeys(keyList=['1'])     #Participant needs to press key '1' to move to the next set of instructions
print(Subject_Response)
if '1' in Subject_Response:           #If command, only if participant presses key '1' will the next set of instructions be shown
  Participant_Instruction_2 = visual.TextStim(mywin, 'You will be shown a pair of digits, containing one number and one letter', color=(1,1,1), colorSpace='rgb')   #2nd set of instructions about the experiment 
  Participant_Instruction_2.draw()    #draw the instructions on the screen
  mywin.update()    #update the window
  Subject_Response_2 = event.waitKeys(keyList=['1'])    #specifying key '1' to be accepted as a response 
  print(Subject_Response_2)
  if '1' in Subject_Response_2:   #If command, only if participant presses key '1' will the next set of instructions be shown
    Participant_Instruction_3 = visual.TextStim(mywin, 'If your cue says LETTER, press c if the letter in the pair is a consonant and v if it is a vowel', color=(1,1,1), colorSpace='rgb')   # 3rd set of instructions for the experiment 
    Participant_Instruction_3.draw()    #draw the instructions on the screen
    mywin.update()    #update the window
    Subject_Response_3 = event.waitKeys(keyList=['1'])    #specifying key '1' to be accepted as a response from the participant
    print(Subject_Response_3)
    if '1' in Subject_Response_3:      #If command, only if participant presses key '1' will the next set of instructions be shown
      Participant_Instruction_4 = visual.TextStim(mywin, 'If your cue says NUMBER, press o if the number in the pair is odd and e if it is even', color=(1,1,1), colorSpace='rgb')
      Participant_Instruction_4.draw()    #draw the instructions on the screen
      mywin.update()    #update the window
      Subject_Response_4 = event.waitKeys(keyList=['1'])    #specifying key '1' to be accepted as a response from the participant
      print(Subject_Response_4)
      if '1' in Subject_Response_4:     #If command, only if participant presses key '1' will the next set of instructions be shown
        Participant_Instruction_5 = visual.TextStim(mywin, 'Here is a trial. Get Ready.', color=(1,1,1), colorSpace='rgb')    #warning before trial starts
        Participant_Instruction_5.draw()    #draw the instructions on the screen
        mywin.update()    #update the window
        Subject_Response_5 = event.waitKeys(keyList=['1'])    #specifying key '1' to be accepted as a response from the participant as a sign that the participant is ready
        print(Subject_Response_5)
        if '1' in Subject_Response_5:   #If command, only if participant presses key '1' will the trial be started
          
          #TRIAL 1
          Cue_1 = visual.TextStim(mywin, 'LETTER', color=(1,1,1), colorSpace='rgb')       #Cue for trial 1 is LETTER, Participant has to decide if the letter in the stimulus pair is a consonant or a vowel
          Cue_1.draw()    #draw the Cue
          mywin.update()    
          core.wait(1.5)    #Added a 1.5 seconds wait before the participant will be shown the Stimulus automatically
          Trial_1 = visual.TextStim(mywin, '3P', color=(1,1,1), colorSpace='rgb')   #Stimulus pair 
          Trial_1.draw()    #draw the stimulus pair on the monitor
          mywin.update()
          Trial_Response_1 = event.waitKeys(keyList=['c','v'])    #Responses acceptable are c for consonant and v for vowel. Next trial will be shown only after response is recieved
          print(Trial_Response_1)
          
          #TRIAL 2
          Cue_2 = visual.TextStim(mywin, 'NUMBER', color=(1,1,1), colorSpace='rgb')     #Cue for trial 2 is NUMBER, Participant has to decide if the number in the stimulus pair is odd or even   
          Cue_2.draw()
          mywin.update()
          core.wait(1.5)
          Trial_2 = visual.TextStim(mywin, 'H4', color=(1,1,1), colorSpace='rgb')     #Stimulus pair for trial 2
          Trial_2.draw()
          mywin.update()
          Trial_Response_2 = event.waitKeys(keyList=['e','o'])      #Responses acceptable are c for consonant and v for vowel. Next trial will be shown only after response is recieved
          print(Trial_Response_2)
          
          Exp_Instructions = visual.TextStim(mywin, 'Trial over. Press 1 when ready', color=(1,1,1), colorSpace='rgb')    #Warning that trial is over
          Exp_Instructions.draw()
          mywin.update()
          Exp_Response = event.waitKeys(keyList=['1'])    #specifying key '1' to be accepted as a response from the participant as a sign that the participant is ready
          print(Exp_Response)
          core.wait(2.0)    #A wait for 2 seconds before the actual experiment begins
          
          if '1' in Exp_Response:     #If command, only if participant presses key '1' will the experimental runs be started
            
            #EXPERIMENTAL RUN 1
            C1 = visual.TextStim(mywin, 'LETTER')   #Cue for experimental run
            C1.draw()
            mywin.update()
            core.wait(1.5)    #waiting time specified as 1.5 seconds after which the stimulus will be displayed automatically
            T1 = visual.TextStim(mywin, '8E')     #Stimulus for experiemntal run
            T1.draw()
            T1time=str(core.getTime(applyZero=True))    #Recording the time of the display of stimulus in the participant response record
            mywin.update()
            R1 = event.waitKeys(keyList=['c','v'])
            R1time=str(core.getTime(applyZero=True))    #recording the time at which participant response was entered
            print(R1)
            dataFile.write('Stimulus Number'+','+'Stimulus Display Time'+','+'Response Time'+'\n')    #Specifying the columns of the file in which the participant response data is recorded
            dataFile.write('Stimulus1'+','+T1time+','+R1time+'\n')      #First coloumn to show stimulus number, second column to show Time of stimulus display, Third column to show Time of response 
            
            #EXPERIMENTAL RUN 2
            C2 = visual.TextStim(mywin, 'NUMBER')
            C2.draw()
            mywin.update()
            core.wait(1.5)
            T2 = visual.TextStim(mywin, 'F4')
            T2.draw()
            T2time=str(core.getTime(applyZero=True))
            mywin.update()
            R2= event.waitKeys(keyList=['e','o'])
            R2time=str(core.getTime(applyZero=True))
            print(R2)
            dataFile.write('Stimulus2'+','+T2time+','+R2time+'\n')
            
            
            #EXPERIMENTAL RUN 3
            C3 = visual.TextStim(mywin, 'NUMBER')
            C3.draw()
            mywin.update()
            core.wait(1.5)
            T3 = visual.TextStim(mywin, 'S9')
            T3.draw()
            T3time=str(core.getTime(applyZero=True))
            mywin.update()
            R3= event.waitKeys(keyList=['e','o'])
            R3time=str(core.getTime(applyZero=True))
            print(R3)
            dataFile.write('Stimulus3'+','+T3time+','+R3time+'\n')
            
            
            #EXPERIMENTAL RUN 4
            C4 = visual.TextStim(mywin, 'NUMBER')
            C4.draw()
            mywin.update()
            core.wait(1.5)
            T4= visual.TextStim(mywin, 'K7')
            T4.draw()
            T4time=str(core.getTime(applyZero=True))
            mywin.update()
            R4= event.waitKeys(keyList=['e','o'])
            R4time=str(core.getTime(applyZero=True))
            print(R4)
            dataFile.write('Stimulus4'+','+T4time+','+R4time+'\n')
            
            
            #EXPERIMENTAL RUN 5
            C5 = visual.TextStim(mywin, 'LETTER')
            C5.draw()
            mywin.update()
            core.wait(1.5)
            T5 = visual.TextStim(mywin, '6U')
            T5.draw()
            T5time=str(core.getTime(applyZero=True))
            mywin.update()
            R5 = event.waitKeys(keyList=['c','v'])
            R5time=str(core.getTime(applyZero=True))
            print(R5)
            dataFile.write('Stimulus5'+','+T5time+','+R5time+'\n')
            
            
            #EXPERIMENTAL RUN 6
            C6 = visual.TextStim(mywin, 'NUMBER')
            C6.draw()
            mywin.update()
            core.wait(1.5)
            T6=visual.TextStim(mywin, 'L9')
            T6.draw()
            T6time=str(core.getTime(applyZero=True))
            mywin.update()
            R6= event.waitKeys(keyList=['o','e'])
            R6time=str(core.getTime(applyZero=True))
            print(R6)
            dataFile.write('Stimulus6'+','+T6time+','+R6time+'\n')
            
            
            #EXPERIMENTAL RUN 7
            C7 = visual.TextStim(mywin, 'LETTER')
            C7.draw()
            mywin.update()
            core.wait(1.5)
            T7 = visual.TextStim(mywin, 'F3')
            T7.draw()
            T7time=str(core.getTime(applyZero=True))
            mywin.update()
            R7 = event.waitKeys(keyList=['c','v'])
            R7time=str(core.getTime(applyZero=True))
            print(R7)
            dataFile.write('Stimulus7'+','+T7time+','+R7time+'\n')
            
            
            #EXPERIMENTAL RUN 8
            C8 = visual.TextStim(mywin, 'LETTER')
            C8.draw()
            mywin.update()
            core.wait(1.5)
            T8 = visual.TextStim(mywin, '5B')
            T8.draw()
            T8time=str(core.getTime(applyZero=True))
            mywin.update()
            R8 = event.waitKeys(keyList=['c','v'])
            R8time=str(core.getTime(applyZero=True))
            print(R8)
            dataFile.write('Stimulus8'+','+T8time+','+R8time+'\n')
            
            
            #EXPERIMENTAL RUN 9
            C9 = visual.TextStim(mywin, 'NUMBER')
            C9.draw()
            mywin.update()
            core.wait(1.5)
            T9 = visual.TextStim(mywin, '8L')
            T9.draw()
            T9time=str(core.getTime(applyZero=True))
            mywin.update()
            R9 = event.waitKeys(keyList=['e','o'])
            R9time=str(core.getTime(applyZero=True))
            print(R9)
            dataFile.write('Stimulus9'+','+T9time+','+R9time+'\n')
            
            
            #EXPERIMENTAL RUN 10
            C10 = visual.TextStim(mywin, 'LETTER')
            C10.draw()
            mywin.update()
            core.wait(1.5)
            T10 = visual.TextStim(mywin, '1S')
            T10.draw()
            T10time=str(core.getTime(applyZero=True))
            mywin.update()
            R10 = event.waitKeys(keyList=['c','v'])
            R10time=str(core.getTime(applyZero=True))
            print(R10)
            dataFile.write('Stimulus10'+','+T10time+','+R10time+'\n')
            
Final_message = visual.TextStim(mywin, 'Thank You for participating')     #Final message display after all 10 runs are completed
Final_message.draw()    #drawing the message of the monitor
mywin.update()      #updating the monitor

core.wait(2.0)    #wait for 2 seconds before the window closes
