## Action plan FAILED

Setup raspberry pi with python 2.7 for running the Naoqi SDK. Use older version of rasbian to ensure Python 2.7 is available as default. Using this approach ensures that the Naoqi SDK can always be run on the raspberry pi, experimenters can use their own computer to connect to the raspberry pi and control the Nao's, without the need to install older versions of python and the Naoqi SDK locally. 

Issue: This version of python runs at 32 bit

Further more, the raspberry pi and the Nao's can be connected to the router, making the setup portable and easy to use in the lab setting. The rasbian image can also be cloned and backed-up.

1. Develop and run script from rapberry pi to control Naoqi API.
2. SSH into raspberry pi from vscode using the remote ssh extension.
3. Run script from raspberry pi in lab setting to controll Noa's
4. Connect Nao's and raspberry pi to the router.
5. Set Nao's IP address in router to be fixed.
6. Have experimenters connect to the router and connect to raspberry pi to control Nao's.

To do: 

- [x] Install raspberry OS [2020-08-20-rspios-buster-arm64-lite.zip](https://downloads.raspberrypi.com/raspios_lite_arm64/images/raspios_lite_arm64-2020-08-24/) on raspberry pi 3 B+ (comes with python 2.7.16)
- [x] Ensure SSH access to raspberry pi: `ssh nao@naoserver.local`
- [x] Install Naoqi SDK on raspberry pi: Giving error on pythen bit version
- [ ] Develop and run script from raspberry pi to control Naoqi API
- [ ] Setup network with Nao's and raspberry pi
