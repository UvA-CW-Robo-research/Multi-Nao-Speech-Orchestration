# Load library
from naoqi import ALProxy

# Define the IP address of each NAO robot
nao1_ip = "192.168.0.102"  
nao2_ip = "192.168.0.103"
nao3_ip = "192.168.0.101"  
nao4_ip = "192.168.0.105"  

# Define the port number used to connect to NAOqi on each robot
# NAOqi is the central software system that lets you control and communicate with NAO.
port = 9559

# Initialize proxies for NAO1
nao1speech = ALProxy("ALTextToSpeech", nao1_ip, port)
nao1tracker = ALProxy("ALTracker", nao1_ip, port)
nao1move = ALProxy("ALMotion", nao1_ip, port)
nao1pose = ALProxy("ALRobotPosture", nao1_ip, port)

# Initialize proxies for NAO2
nao2speech = ALProxy("ALTextToSpeech", nao2_ip, port)
nao2tracker = ALProxy("ALTracker", nao2_ip, port)
nao2move = ALProxy("ALMotion", nao2_ip, port)
nao2pose = ALProxy("ALRobotPosture", nao2_ip, port)

# Initialize proxies for NAO3
nao3speech = ALProxy("ALTextToSpeech", nao3_ip, port)
nao3tracker = ALProxy("ALTracker", nao3_ip, port)
nao3move = ALProxy("ALMotion", nao3_ip, port)
nao3pose = ALProxy("ALRobotPosture", nao3_ip, port)

# Initialize proxies for NAO4
nao4speech = ALProxy("ALTextToSpeech", nao4_ip, port)
nao4tracker = ALProxy("ALTracker", nao4_ip, port)
nao4move = ALProxy("ALMotion", nao4_ip, port)
nao4pose = ALProxy("ALRobotPosture", nao4_ip, port)

