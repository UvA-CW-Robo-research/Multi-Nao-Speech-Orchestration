---
title: "Multi Nao Speech Orchestration"
subtitle: "Setup"
output: html_document
---

Pre-requisites

1. Nao version 2.8.6.23 uses older python version. Though it does need 64 bit.
2. Go to [Softbank](http://doc.aldebaran.com/2-5/dev/python/index.html) download the python sdk for your operating system. This website is not up-to-date. The instructions on getting the Python SDK are not correct. Go to [aldebaran.com support](https://aldebaran.com/en/support/kb/nao6/downloads/nao6-software-downloads/), create an account log in and you can download the 2.8.6 - Python 2.7 SDK from downloads > SDK. 
3. Python 2.7 is needed.
4. Installation guide is available at [Softbank](http://doc.aldebaran.com/2-5/dev/python/install_guide.html)

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

## New action plan

The Nao Python SDK only works on x86 64Bit architecture and not on ARM 64Bit. This means that the software does not run on raspberry pi.

The new plan is to use an old x86 mac mini, install ubuntu linux on it and run the software from there. As the latest Ubuntu distro comes with Pyhton 3.x pre installed, we plan to install anaconda to also make a 2.7 python environment available.

- [x] Install [Ubuntu 24.04.2 LTS](https://ubuntu.com/blog/ubuntu-desktop-24-04-noble-numbat-deep-dive) on mac mini `naoserver.local`
- [x] [Install SSH](https://www.cyberciti.biz/faq/how-to-install-ssh-on-ubuntu-linux-using-apt-get/)
- [x] [Enable remote desktop](https://help.ubuntu.com/stable/ubuntu-help/sharing-desktop.html.ro)
- [x] [Install anaconda](https://linuxconfig.org/installing-anaconda-on-ubuntu-24-04)
- [x] Add python 2.7 environment to anaconda `conda create --name naoqi python=2.7`
- [x] Enable naoqi environment `conda activate naoqi`
- [x] Install NAOqi Python SDK, download [2.8.6 - Python 2.7 SDK](https://aldebaran.com/en/support/kb/nao6/downloads/nao6-software-downloads/). 
- [x] Exctract tar.gz to directory `cd home/nao/` extract file there `tar -xvzf pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327.tar.gz`
- [x] Add SDK to python path `export PYTHONPATH=${PYTHONPATH}:~/nao/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327/lib/python2.7/site-packages`
- [x] Make path permanent (improve)
- [x] Run python 2.7 in naoqi conda environment `python`
- [x] set naoqi to default environment
- [x] Import NAOqi in python `import naoqi`
- [x] Check if it works `noaqi`
- [x] Setup router tp-link u:admin
- [x] Assign fixed IP's to Nao's
    - nao1: 192.168.0.102
    - nao2: 192.168.0.103
    - nao3: 192.168.0.101
    - nao4: 192.168.0.105
- [x] Develop and run script from mac mini to control Naoqi API

