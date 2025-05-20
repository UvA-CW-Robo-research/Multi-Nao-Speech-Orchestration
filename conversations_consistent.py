# Load library
from naoqi import ALProxy

# Configure robot's movement and speech
nao1speech = ALProxy("ALTextToSpeech", "192.168.0.102", 9559)
nao1move = ALProxy("ALMotion", "192.168.0.102", 9559)
nao2speech = ALProxy("ALTextToSpeech", "192.168.0.103", 9559)
nao2move = ALProxy("ALMotion", "192.168.0.103", 9559)
nao3speech = ALProxy("ALTextToSpeech", "192.168.0.101", 9559)
nao3move = ALProxy("ALMotion", "192.168.0.101", 9559)
nao4speech = ALProxy("ALTextToSpeech", "192.168.0.105", 9559)
nao4move = ALProxy("ALMotion", "192.168.0.105", 9559)


# Conversations in the experiment (inconsistent version)
nao1speech.say("I agree with the news story. I'm a robot connected to smart thermostats via the internet. I know a lot about the technology to evaluate its performance. I have almost always experienced such issues in the homes where I was.")
nao4speech.say("I do agree with the news story. In the homes where I was, I have experienced all the issues mentioned in the news story.")
nao2speech.say("I also agree. I can detect when Internet connectivity weakens. I can alert people when they should check the Internet connectivity, before connection shuts down. I have often used this alert function, there are many issues.")
nao3speech.say("I see all of your points; I agree with the news story too. I have temperature sensors to detect when a room is too hot or too cold. I can fix it when a thermostat is not working correctly. I have always experienced temperature problems in the homes where I have been.")
