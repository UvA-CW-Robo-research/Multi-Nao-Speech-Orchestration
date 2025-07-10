# Guideline for research assistant to set up the experiment

## Prerequisite
  - Setup a VScode ssh connection with the mac mini (only required for the first time):
    - [YouTube crash course](https://www.youtube.com/watch?v=cOopQQIL8JU)
    - Download VScode to the local device.
    - Download "Remote - SSH" by Microsoft from the extensions
    - Click the bottom left blue icon to open a remote window
    - Click "Connect to Host..." --> "Configure SSH..." --> select the top config file from users (e.g., /Users/Name/.ssh/config)
    - Ignore the existing texts in the config file and type the following code:
      - <pre> Host naoserver 
          ....HostName naoserver.local 
          ....User nao </pre>
      - The config file will be saved automatically

## 1. Connect all devices (e.g., mac mini, tp-link, researcher laptop, robots).
  - Connect the robots to sockets with adapters, and do NOT activate them YET.
  - Connect the experimenter's mac with the tp-link and the mac mini (with an adapter).
  - Open the VScode -> click the bottom left blue icon to open a remote window -> click "Connect to Host..." -> click "naoserver" -> enter password (See "usernames and passwords.docx" in Teams).
  - Activate the robots by pressing the button on their breast.
  - Open the script in VScode (See order in the following steps).
    - Click "Terminal" in the menu bar and select "New Terminal".
    - Type `python` + drag/type the path and then tap the "Enter" key to run the code.
  
## 2. Set up the robots in the right positions (in a circle with the participant on the floor).
![robotsetup](https://github.com/UvA-CW-Robo-research/Multi-Nao-Speech-Orchestration/blob/main/robotsetup.jpeg)

## 3. Run the [preparation script](https://github.com/UvA-CW-Robo-research/Multi-Nao-Speech-Orchestration/blob/main/nao_preparation.py) to make all robots sit in the same posture and look at the participant.

## 4. Run the [interaction script](https://github.com/UvA-CW-Robo-research/Multi-Nao-Speech-Orchestration/blob/main/nao_interactions.py).
- Press 'f' on keyboard AND then hit 'Enter' when the participant response is YES.
- Press 'j' on keyboard AND then hit 'Enter' when the participant response is NO.
- See further instructions in the script.
  
## 5. Play the audio for the cover story.

## 6. Run the [experiment script](https://github.com/UvA-CW-Robo-research/Multi-Nao-Speech-Orchestration/blob/main/nao_experiment.py).
- Press 'f' on keyboard AND then hit 'Enter'for CONSISTENT version
- Press 'j' on keyboard AND then hit 'Enter' for INCONSISTENT version

## 7. Turn off all devices before leaving the lab.
  - How to turn off mac mini and tp-link through the terminal?
    - Open terminal on the researcher's laptop.
    - Copy and paste: `ssh nao@naoserver.local`
    - Enter the password (See "usernames and passwords.docx" in Teams)
    - Copy and paste: `sudo shutdown -h now`
    - Enter the same password.
  - How to turn off the robots?
    - Press the button on their chests for a few seconds.
  
## Notice
- When the script is running, please do NOT type anything in the terminal unless an instruction shows up.
- If the terminal shows the "nao ip" is disconnected after running the script, REPEAT the following action till the code is running: *Type `python` + drag/type the path and then tap the "Enter" key to run the code*.
- A blinking red light on NAO's chest button signifies that the battery charge is low, and the robot should be charged immediately *while turned off*.




