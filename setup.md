---
title: "Multi Nao Speech Orchestration"
subtitle: "Setup"
output: html_document
---

Pre-requisites

1. Nao version 2.8.6.23 uses older python version.
2. Go to [Softbank](http://doc.aldebaran.com/2-5/dev/python/index.html) download the python sdk for your operating system. This website is not up-to-date. The instructions on getting the Python SDK are not correct. Go to [aldebaran.com support](https://aldebaran.com/en/support/kb/nao6/downloads/nao6-software-downloads/), create an account log in and you can download the 2.8.6 - Python 2.7 SDK from downloads > SDK. 
3. Python 2.7 is needed.
4. Installation guide is available at [Softbank](http://doc.aldebaran.com/2-5/dev/python/install_guide.html)

## Action plan

Setup raspberry pi with python 2.7 for running the Naoqi SDK. Use older version of rasbian to ensure Python 2.7 is available as default. Using this approach ensures that the Naoqi SDK can always be run on the raspberry pi, experimenters can use their own computer to connect to the raspberry pi and control the Nao's, without the need to install older versions of python and the Naoqi SDK locally. 

Further more, the raspberry pi and the Nao's can be connected to the router, making the setup portable and easy to use in the lab setting. The rasbian image can also be cloned and backed-up.

1. Develop and run script from rapberry pi to control Naoqi API.
2. SSH into raspberry pi from vscode using the remote ssh extension.
3. Run script from raspberry pi in lab setting to controll Noa's
4. Connect Nao's and raspberry pi to the router.
5. Set Nao's IP address in router to be fixed.
6. Have experimenters connect to the router and connect to raspberry pi to control Nao's.

To do: 

- [x] Install raspbian [2020-02-13-raspbian-buster.zip](https://downloads.raspberrypi.org/raspbian/images/raspbian-2020-02-14/) on raspberry pi 3 B+
- [x] Ensure SSH access to raspberry pi: `ssh nao@naoserver.local`
- [ ] Install Naoqi SDK on raspberry pi
- [ ] Develop and run script from raspberry pi to control Naoqi API
- [ ] Setup network with Nao's and raspberry pi
