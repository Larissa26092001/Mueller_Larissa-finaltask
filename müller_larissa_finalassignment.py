#this is a stroop task  with two blocks containing of 20 trials each
#both blocks have mixed conditions of congruent and incongruent trials but both appeard equally often in a random order
#the task is to press the key tab when the word and the color are the same and the space key when they are different

from psychopy import visual, core, event, gui, data, logging
import random
import time
import os

event.globalKeys.add(key='q', modifiers=['ctrl'], func=core.quit)

#setting the basics:

#set the window size
win = visual.Window([800,600], color="white", units='pix')

#set the response keys
resp = ['tab', 'space']

#setting the needed screens

#set the instruction screen
instruction = visual.TextStim(win, text="Welcome to the Stroop Task! \nIn this task you will see a word and a color. \nYou have to press the tab key when the word and the color match and the space key when they don't match.", color="black", height=30)

#set side-note screen 1
side_note1 = visual.TextStim(win, text="Lay your fingers on tab and space bar to be ready.\n There are two rounds.\nthe first round starts in 5 seconds.", color="black", height=30)

#set side-note screen 2
side_note2 = visual.TextStim(win, text="The first round is over. \nTake a short break.\n The second and last round starts in 5 seconds.", color="black", height=30)

#set end screen
end = visual.TextStim(win, text="The experiment is over now. \nThank you for participating!", color="black", height=50)

#setting the needed lists

#set the response time list
response_time = []

#response time congruent
response_time_congruent = []

#response time incongruent
response_time_incongruent = []

#set the response list
response = []

#set the correct responses list
correct_responses = []

#set the average response time list
average_response_time = []

#set the total correct responses list
correct_responses_total = []

#set the correct incongruent responses list
correct_responses_incongruent = []

#set the correct congruent responses list
correct_responses_congruent = []

#list of the countdowm numbers
countdown_list = [5, 4, 3, 2, 1]

#defining the different stimuli for congruent and incongruent condition

#set congruent stimuli
congruent1 = visual.TextStim(win, text="red", color="red", height=50)
congruent2 = visual.TextStim(win, text="blue", color="blue", height=50)
congruent3 = visual.TextStim(win, text="green", color="green", height=50)
congruent4 = visual.TextStim(win, text="yellow", color="yellow", height=50)
congruent5 = visual.TextStim(win, text="orange", color="orange", height=50)
congruent6 = visual.TextStim(win, text="purple", color="purple", height=50)
congruent7 = visual.TextStim(win, text="pink", color="pink", height=50)
congruent8 = visual.TextStim(win, text="brown", color="brown", height=50)
congruent9 = visual.TextStim(win, text="grey", color="grey", height=50)
congruent10 = visual.TextStim(win, text="black", color="black", height=50)

#define the incongruent stimuli
incongruent1 = visual.TextStim(win, text="red", color="blue", height=50)
incongruent2 = visual.TextStim(win, text="blue", color="red", height=50)
incongruent3 = visual.TextStim(win, text="green", color="yellow", height=50)
incongruent4 = visual.TextStim(win, text="yellow", color="green", height=50)
incongruent5 = visual.TextStim(win, text="orange", color="purple", height=50)
incongruent6 = visual.TextStim(win, text="purple", color="orange", height=50)
incongruent7 = visual.TextStim(win, text="pink", color="brown", height=50)
incongruent8 = visual.TextStim(win, text="brown", color="pink", height=50)
incongruent9 = visual.TextStim(win, text="grey", color="black", height=50)
incongruent10 = visual.TextStim(win, text="black", color="grey", height=50)

#set the congruent stimuli list
congruent = [congruent1, congruent2, congruent3, congruent4, congruent5, congruent6, congruent7, congruent8, congruent9, congruent10]

#set the incongruent stimuli list
incongruent = [incongruent1, incongruent2, incongruent3, incongruent4, incongruent5, incongruent6, incongruent7, incongruent8, incongruent9, incongruent10]

#display the instruction screen
instruction.draw()
win.flip()
core.wait(8)

#display the side note 1 screen
side_note1.draw()
win.flip
core.wait(5)

#loop through the countdown numbers 
for i in countdown_list:
    countdown = visual.TextStim(win, text=i, color="black", height=70)
    countdown.draw()
    win.flip()
    core.wait(1)

#first block of two blocks starts here:
for i in range(0, 20):
    #randomly choose congruent or incongruent stimuli
    stim = random.choice([congruent, incongruent])
    #randomly choose one of the stimuli in the congruent or incongruent list
    stim = random.choice(stim)
    #draw the stimuli on the screen
    stim.draw()
    win.flip()
    #start the timer -> returns the number of seconds passed since the point where time begins
    start = time.time()
    #wait for the response 
    key = event.waitKeys(keyList=resp)
    #stop the timer
    stop = time.time()
    #calculate the response time
    rt = stop - start
    #append the response time to the response time list -> append: will place new items in the available space.
    response_time.append(rt)
    #append the response to the response list
    response.append(key)
    #append the correct response to the correct responses list -> adds the number of times the participant pressed the tab key when it was a congruent stimuli to the list
    if stim in congruent:
        correct_responses.append('tab')
    else:
        correct_responses.append('space')
    #append the correct response for incongruent stimuli to the correct responses list
    if stim in incongruent:
        correct_responses_incongruent.append('space')
    else:
        correct_responses_incongruent.append('tab')   
    #append the response time for congruent stimuli to the response time list
    if stim in congruent: 
        response_time_congruent.append(rt)
    else:
        response_time_incongruent.append(rt)
    #append the response time for incongruent stimuli to the response time list
    if stim in incongruent:
        response_time_incongruent.append(rt)
    else:
        response_time_congruent.append(rt)
    #clear the screen
    win.flip()
    core.wait(0.5)

