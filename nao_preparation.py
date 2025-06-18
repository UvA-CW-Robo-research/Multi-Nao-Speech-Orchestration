# Import all predefined proxies
from nao_setup import *

# Set the posture to sti still
nao1pose.goToPosture("Sit", 1.0)
nao2pose.goToPosture("Sit", 1.0)
nao3pose.goToPosture("Sit", 1.0)
nao4pose.goToPosture("Sit", 1.0)

# Set head stiffness so head can move
nao1move.setStiffnesses("Head", 1.0)
nao2move.setStiffnesses("Head", 1.0)
nao3move.setStiffnesses("Head", 1.0)
nao4move.setStiffnesses("Head", 1.0)


# Turn nao1 and nao3 heads to the left
nao1move.setAngles("HeadYaw", 0.7, 0.2)
nao3move.setAngles("HeadYaw", 0.9, 0.2)

# Turn nao2 and nao4 heads to the right
nao2move.setAngles("HeadYaw", -0.7, 0.2)
nao4move.setAngles("HeadYaw", -0.9, 0.2)
