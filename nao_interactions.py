# Import all predefined proxies from the self-defined file 
from nao_setup import *
import time

# Define a list of dictionaries, each representing one robot.
# Each dictionary contains:
# - 'move': the motion control object to manage joint stiffness and movement
# - 'tracker': the face tracking object responsible for detecting and following faces
# - 'speech': the speech synthesis object controlling voice parameters
# - 'pitch': the pitch shift value specific to that robot's voice tone
robots = [
    {'move': nao1move, 'tracker': nao1tracker, 'speech': nao1speech, 'pitch': 0.78},
    {'move': nao2move, 'tracker': nao2tracker, 'speech': nao2speech, 'pitch': 0.80},
    {'move': nao3move, 'tracker': nao3tracker, 'speech': nao3speech, 'pitch': 1},
    {'move': nao4move, 'tracker': nao4tracker, 'speech': nao4speech, 'pitch': 1},
]

# Loop through each robot to configure face tracking and speech parameters:
for robot in robots:
    # Set stiffness of the 'HeadYaw' joint to maximum (1.0) with a 1-second transition.
    # This ensures the robot's head moves responsively and smoothly when tracking.
    robot['move'].stiffnessInterpolation("HeadYaw", 1.0, 1.0)
    
    # Register a target for tracking labeled "Face" with an estimated width of 0.12 meters (~12 cm).
    # This size helps the tracker correctly identify and focus on a human face.
    robot['tracker'].registerTarget("Face", 0.12)
    
    # Begin actively tracking the registered face target.
    # The robot's sensors will detect and follow the face position.
    robot['tracker'].track("Face")
    
    # Set tracking mode to "Head" so that only the robot's head moves to follow the face,
    # keeping the rest of the body stationary for stability.
    robot['tracker'].setMode("Head")
    
    # Set speech speed parameter to 85 (out of 100 or based on API scale),
    # which controls how fast the robot speaks.
    robot['speech'].setParameter("speed", 85)
    
    # Set the voice to "naoenu" (likely English voice profile),
    # defining the robot's accent and timbre.
    robot['speech'].setVoice("naoenu")
    
    # Adjust the pitch of the robot's voice by the specified pitch shift value.
    # This allows individual robots to have distinct voice tones.
    robot['speech'].setParameter("pitchShift", robot['pitch'])


# Greetings from all four robots
nao1speech.say("Hello, my name is Robin and I am a social robot. What is your name?")

ra_action1 = raw_input("Press 'Enter' when participant finishes speaking.")


nao1speech.say("It is a pleasure to meet you.")
time.sleep(1.5)

nao2speech.say("Hi, and I am Chris. Nice to meet you.")
time.sleep(1.5)

nao3speech.say("Hello, my name is Sam. It is great meeting you!")
time.sleep(1.5)

nao4speech.say("Hi there, I am Alex. Nice to meet you!")
time.sleep(2.5)


# Question 1 from Chris
nao2speech.say("Some people struggled to find the lab. Did you manage to find the lab easily?")

ra_action2 = raw_input("Press 'f' (YES) or 'j' (NO), then 'Enter': ").lower()
if ra_action2 == 'f':
    nao2speech.say("That's good to hear!")
elif ra_action2 == 'j':
    nao2speech.say("It can be hard to find the lab, indeed, but luckily you made it.")

# Question 2 from Alex
time.sleep(1.5)
nao4speech.say("Most people participated in experiments in this lab are students. Are you currently a student?")

ra_action3 = raw_input("Press 'f' (YES) or 'j' (NO), then 'Enter': ").lower()
if ra_action3 == 'f':
    nao4speech.say("Alright, and what are you studying now? Could you tell me more about it?")
elif ra_action3 == 'j':
    nao4speech.say("And what do you currently do?")

ra_action4 = raw_input("Press 'Enter' when participant finishes speaking.")

nao4speech.say("Thanks for letting me know.")

# Question 3 from Sam
time.sleep(1.5)
nao3speech.say("People do a lot of different things in their free time. What do you do in your free time?")

ra_action5 = raw_input("Press 'f' (activity MENTIONED) or 'j' (Do NOT know), then 'Enter': ").lower()
if ra_action5 == 'f':
    nao3speech.say("I see. That sounds very interesting!")
elif ra_action5 == 'j':
    nao3speech.say("I see. That is alright. Perhaps you will discover a new hobby in the future.")

# Question 4 from Robin
time.sleep(1.5)
nao1speech.say("It is really nice that you came over for the experiment today. Do you frequently participate in experiments?")

ra_action6 = raw_input("Press 'f' (YES) or 'j' (NO), then 'Enter': ").lower()
if ra_action6 == 'f':
    nao1speech.say("That is great!")
elif ra_action6 == 'j':
    nao1speech.say("It is great that you will participate today!")
