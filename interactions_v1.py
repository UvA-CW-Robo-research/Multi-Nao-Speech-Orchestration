# Load library
from naoqi import ALProxy
import time

### Create a new file and code for the modules' setup

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


# Robot 2 introduces itself after recognizing participant's voice
time.sleep(1.5) # Wait 1.5 seconds so Robot 2 doesn't recognize Robot 1's voice



nao2sounddetection.setParameter("Sensitivity", 0.5)  # set sensitivity to sound less than default 0.9


sound_detector.subscribe("MySoundDetector")
print("Sound detection starts.")

sound_detected = False
start_time = time.time()

while time.time() - start_time < 5:
    data = nao2memory.getData("SoundDetected")
    if data and len(data) > 0:
        print("Sound detected:", data)
        sound_detected = True
        break
    time.sleep(0.1)

sound_detector.unsubscribe("MySoundDetector")
print("Sound detection stops.")


if sound_detected:
    print("It is a pleasure to meet you! I am Chris.")
else:
    print("I did not really hear your name as your voice was a bit low, but my name is Chris.") # I'm a bit deaf.


# Robot 3 speaks
time.sleep(0.5)
nao3speech.say("Hello, my name is Sam.")

# Robot 4 speaks
time.sleep(0.5)
nao4speech.say("And my name is Alex.")



# Interaction with Robot 2
time.sleep(1.5)

vocabulary_1 = [
    # Affirmative words
    "yes", "yeah", "yup", "yep", "okay", "ok", "sure", "alright",
    "absolutely", "definitely", "of course", "perhaps", "maybe",
    "right", "fine", "correct", "affirmative",

    # Negative words
    "no", "nee", "nope", "nah", "no way", "not really", "never",
    "wrong", "incorrect", "negative", "unfortunately"
]

nao2speechrecognition.setVocabulary(vocabulary_1, True) # Enable word spotting

nao2speech.say("Did you manage to find the lab easily?")


nao2speechrecognition.subscribe("Test_ASR") 
print("Speech recognition starts.")

response = None
max_checks = 5  # Increase number of checks for responsiveness
check_interval = 0.1  # Check every 0.1 seconds

for _ in range(max_checks):
    data = nao2memory.getData("WordRecognized")
    if data and isinstance(data, list) and len(data) > 1:
        word = data[0].lower()
        confidence = data[1]
        print(f"Detected word: '{word}' with confidence {confidence}")
        if confidence > 0.2 and word in vocabulary_1:
            response = word
            break
    time.sleep(check_interval)

nao2speechrecognition.unsubscribe("Test_ASR")
print("Speech recognition Stops.")


if response in ["yes", "yeah", "yup", "yep", "okay", "ok", "sure", "alright",
                "absolutely", "definitely", "of course", "affirmative"]:
    nao2speech.say("That is good to hear!")
elif response in ["no", "nee", "nope", "nah", "no way", "not really", "never",
                  "wrong", "incorrect", "negative", "unfortunately"]:
    nao2speech.say("It can be hard to find the lab, indeed, but luckily you made it.")
else:
    nao2speech.say("I did not quite catch that, but I am glad you are here!")






