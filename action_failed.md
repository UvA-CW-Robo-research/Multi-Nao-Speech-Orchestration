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

## Archived action plan:
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
    - Test if pynput works: `python -c "from pynput.keyboard import Key, Controller; print('pynput works')"`.
- [ ] Enable X11 forwarding:
    - Download [Quartz](https://www.xquartz.org/) to local macOS.
    - Run `ssh -X nao@naoserver.local` in local terminal -> `sudo nano /etc/ssh/sshd_config` -> find and changes lines to `X11Forwarding yes
X11DisplayOffset 10
X11UseLocalhost yes`
    - Save `Ctrl + O` -> Tap enter key -> exit `Ctrl + X `.
    - Restart the SSH server: `sudo systemctl restart sshd`.
    - Connect with X11 forwarding (enabled): `ssh -X nao@naoserver.local` -> type `yes`

Reason: The scripts use raw_input() for user input and does not simulate or listen for key presses.
