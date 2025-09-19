## Pre-requisites

1. Nao version 2.8.6.23 uses older python version. Though it does need 64 bit.
2. Go to [Softbank](http://doc.aldebaran.com/2-5/dev/python/index.html) download the python sdk for your operating system. This website is not up-to-date. The instructions on getting the Python SDK are not correct. Go to [aldebaran.com support](https://aldebaran.com/en/support/kb/nao6/downloads/nao6-software-downloads/), create an account log in and you can download the 2.8.6 - Python 2.7 SDK from downloads > SDK. 
3. Python 2.7 is needed.
4. Installation guide is available at [Softbank](http://doc.aldebaran.com/2-5/dev/python/install_guide.html)
5. Install audio player to run the cover story mp3 file

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
- [x] Add the python path permanently to the conda naoqi environment
    - `conda activate naoqi`
    - `export PYTHONPATH=${PYTHONPATH}:~/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327/lib/python2.7/site-packages/`
- [x] Run python 2.7 in naoqi conda environment `python`
- [x] Set naoqi to default environment by [modifying your .bashrc file](https://docs.rc.fas.harvard.edu/kb/editing-your-bashrc/#:~:text=In%20order%20to%20edit%20your,that%20you're%20using%20nano%20.) to contain this line at the bottom of the file:
    - `conda activate naoqi`
- [x] Import NAOqi in python `import naoqi`
- [x] Check if it works `naoqi`
- [x] Setup router tp-link u:admin
- [x] Assign fixed IP's to Nao's
    - nao1: 192.168.0.102
    - nao2: 192.168.0.103
    - nao3: 192.168.0.101
    - nao4: 192.168.0.105
- [x] Develop and run script from mac mini to control Naoqi API
- [x] Install python 2.7 compatible version of the `pandas` package to the mac mini (OFFLINE):
    - Download `pandas-0.24.2-cp27-cp27mu-manylinux1_x86_64.whl` from [pandas.PyPI](https://pypi.org/project/pandas/0.24.2/#files), `numpy-1.16.6-cp27-cp27mu-manylinux1_x86_64.whl` from [numpy.PyPI](https://pypi.org/project/numpy/1.16.6/#files), and `xlrd-1.2.0-py2.py3-none-any.whl` from [xlrd.PyPI](https://pypi.org/project/xlrd/1.2.0/#files) to local laptop. (*Notice*: My laptop is macOS but the python 2.7 environment on mac mini is Linux, so the wheels must also be Linux)
    - Drag the three wheel files to the mac mini directory `~/nao/` on VS Code.
    - Install `pandas` on the mac mini: `cd ~/nao` -> `pip install ./*.whl`.
  
After the summer break, we realize that offline installing new packages to the mac mini requires too much work. Therefore, we would turn on the wifi for the mac mini whenever we need to install some new stuff.

- [ ] Mac mini connected to [IOTroam](iotroam.nl) of Sharon's account (expiration date: 25-09-2025). 
- [ ] Turn on the wifi for mac mini: `sudo nmcli radio wifi on`.
- [ ] Install `vlc` on the mac mini: `sudo`
## Resources
- [ ] [Naoqi APIs](http://doc.aldebaran.com/2-1/naoqi/index.html)
- [ ] [Text to speech tutorial](http://doc.aldebaran.com/2-1/naoqi/audio/altexttospeech-tuto.html)
      - Check the default list of available voices: `print(tts.getAvailableVoices())`
- [ ] Set up [face tracker](http://doc.aldebaran.com/2-1/naoqi/trackers/altracker.html#ready-to-move-robot) with head movement only 
    - Note: some arguments for the used parameters (e.g., `stiffnessInterpolation` and `registerTarget`) are not entirely clear (see the python script).
- [ ] We wanted to add some animations such as blinking while NAO is talking. [animation libirary](http://doc.aldebaran.com/2-5/naoqi/motion/alanimationplayer-advanced.html#animationplayer-list-behaviors-nao)
