This assignment 3 titled 'Performance Comparison in Task-Switching in Monolinguals and Bilinguals' analyses the difference between monolingual and bilingual groups in their effeciency to utilise executive functions. 

Through this experiemnt I try to find out if bilinguals have an advantage over monolinguals in tasks that require shifting of attention from one mental set to another.

I have used 8 participants here, 4 monolinguals and 4 bilinguals. Each of them performed the task-switching experiement, a paradigm that is known for assessing the ability to shift between different sets of instructions.

The assignment contains 3 parts:

1. The task switching paradigm coded in python for psychopy: The experiment contains two parts- 2 trial runs (to accustom the participants to the experiemntal design) and 10 experiemntal runs. The responses from the experimental runs were used to perform the analysis. It also contains instructions to be followed during the task. Responses of the participants are recorded onto a csv file along with the experimental logs which give a summary of the events during the course of the experiemnt in the form of a txt file.

2. Experimental logs: The events that took place on the monitor, such as, display of the stimulus, response of the participant along with the event's timestamp is recorded in the experimental logs for all 8 participants. The files are named such that they include the participant number and the timestamp at which the log was created Eg, P1Log_(date and time)

3. Participant Response: The responses noted during the performance for each of the participant was noted and saved as a csv file. The variables noted were:
    1. The number of experimental run for which the response is being recorded- under the first column 'Stimulus number'
    2. Timestamp at which the stimulus was displayed on the monitor- under the second column 'Stimulus display time'
    3. Timestamp at which the participant responded by pressing a key on the keyboard- under the third column 'Response time'
    4. The difference between the two timestamps was calculated under the fourth column as 'reaction Time'
  The folder also contains an analysis file that shows the results of the independent on-tailed t-test performed for assessing if the reactions times of the two groups were significantly different. 
  
An image to better understand the experiemntal paradigm: https://www.researchgate.net/figure/The-task-switching-task-adapted-from-Rogers-Monsell-1995-Each-trial-begins-with_fig1_6717507