#display side note screen 2
side_note2.draw()
win.flip()
core.wait(5)

#loop through the countdown
for i in countdown_list:
    countdown = visual.TextStim(win, text=i, color="black", height=70)
    countdown.draw()
    win.flip()
    core.wait(1)

#second block of two blocks starts here
for i in range(0, 20):
    #randomly choose congruent or incongruent stimuli
    stim = random.choice([congruent, incongruent])
    #randomly choose one of the stimuli in the congruent or incongruent list
    stim = random.choice(stim)
    #draw the stimuli on the screen
    stim.draw()
    win.flip()
    #start the timer
    start = time.time()
    #wait for the response
    key = event.waitKeys(keyList=resp)
    #stop the timer
    stop = time.time()
    #calculate the response time
    rt = stop - start
    #append the response time to the response time list
    response_time.append(rt)
    #append the response to the response list
    response.append(key)
    #append the correct response for congruent stimuli to the correct responses list
    if stim in congruent:
        correct_responses_congruent.append('tab')
    else:
        correct_responses_congruent.append('space')
  #append the correct response for incongruent stimuli to the correct responses list
    if stim in incongruent:
        correct_responses_incongruent.append('space')
    else:
        correct_responses_incongruent.append('tab')
    #append the response time for congruent stimuli to the response time list
    if stim in congruent: 
        response_time_congruent.append(rt)
    else:
        response_time_incongruent.append(rt)
    #append the response time for incongruent stimuli to the response time list
    if stim in incongruent:
        response_time_incongruent.append(rt)
    else:
        response_time_congruent.append(rt)
    #clear the screen
    win.flip()
    core.wait(0.5)

#calculate the average response time total, the average congruent response time and average incongruent response time -> len() function is used to calculate the length of the list (the number of data items presented in the list)
average_response_time.append(sum(response_time)/len(response_time))
average_congruent_response_time = sum(response_time_congruent)/len(response_time_congruent)
average_incongruent_response_time = sum(response_time_incongruent)/len(response_time_incongruent)
average_response_time = sum(response_time)/len(response_time)

#display the three calculated response times on the screen as a little feedback for the participant
average_response_time = visual.TextStim(win, text="Your average response time was " + str(average_response_time) + " seconds. \n Your average congruent response time was " + str(average_congruent_response_time) + " seconds. \n And your average incongruent response time was " + str(average_incongruent_response_time) + " seconds.", color="black", height=30)
average_response_time.draw()
win.flip()
core.wait(8)    

#count the number of tabs in the correct congruent lists and the number of spaces in the correct incongruent lists ->counts number of items in the lists
correct_congruent = correct_responses_congruent.count('tab')
correct_incongruent = correct_responses_incongruent.count('space')
correct_total = correct_congruent + correct_incongruent

#display the total correct responses for both conditions
correct_responses_total = visual.TextStim(win, text="You got " + str(correct_total) + " out of 40 correct. \n That is " + str(correct_total/40*100) + "% correct.", color="black", height=30)
correct_responses_total.draw()
win.flip() 
core.wait(8)

#display the end screen
end.draw()
win.flip()
core.wait(5)

#saving the three response times in seperate text files
response_time_data = open('response_time_data.txt', 'w')
info = "response_time"
response_time_data.write(info)
response_time_data.write('\n')
for i in response_time:
    response_time_data.write(str(i))
    response_time_data.write('\n')
response_time_data.close()

response_time_congruent = open('response_time_congruent.txt', 'w')
info = "response_time_congruent"
response_time_congruent.write(info)
response_time_congruent.write('\n')
for i in response_time_congruent:
    response_time_congruent.write(str(i))
    response_time_congruent.write('\n')
response_time_congruent.close()

response_time_incongruent = open('response_time_incongruent.txt', 'w')
info = "response_time_incongruent"
response_time_incongruent.write(info)
response_time_incongruent.write('\n')
for i in response_time_incongruent:
    response_time_incongruent.write(str(i))
    response_time_incongruent.write('\n')
response_time_incongruent.close()

#save the correct responses in a text file
correct_responses = open('correct_responses.txt', 'w')
info = "correct_responses"
correct_responses.write(info)
correct_responses.write('\n')
for i in correct_responses:
    correct_responses.write(str(i))
    correct_responses.write('\n')
correct_responses.close()

#save the correct responses for congruent stimuli in a text file
correct_responses_congruent = open('correct_responses_congruent.txt', 'w')
info = "correct_responses_congruent"
correct_responses_congruent.write(info)
correct_responses_congruent.write('\n')
for i in correct_responses_congruent:
    correct_responses_congruent.write(str(i))
    correct_responses_congruent.write('\n')
correct_responses_congruent.close()

#save the correct responses for incongruent stimuli in a text file
correct_responses_incongruent = open('correct_responses_incongruent.txt', 'w')
info = "correct_responses_incongruent"
correct_responses_incongruent.write(info)
correct_responses_incongruent.write('\n')
for i in correct_responses_incongruent:
    correct_responses_incongruent.write(str(i))
    correct_responses_incongruent.write('\n')
correct_responses_incongruent.close()

