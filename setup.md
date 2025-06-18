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
- [ ] Manually install pynput 1.5.2 on mac mini
    - Download [pynput 1.5.2](https://files.pythonhosted.org/packages/source/p/pynput/pynput-1.5.2.tar.gz) and [python-xlib wheel for Python 2.7](https://pypi.org/project/python-xlib/#files) to local desktop.
    - Build wheel files through local terminal: `cd ~/Desktop` -> `tar -xvzf pynput-1.5.2.tar.gz` -> `cd pynput-1.5.2` -> `pip wheel . --wheel-dir=wheelhouse`.
    - Drap `python_xlib-0.33-py2.py3-none-any.whl` and`pynput-1.5.2-py2.py3-none-any.whl`, `six-1.17.0-py2.py3-none-any.whl`, `enum34-1.1.10-py2-none-any.whl` from the wheelhouse folder to directory `~/nao/`.
    - Install the packages offline on mac mini: `conda activate naoqi` -> `cd ~/nao` -> `pip install ./*.whl`.
- [ ] Because mac mini is offline and the pynput package is dependent on the xlib package, which is not supported by python 2.7, to fix this issue:
    - You need to manually disable `Xlib.display.Display()`through the following steps
    - `find $CONDA_PREFIX/lib -path "*pynput/_util/xorg.py"` -> `nano /home/nao/anaconda3/envs/naoqi/lib/python2.7/site-packages/pynput/_util/xorg.py` -> replace `def _check():
    display = Xlib.display.Display()
    display.close()
_check()
del _check` with `def _check():
    pass`
    - Save `Ctrl + O` -> Tap enter key -> exit `Ctrl + X `.
    - Test if pynput works: `python -c "from pynput.keyboard import Key, Controller, Listener; print('pynput works')"`.



## Test the robot
- [ ] [Naoqi APIs](http://doc.aldebaran.com/2-1/naoqi/index.html)
- [ ] Set up a virtual NAO robot V6 in the software Choregraphe (version 2.8)
- [ ] [Text to speech tutorial](http://doc.aldebaran.com/2-1/naoqi/audio/altexttospeech-tuto.html)
      - Check the default list of available voices: `print(tts.getAvailableVoices())`

- [ ] Set up [face tracker](http://doc.aldebaran.com/2-1/naoqi/trackers/altracker.html#ready-to-move-robot) with head movement only 
    - Note: some arguments for the used parameters (e.g., `stiffnessInterpolation` and `registerTarget`) are not entirely clear (see the python script).
