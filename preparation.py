# Load library
from naoqi import ALProxy

# Configure robot's motion and posture
nao1move = ALProxy("ALMotion", "192.168.0.102", 9559)
nao2move = ALProxy("ALMotion", "192.168.0.103", 9559)
nao3move = ALProxy("ALMotion", "192.168.0.101", 9559)
nao4move = ALProxy("ALMotion", "192.168.0.105", 9559)

nao1pose = ALProxy("ALRobotPosture", "192.168.0.102", 9559)
nao2pose = ALProxy("ALRobotPosture", "192.168.0.103", 9559)
nao3pose = ALProxy("ALRobotPosture", "192.168.0.101", 9559)
nao4pose = ALProxy("ALRobotPosture", "192.168.0.105", 9559)

# Set the posture to sti still
nao1pose.goToPosture("Sit", 1.0)
nao2pose.goToPosture("Sit", 1.0)
nao3pose.goToPosture("Sit", 1.0)
nao4pose.goToPosture("Sit", 1.0)

# Set head stiffness so head can move
nao1move.setStiffnesses("Head", 1.0)
nao2move.setStiffnesses("Head", 1.0)
#nao3move.setStiffnesses("Head", 1.0)
nao4move.setStiffnesses("Head", 1.0)


# Turn nao1 and nao3 heads to the left
nao1move.setAngles("HeadYaw", 0.7, 0.2)
nao3move.setAngles("HeadYaw", 0.9, 0.2)

# Turn nao2 and nao4 heads to the right
nao2move.setAngles("HeadYaw", -0.7, 0.2)
nao4move.setAngles("HeadYaw", -0.9, 0.2)
