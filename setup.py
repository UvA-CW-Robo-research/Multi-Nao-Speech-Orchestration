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

# Run a simple conversation
nao2speech.say("Hello, i am Frieza. Who are you?")
nao4speech.say("I am rock!")
nao2speech.say("Its nice to meet you!")
nao4speech.say("Nice to meet you too! How are you doing?")
nao2speech.say("I'm good! What about you?")
nao4speech.say("I'm doing fine!")
nao2speech.say("Great!")
nao2speech.say("Let me show you something!")
# Make sure the legs can move
nao2move.setStiffnesses("Body", 1.0)
# Go to standing position
nao2move.moveInit()
# Walk forward 0,5 meters and put this into a variable
id = nao2move.post.moveTo(0.5, 0, 0)
nao2speech.say("Look! I'm walking!")
nao4speech.say("Wow!")
# Wait (time = variable we set earlier) until the walking has ended
nao2move.wait(id, 0)
