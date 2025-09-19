# Load libraries
from naoqi import ALProxy
import time, threading, random
import pandas as pd
import os

# Define the IP address of each NAO robot
nao1_ip = "192.168.0.102"  
nao2_ip = "192.168.0.103"
nao3_ip = "192.168.0.101"  
nao4_ip = "192.168.0.105"  

# Define the port number used to connect to NAOqi on each robot
# NAOqi is the central software system that lets you control and communicate with NAO.
port = 9559

# Summary of the following proxies:
# - The ALTextToSpeech module allows the robot to speak.
# - The ALTracker module allows the robot to track different targets using different means (head only, whole body, move, etc).
# - The ALMotion module provides methods which facilitate making the robot move.
# - ALRobotPosture module allows you to make the robot go to different predefined postures.
# - ALLeds module provides simple ways of setting or fading the intensity of a LED or a group of LEDs

# Initialize proxies for NAO1
nao1speech = ALProxy("ALTextToSpeech", nao1_ip, port) 
nao1tracker = ALProxy("ALTracker", nao1_ip, port) 
nao1move = ALProxy("ALMotion", nao1_ip, port) 
nao1pose = ALProxy("ALRobotPosture", nao1_ip, port)
nao1leds = ALProxy("ALLeds", nao1_ip, port)


# Initialize proxies for NAO2
nao2speech = ALProxy("ALTextToSpeech", nao2_ip, port) 
nao2tracker = ALProxy("ALTracker", nao2_ip, port) 
nao2move = ALProxy("ALMotion", nao2_ip, port)
nao2pose = ALProxy("ALRobotPosture", nao2_ip, port)
nao2leds = ALProxy("ALLeds", nao2_ip, port)


# Initialize proxies for NAO3
nao3speech = ALProxy("ALTextToSpeech", nao3_ip, port)
nao3tracker = ALProxy("ALTracker", nao3_ip, port) 
nao3move = ALProxy("ALMotion", nao3_ip, port) 
nao3pose = ALProxy("ALRobotPosture", nao3_ip, port)
nao3leds = ALProxy("ALLeds", nao3_ip, port)


# Initialize proxies for NAO4
nao4speech = ALProxy("ALTextToSpeech", nao4_ip, port) 
nao4tracker = ALProxy("ALTracker", nao4_ip, port) 
nao4move = ALProxy("ALMotion", nao4_ip, port) 
nao4pose = ALProxy("ALRobotPosture", nao4_ip, port)
nao4leds = ALProxy("ALLeds", nao4_ip, port)



# Define a list of dictionaries, each representing one robot.
# Each dictionary contains:
# - 'id': The identification of each robot
# - 'move': the motion control object to manage joint stiffness and movement
# - 'tracker': the face tracking object responsible for detecting and following faces
# - 'speech': the speech synthesis object controlling voice parameters
# - 'pitch': the pitch shift value specific to that robot's voice tone
robots = [
    {'id': 1, 'move': nao1move, 'tracker': nao1tracker, 'speech': nao1speech, 'pitch': 0.78, 'leds': nao1leds},
    {'id': 2, 'move': nao2move, 'tracker': nao2tracker, 'speech': nao2speech, 'pitch': 0.80, 'leds': nao2leds},
    {'id': 3, 'move': nao3move, 'tracker': nao3tracker, 'speech': nao3speech, 'pitch': 1, 'leds': nao3leds},
    {'id': 4, 'move': nao4move, 'tracker': nao4tracker, 'speech': nao4speech, 'pitch': 1, 'leds': nao4leds}
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

    # LEDs (of eyes) ON initially
    robot['leds'].on('FaceLeds')



# Define the function for blinking while speaking
def say_with_blinking(speech_proxy, leds_proxy, text):
    talking = [True]

    def natural_blink():
        while talking[0]:
            # Shorter, more frequent blinks for visibility
            time.sleep(random.uniform(0.5, 1.5))  
            try:
                leds_proxy.off("FaceLeds")
            except Exception:
                pass
            time.sleep(0.2)  # blink duration slightly longer
            try:
                leds_proxy.on("FaceLeds")
            except Exception:
                pass

    leds_proxy.on("FaceLeds")  # ensure eyes ON
    blink_thread = threading.Thread(target=natural_blink)
    blink_thread.setDaemon(True)
    blink_thread.start()

    speech_proxy.say(text)
    talking[0] = False
    blink_thread.join()
    leds_proxy.on("FaceLeds")  # make sure eyes stay ON