# Import all predefined proxies
from nao_setup import *

# Set the posture to sit still
# 1.0 is the speed of the movement (range: 0.0 to 1.0, where 1.0 is fastest)
nao1pose.goToPosture("Sit", 1.0)
nao2pose.goToPosture("Sit", 1.0)
nao3pose.goToPosture("Sit", 1.0)
nao4pose.goToPosture("Sit", 1.0)

# Set head stiffness to max (1.0) so motors hold position and head can move precisely
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
