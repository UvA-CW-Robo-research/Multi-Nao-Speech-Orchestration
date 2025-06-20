# Load library
from naoqi import ALProxy

nao1_ip = "192.168.0.102"  
port = 9559

nao1speech = ALProxy("ALTextToSpeech", nao1_ip, port) 
nao1tracker = ALProxy("ALTracker", nao1_ip, port) 
nao1move = ALProxy("ALMotion", nao1_ip, port) 
nao1pose = ALProxy("ALRobotPosture", nao1_ip, port) 


