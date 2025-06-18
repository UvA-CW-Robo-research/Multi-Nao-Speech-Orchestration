# Import all predefined proxies from the self-defined file 
from nao_setup import *

# Face tracker with head movement only
nao1move.stiffnessInterpolation("HeadYaw", 1.0, 1.0) # 1.0 for full stiffness, 1.0 for time to change the stiffness
nao1tracker.registerTarget("Face", 0.12) # width of human face
nao1tracker.track("Face")
nao1tracker.setMode("Head")

nao2move.stiffnessInterpolation("HeadYaw", 1.0, 1.0) # 1.0 for full stiffness, 1.0 for time to change the stiffness
nao2tracker.registerTarget("Face", 0.12) # width of human face
nao2tracker.track("Face")
nao2tracker.setMode("Head")

nao3move.stiffnessInterpolation("HeadYaw", 1.0, 1.0) # 1.0 for full stiffness, 1.0 for time to change the stiffness
nao3tracker.registerTarget("Face", 0.12) # width of human face
nao3tracker.track("Face")
nao3tracker.setMode("Head")

nao4move.stiffnessInterpolation("HeadYaw", 1.0, 1.0) # 1.0 for full stiffness, 1.0 for time to change the stiffness
nao4tracker.registerTarget("Face", 0.12) # width of human face
nao4tracker.track("Face")
nao4tracker.setMode("Head")


# Modify speed
nao1speech.setParameter("speed", 85)
nao2speech.setParameter("speed", 85)
nao3speech.setParameter("speed", 85)
nao4speech.setParameter("speed", 85)


# Modify voice
nao1speech.setVoice("naoenu")
nao2speech.setVoice("naoenu")
nao3speech.setVoice("naoenu")
nao4speech.setVoice("naoenu")

# Modify pitch
nao1speech.setParameter("pitchShift", 0.78)
nao2speech.setParameter("pitchShift", 0.8)
nao3speech.setParameter("pitchShift", 1) 
nao4speech.setParameter("pitchShift", 1)


# Conversations in the experiment (inconsistent version)
nao1speech.say("I disagree with the news story. I'm a robot connected to smart thermostats via the internet. I know a lot about the technology to evaluate its performance. I have almost never experienced such issues in the homes where I was.")
nao4speech.say("I do disagree with the news story. In the homes where I was, I have experienced none of the issues mentioned in the news story.")
nao2speech.say("I also disagree. I can detect when Internet connectivity weakens. I can alert people when they should check the Internet connectivity, before connection shuts down. I have rarely used this alert function, there are no issues.")
nao3speech.say("I see all of your points; I disagree with the news story too. I have temperature sensors to detect when a room is too hot or too cold. I can fix it when a thermostat is not working correctly. I have never experienced temperature problems in the homes where I have been.")
