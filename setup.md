## Pre-requisites

1. Nao version 2.8.6.23 uses older python version. Though it does need 64 bit.
2. Go to [Softbank](http://doc.aldebaran.com/2-5/dev/python/index.html) download the python sdk for your operating system. This website is not up-to-date. The instructions on getting the Python SDK are not correct. Go to [aldebaran.com support](https://aldebaran.com/en/support/kb/nao6/downloads/nao6-software-downloads/), create an account log in and you can download the 2.8.6 - Python 2.7 SDK from downloads > SDK. 
3. Python 2.7 is needed.
4. Installation guide is available at [Softbank](http://doc.aldebaran.com/2-5/dev/python/install_guide.html)

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
- [x] Add the python path permanently to the conda naoqi environment
    - `conda activate naoqi`
    - `export PYTHONPATH=${PYTHONPATH}:~/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327/lib/python2.7/site-packages/`
- [x] Run python 2.7 in naoqi conda environment `python`
- [x] set naoqi to default environment
- [x] Import NAOqi in python `import naoqi`
- [x] Check if it works `naoqi`
- [x] Setup router tp-link u:admin
- [x] Assign fixed IP's to Nao's
    - nao1: 192.168.0.102
    - nao2: 192.168.0.103
    - nao3: 192.168.0.101
    - nao4: 192.168.0.105
- [x] Develop and run script from mac mini to control Naoqi API
- [ ] Connect the experimenter's mac with the tp-link and the mac mini (with an adapter)
- [ ] Setup a VScode ssh connection with the mac mini
    - [YouTube crash course](https://www.youtube.com/watch?v=cOopQQIL8JU)
    - Download "Remote - SSH" by Microsoft from the extensions
    - Click the bottom left blue icon to open a remote window
    - Click "Connect to Host..." --> "Configure SSH..." --> select the top config file from users (e.g., /Users/Name/.ssh/config)
    - Ignore the existing texts in the config file and type the following code:
      - <pre> Host naoserver 
          ....HostName naoserver.local 
          ....User nao </pre>
      - The config file will be saved automatically
- [ ] Open terminal in VScode
    - Connect local to host (naoserver)
    - Click "Terminal" in the menu bar and select "New Terminal"
    - type `python` + drag/type the path and then tap the enter key to run the code
- [ ] Turn off mac mini through researcher's terminal
    - `ssh nao@naoserver.local`
    - See password from "usernames and passwords.docx" in Teams
    - `sudo shutdown -h now`

## Test the robot
- [ ] [Naoqi APIs](http://doc.aldebaran.com/2-1/naoqi/index.html)
- [ ] Set up a virtual NAO robot V6 in the software Choregraphe (version 2.8)
- [ ] [Text to speech tutorial](http://doc.aldebaran.com/2-1/naoqi/audio/altexttospeech-tuto.html)
      - Check the default list of available voices: `print(tts.getAvailableVoices())`

- [ ] Set up [face tracker](http://doc.aldebaran.com/2-1/naoqi/trackers/altracker.html#ready-to-move-robot) with head movement only 
    - Note: some arguments for the used parameters (e.g., `stiffnessInterpolation` and `registerTarget`) are not entirely clear (see the python script).

## Guideline for setting up the experiment
1. Connect all equipments (e.g., mac mini, tp-link, researcher laptop, robots).
2. Run the [preparation script](https://github.com/UvA-CW-Robo-research/Multi-Nao-Speech-Orchestration/blob/main/preparation.py) to make all robots sit in the same posture and look at the participant.
3. Set up the robots in the right positions (see figure below). ![robotsetup](https://github.com/UvA-CW-Robo-research/Multi-Nao-Speech-Orchestration/blob/main/robotsetup.jpeg)

4. Run the interaction script.
5. Play the audio for the cover story.
6. Run the experiment script.

## Notice 🔋
- A blinking red light on NAO's chest button signifies that the battery charge is low, and the robot should be charged immediately while turned off.
