# Load library
from naoqi import ALProxy
import time

# Configure robot's motion, audio, and trackers
nao1speech = ALProxy("ALTextToSpeech", "192.168.0.102", 9559)
nao1tracker = ALProxy("ALTracker", "192.168.0.102", 9559)
nao1move = ALProxy("ALMotion", "192.168.0.102", 9559)

nao2speech = ALProxy("ALTextToSpeech", "192.168.0.103", 9559)
nao2tracker = ALProxy("ALTracker", "192.168.0.103", 9559)
nao2move = ALProxy("ALMotion", "192.168.0.103", 9559)
nao2sounddetection = ALProxy("ALSoundDetection", "192.168.0.103", 9559)
nao2speechrecognition = ALProxy("ALSpeechRecognition", "192.168.0.103", 9559)
nao2memory = ALProxy("ALMemory", "192.168.0.103", 9559)

nao3speech = ALProxy("ALTextToSpeech", "192.168.0.101", 9559)
nao3tracker = ALProxy("ALTracker", "192.168.0.101", 9559)
nao3move = ALProxy("ALMotion", "192.168.0.101", 9559)

nao4speech = ALProxy("ALTextToSpeech", "192.168.0.105", 9559)
nao4tracker = ALProxy("ALTracker", "192.168.0.105", 9559)
nao4move = ALProxy("ALMotion", "192.168.0.105", 9559)


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



# Robot 1 speaks
nao1speech.say("Hello, it is nice to meet you! My name is Robin and I am a social robot. What is your name?")
time.sleep(2.5)  # Give time for speech to finish and mic to reset

# Set up dummy vocabulary for speech detection
nao2speechrecognition.setLanguage("English")
nao2speechrecognition.setVocabulary(["hello", "my", "name", "is", "I", "am"], False)

time.sleep(1)
nao2speechrecognition.subscribe("SpeechDetector")
time.sleep(0.5)

print("Listening...")


# Listen for 5 seconds
speech_detected = False
start_time = time.time()

while time.time() - start_time < 5:
    data = nao2memory.getData("WordRecognized")
    if data and isinstance(data, list) and len(data) >= 2:
        word, confidence = data[0], data[1]
        print("Detected word:", word, "Confidence:", confidence)
        if confidence > 0.1:  # Adjust as needed
            speech_detected = True
            break
    time.sleep(0.1)

# Unsubscribe from recognition
nao2speechrecognition.unsubscribe("SpeechDetector")

# Response logic
if speech_detected:
    time.sleep(0.5)
    nao2speech.say("It is a pleasure to meet you! I am Chris.")
    time.sleep(0.5)
    nao3speech.say("Hello, my name is Sam.")
    time.sleep(0.5)
    nao4speech.say("And my name is Alex.")
else:
    nao2speech.say("I did not quite hear you, but I am glad you are here!")


# Question 1
vocabulary = ["yes", "no", "nee", "yeah", "nope", "yup", "nah"]
nao2speechrecognition.setVocabulary(vocabulary, False)

nao2speechrecognition.subscribe("Test_ASR")

time.sleep(1.5)
nao2speech.say("Did you manage to find the lab easily?")
print("Waiting for user response...")
time.sleep(0.5)

# Listen to the participant
response = None
for i in range(5):
    data = nao2memory.getData("WordRecognized")
    if data and isinstance(data, list) and len(data) > 1:
        word = data[0]
        confidence = data[1]
        if confidence > 0.1:
            response = word
            print("Recognized:", word, "Confidence:", confidence)
            break
    time.sleep(0.5)

# Unsubscribe
nao2speechrecognition.unsubscribe("Test_ASR")

if response in ["yes", "yeah", "yup"]:
    nao2speech.say("That is good to hear!")
elif response in ["no", "nope", "nee"]:
    nao2speech.say("It can be hard to find the lab, indeed, but luckily you made it.")
else:
    nao2speech.say("I did not quite catch that, but I am glad you're here!")






