## Guideline for research assistant to set up the experiment
1. Connect all devices (e.g., mac mini, tp-link, researcher laptop, robots).
  - Open terminal in VScodeConnect the experimenter's mac with the tp-link and the mac mini (with an adapter).
  - Setup a VScode ssh connection with the mac mini (only required for the first time):
    - [YouTube crash course](https://www.youtube.com/watch?v=cOopQQIL8JU)
    - Download "Remote - SSH" by Microsoft from the extensions
    - Click the bottom left blue icon to open a remote window
    - Click "Connect to Host..." --> "Configure SSH..." --> select the top config file from users (e.g., /Users/Name/.ssh/config)
    - Ignore the existing texts in the config file and type the following code:
      - <pre> Host naoserver 
          ....HostName naoserver.local 
          ....User nao </pre>
      - The config file will be saved automatically
  - Open terminal in VScode
    - Connect local to host (naoserver)
    - Click "Terminal" in the menu bar and select "New Terminal"
    - type `python` + drag/type the path and then tap the enter key to run the code
2. Set up the robots in the right positions (see figure below). ![robotsetup](https://github.com/UvA-CW-Robo-research/Multi-Nao-Speech-Orchestration/blob/main/robotsetup.jpeg)
3. Run the [preparation script](https://github.com/UvA-CW-Robo-research/Multi-Nao-Speech-Orchestration/blob/main/preparation.py) to make all robots sit in the same posture and look at the participant. 

4. Run the [interaction script]().
5. Play the audio for the cover story.
6. Run the [experiment script]() based on the condition (consistent vs. inconsistent).
7. Turn off all devices before leaving the lab.
  - How to turn off mac mini and tp-link through the terminal?
    - Open terminal on the researcher's laptop.
    - Copy and paste: `ssh nao@naoserver.local`
    - Enter the password (See "usernames and passwords.docx" in Teams)
    - Copy and paste: `sudo shutdown -h now`
    - Enter the same password.
  - How to turn off the robots?
    - Press the button on their chests for a few seconds.
  
## Notice 🔋
- A blinking red light on NAO's chest button signifies that the battery charge is low, and the robot should be charged immediately while turned off.


## Test the robot
- [ ] [Naoqi APIs](http://doc.aldebaran.com/2-1/naoqi/index.html)
- [ ] Set up a virtual NAO robot V6 in the software Choregraphe (version 2.8)
- [ ] [Text to speech tutorial](http://doc.aldebaran.com/2-1/naoqi/audio/altexttospeech-tuto.html)
      - Check the default list of available voices: `print(tts.getAvailableVoices())`

- [ ] Set up [face tracker](http://doc.aldebaran.com/2-1/naoqi/trackers/altracker.html#ready-to-move-robot) with head movement only 
    - Note: some arguments for the used parameters (e.g., `stiffnessInterpolation` and `registerTarget`) are not entirely clear (see the python script).


