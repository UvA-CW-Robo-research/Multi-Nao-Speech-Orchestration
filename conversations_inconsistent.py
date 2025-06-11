# Load library
from naoqi import ALProxy

# Configure robot's movement, speech, tracker
nao1speech = ALProxy("ALTextToSpeech", "192.168.0.102", 9559)
nao1tracker = ALProxy("ALTracker", "192.168.0.102", 9559)
nao1move = ALProxy("ALMotion", "192.168.0.102", 9559)

nao2speech = ALProxy("ALTextToSpeech", "192.168.0.103", 9559)
nao2tracker = ALProxy("ALTracker", "192.168.0.103", 9559)
nao2move = ALProxy("ALMotion", "192.168.0.103", 9559)

nao3speech = ALProxy("ALTextToSpeech", "192.168.0.101", 9559)
nao3tracker = ALProxy("ALTracker", "192.168.0.101", 9559)
nao3move = ALProxy("ALMotion", "192.168.0.101", 9559)

nao4speech = ALProxy("ALTextToSpeech", "192.168.0.105", 9559)
nao4tracker = ALProxy("ALTracker", "192.168.0.105", 9559)
nao4move = ALProxy("ALMotion", "192.168.0.105", 9559)


# Face tracker with head movement only
nao1move.stiffnessInterpolation("HeadYaw", 1.0, 5.0) # time argument not so sure
nao1tracker.registerTarget("Face", 5) # width parameter not so sure
nao1tracker.track("Face")
nao1tracker.setMode("Head")
# print(nao1tracker.isActive())

nao2move.stiffnessInterpolation("HeadYaw", 1.0, 5.0) # time argument not so sure
nao2tracker.registerTarget("Face", 5) # width parameter not so sure
nao2tracker.track("Face")
nao2tracker.setMode("Head")
# print(nao2tracker.isActive())

nao3move.stiffnessInterpolation("HeadYaw", 1.0, 5.0) # time argument not so sure
nao3tracker.registerTarget("Face", 5) # width parameter not so sure
nao3tracker.track("Face")
nao3tracker.setMode("Head")
# print(nao3tracker.isActive())

nao4move.stiffnessInterpolation("HeadYaw", 1.0, 5.0) # time argument not so sure
nao4tracker.registerTarget("Face", 5) # width parameter not so sure
nao4tracker.track("Face")
nao4tracker.setMode("Head")
# print(nao4tracker.isActive())


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

print(nao4speech.getAvailableVoices())


# Conversations in the experiment (inconsistent version)
nao1speech.say("I disagree with the news story. I'm a robot connected to smart thermostats via the internet. I know a lot about the technology to evaluate its performance. I have almost never experienced such issues in the homes where I was.")
nao4speech.say("I do disagree with the news story. In the homes where I was, I have experienced none of the issues mentioned in the news story.")
nao2speech.say("I also disagree. I can detect when Internet connectivity weakens. I can alert people when they should check the Internet connectivity, before connection shuts down. I have rarely used this alert function, there are no issues.")
nao3speech.say("I see all of your points; I disagree with the news story too. I have temperature sensors to detect when a room is too hot or too cold. I can fix it when a thermostat is not working correctly. I have never experienced temperature problems in the homes where I have been.")
