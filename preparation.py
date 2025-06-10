# Load library
from naoqi import ALProxy

# Configure robot's movement and speech
nao1pose = ALProxy("ALRobotPosture", "192.168.0.102", 9559)
nao2pose = ALProxy("ALRobotPosture", "192.168.0.103", 9559)
nao3pose = ALProxy("ALRobotPosture", "192.168.0.101", 9559)
nao4pose = ALProxy("ALRobotPosture", "192.168.0.105", 9559)

# Set the posture
nao1pose.goToPosture("Sit", 1.0)
nao2pose.goToPosture("Sit", 1.0)
nao3pose.goToPosture("Sit", 1.0)
nao4pose.goToPosture("Sit", 1.0)
