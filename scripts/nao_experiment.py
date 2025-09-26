from nao_setup import *


# Ask user which version of the conversation to use
version = raw_input("Press 'f' (CONSISTENT) or 'j' (INCONSISTENT), then 'Enter': ").lower()

if version == 'f':
    version_file = 'consistent.xlsx'
    print("You selected the CONSISTENT version.")
else:
    version_file = 'inconsistent.xlsx'
    print("You selected the INCONSISTENT version.")

# Play the audio mp3 file with the cover story using the os library
raw_input("Press 'Enter' to play the audio cover story")
os.system("vlc --play-and-exit ./cover_story.mp3")

# Wait for user confirmation before starting the robots
raw_input("Press 'Enter' to make the robots start talking...")

# We use an excel file for all the things the robots should say for a more easy way of configuring the conversation
# With the script below we loop through each row of the excel file

# Load script from the selected file
df = pd.read_excel(version_file)

# Speak each line of text with the corresponding robot
for _, row in df.iterrows():
    # Check if the 'text' cell is not empty or NaN
    if pd.notnull(row['text']):
        # Find the robot dict matching the current row's robot_id
        robot = next(r for r in robots if r['id'] == row['robot_id'])
        # Convert text to string and send it to the robot's speech engine
        say_with_blinking(robot['speech'], robot['leds'], str(row['text']))
        # Pause after each speech (the code runs if the column time has a value)
        if pd.notnull(row['time']):
            print("Wait for {} seconds".format(row['time']))
            time.sleep(float(row['time']))


