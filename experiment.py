import pandas as pd
from nao_setup import *

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

# Ask user which version of the conversation to use
version = raw_input("Press 'f' (CONSISTENT) or 'j' (INCONSISTENT), then 'Enter': ").lower()

if version == 'f':
    version_file = 'consistent.xlsx'
    print("You selected the CONSISTENT version.")
else version == 'j':
    version_file = 'inconsistent.xlsx'
    print("You selected the INCONSISTENT version.")

# Load script from the selected file
df = pd.read_excel(version_file)

# Speak each line of text with the corresponding robot
for _, row in df.iterrows():
    robot = next(r for r in robots if r['id'] == row['robot_id'])
    robot['speech'].say(row['text'])


