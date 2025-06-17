# Load library
from naoqi import ALProxy
import time
import re

nao1speech = ALProxy("ALTextToSpeech", "192.168.0.102", 9559)
nao1tracker = ALProxy("ALTracker", "192.168.0.102", 9559)
nao1move = ALProxy("ALMotion", "192.168.0.102", 9559)
nao1sounddetection = ALProxy("ALSoundDetection", "192.168.0.102", 9559)
nao1speechrecognition = ALProxy("ALSpeechRecognition", "192.168.0.102", 9559)
nao1memory = ALProxy("ALMemory", "192.168.0.102", 9559)

# Robot 1 speaks
nao1speech.say("Hello, it is nice to meet you! My name is Robin and I am a social robot. What is your name?")


# Robot 2 introduces itself after recognizing participant's voice
time.sleep(3) # Wait ... seconds so Robot 2 doesn't recognize Robot 1's voice

nao1sounddetection.setParameter("Sensitivity", 0.6)  # set sensitivity to sound less than default 0.9

nao1sounddetection.subscribe("MySoundDetector")
print("Sound detection starts.")

sound_detected = False
start_time = time.time()

while time.time() - start_time < 5:
    data = nao1memory.getData("SoundDetected")
    if data and len(data) > 0:
        print("Sound detected:", data)
        sound_detected = True
        break
    time.sleep(0.1)

nao1sounddetection.unsubscribe("MySoundDetector")
print("Sound detection stops.")

if sound_detected:
    nao1speech.say("It is a pleasure to meet you! I am Chris.")
else:
    nao1speech.say("I did not really hear your name as your voice was a bit low, but my name is Chris.") # I'm a bit deaf.


# Interaction with Robot 2
time.sleep(1.5)

vocabulary_1 = [
    # Affirmative words
    "yes", "yeah", "yup", "yep", "okay", "ok", "sure", "alright",
    "absolutely", "definitely", "of course", "perhaps", "maybe",
    "right", "fine", "correct", "affirmative",

    # Negative words
    "no", "nee", "nope", "no way", "not really", "never",
    "wrong", "incorrect", "negative", "unfortunately"
]



# Now safely set vocabulary
nao1speechrecognition.setVocabulary(vocabulary_1, True)  # Enable word spotting

# Then subscribe to start recognition
nao1speechrecognition.subscribe("Test_ASR")

time.sleep(1.5)
nao1speech.say("Did you manage to find the lab easily?")
time.sleep(2.5)  # Wait longer before subscribing
nao1speechrecognition.subscribe("Test_ASR")

print("Speech recognition starts.")

response = None
max_checks = 5  # Increase number of checks for responsiveness
check_interval = 0.1  # Check every 0.1 seconds

for _ in range(max_checks):
    data = nao1memory.getData("WordRecognized")
    if data and isinstance(data, list) and len(data) > 1:
        word = data[0].lower()
        confidence = data[1]
        print("Detected word: '{}' with confidence {}".format(word, confidence))
        if confidence > 0.2 and word in vocabulary_1:
            response = word
            break
    time.sleep(check_interval)

nao1speechrecognition.unsubscribe("Test_ASR")
print("Speech recognition Stops.")

if response:
    # Remove all occurrences of <...> and anything inside the brackets
    clean_word = re.sub(r'<.*?>', '', response).strip()
else:
    clean_word = ''

if clean_word in ["yes", "yeah", "yup", "yep", "okay", "ok", "sure", "alright",
                  "absolutely", "definitely", "of course", "affirmative", "right"]:
    nao1speech.say("That is good to hear!")
elif clean_word in ["no", "nee", "nope", "no way", "not really", "never",
                    "wrong", "incorrect", "negative", "unfortunately"]:
    nao1speech.say("It can be hard to find the lab, indeed, but luckily you made it.")
else:
    nao1speech.say("I did not quite catch that, but I am glad you are here!")
