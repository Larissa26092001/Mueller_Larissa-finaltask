#this is a stroop task  with two blocks containing of 20 trials each
#both blocks have mixed conditions of congruent and incongruent trials but both appear equally often in a random order
#the task is to press  a when the word and the color are the same and l when they are different

from psychopy import visual, core, event, gui, data, logging
from psychopy.hardware import keyboard
import random
import os

event.globalKeys.add(key='q', modifiers=['ctrl'], func=core.quit)

#setting the basics:

#set the window size
win = visual.Window([800,600], color="white", units='pix')

#set the response keys
resp = ['a', 'l']

#setting the needed screens:

#set the instruction screen
instruction = visual.TextStim(win, text="Welcome to the Stroop Task! \nIn this task you will see a word and a color. \nYou have to press the a key when the word and the color match and the l key when they don't match.", color="black", height=30)

#set side-note screen 1
side_note1 = visual.TextStim(win, text="Lay your fingers on tab and space bar to be ready.\n There are two rounds.\nthe first round starts in 5 seconds.", color="black", height=30)

#set side-note screen 2
side_note2 = visual.TextStim(win, text="The first round is over. \nTake a short break.\n The second and last round starts in 5 seconds.", color="black", height=30)

#set end screen
end = visual.TextStim(win, text="The experiment is over now. \nThank you for participating!", color="black", height=50)

#set the response list
responses = []  # tuple of (is_response_correct, response_time, congruent/incongruent)

#list of all the colors
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "grey", "black"]

#create incongruent and congruent stimuli based on colors, by looping through the colors of the colors list above
congruent, incongruent = [], []
for color1 in colors:
    for color2 in colors: 
        (congruent if color1 == color2 else incongruent).append(visual.TextStim(win, text=color1, color=color2, height=50))

#display the instruction screen
instruction.draw()
win.flip()
core.wait(8)

#display the side note 1 screen
side_note1.draw()
win.flip
core.wait(5)

kb = keyboard.Keyboard()

#loop for the main task of experiment:
#range(2) -> two blocks/cycles, loop will quit after second block

for cycle in range(2):
    #setting the countdown 
    for i in range(5, 0, -1):
        countdown = visual.TextStim(win, text=i, color="black", height=70)
        countdown.draw()
        win.flip()
        core.wait(1)

   #displaying the 20 either congruent or incongruent stimuli in a random order
    for i in range(0, 20):
        #randomly choose congruent or incongruent stimuli
        stim = random.choice([congruent, incongruent])
        #randomly choose one of the stimuli in the congruent or incongruent list
        stim = random.choice(stim)
        #draw the stimuli on the screen
        stim.draw()
        win.flip()
        #wait for the response 
        kb.clock.reset()
        key = kb.waitKeys(keyList=resp)[0]
        
        #defining what correct responses are 
        is_correct = (key.name == "a") == (is_congruent := (stim in congruent))
        #the responses are captured and appended for the final Excel File
        responses.append((is_correct, key.rt, "congruent" if is_congruent else "incongruent"))
        
        #clear the screen
        win.flip()
        core.wait(0.5)

    #after the first block is over (cycle=0) the side note screen appears  
    if cycle == 0:
        #display side note screen 2
        side_note2.draw()
        win.flip()
        core.wait(5)

#calculating the three different response times (total, congruent, incongruent)
rt = [t for _, t, _ in responses]
rt_congruent = [t for _, t, c in responses if c == "congruent"]
rt_incongruent = [t for _, t, c in responses if c == "incongruent"]

#calucating the average total response time
avg = lambda l: sum(l) / len(l)

#displaying the three different calculated response times on the screen as a little feedback for the participant
average_response_time = visual.TextStim(win, text=f"Your average response time was {avg(rt)} seconds. \n Your average congruent response time was {avg(rt_congruent)} seconds. \n And your average incongruent response time was {avg(rt_incongruent)} seconds.", color="black", height=30)
average_response_time.draw()
win.flip()
core.wait(8)    

#calculating the total correct responses 
correctness = [c for c, _, _ in responses]
correct_total = len([c for c in correctness if c])

#displaying the total correct responses for both conditions as an immediate feedback
correct_responses_total = visual.TextStim(win, text="You got " + str(correct_total) + f" out of {len(responses)} correct. \n That is " + str(correct_total/len(responses)*100) + "% correct.", color="black", height=30)
correct_responses_total.draw()
win.flip() 
core.wait(8)

#display the end screen
end.draw()
win.flip()
core.wait(5)

#creating the excel file in which the three different data types are documented in
with open("result.csv", "w") as file:
    for is_correct, response_time, congruency in responses:
        file.write(f"{is_correct}, {response_time}, {congruency}\n")

