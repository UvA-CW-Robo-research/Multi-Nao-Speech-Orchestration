# Import all predefined proxies from the self-defined file 
from test_setup import *  


# Import tools from pynput to press keys and listen for keyboard input:
# - Key: special keys like Enter or Shift
# - Controller: to press or release keys in code
# - Listener: to watch for key presses by the user
from pynput.keyboard import Key, Controller


# Face tracker with head movement only
nao1move.stiffnessInterpolation("HeadYaw", 1.0, 1.0) # 1.0 for full stiffness, 1.0 for time to change the stiffness

# Modify speed
nao1speech.setParameter("speed", 85)

# Modify voice
nao1speech.setVoice("naoenu")

# Modify pitch
nao1speech.setParameter("pitchShift", 0.78)


# Robot 1 speaks and interacts
nao1speech.say("Hello, it is nice to meet you! My name is Robin and I am a social robot. What is your name?")

print("Press Enter when participant finishes speaking.")
name = raw_input()  # Python 2.7 input

nao1speech.say("Did you manage to find the lab easily?")

answer = raw_input("Please type 'f' or 'j' and hit Enter: ")
if answer == 'f':
    nao1speech.say("That's good to hear!")
elif answer == 'j':
    nao1speech.say("It can be hard to find the lab, indeed, but luckily you made it.")

