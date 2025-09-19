# Import all predefined proxies from the self-defined file 
from nao_preparation import *


# Greetings from all four robots
say_with_blinking(nao1speech, nao1leds, "Hello, my name is Robin and I am a social robot. What is your name?")
ra_action1 = raw_input("Press 'Enter' when participant finishes speaking.")
say_with_blinking(nao1speech, nao1leds, "It is a pleasure to meet you.")
time.sleep(1.5)

say_with_blinking(nao2speech, nao2leds, "Hi, and I am Chris. Nice to meet you.")
time.sleep(1.5)

say_with_blinking(nao3speech, nao3leds, "Hello, my name is Sam. It is great meeting you!")
time.sleep(1.5)

say_with_blinking(nao4speech, nao4leds, "Hi there, I am Alex. Nice to meet you!")
time.sleep(2.5)


# Question 1 from Chris
say_with_blinking(nao2speech, nao2leds, "Some people struggled to find the lab. Did you manage to find the lab easily?")
ra_action2 = raw_input("Press 'f' (YES) or 'j' (NO), then 'Enter': ").lower()
if ra_action2 == 'f':
    say_with_blinking(nao2speech, nao2leds, "That's good to hear!")
elif ra_action2 == 'j':
    say_with_blinking(nao2speech, nao2leds, "It can be hard to find the lab, indeed, but luckily you made it.")
    

# Question 2 from Alex
time.sleep(1.5)
say_with_blinking(nao4speech, nao4leds, "Most people who participate in experiments in this lab are students. Are you currently a student?")
ra_action3 = raw_input("Press 'f' (YES) or 'j' (NO), then 'Enter': ").lower()
if ra_action3 == 'f':
    say_with_blinking(nao4speech, nao4leds, "Alright, and what are you studying now? Could you tell me more about it?")
elif ra_action3 == 'j':
    say_with_blinking(nao4speech, nao4leds, "And what do you currently do?")

ra_action4 = raw_input("Press 'Enter' when participant finishes speaking.")
say_with_blinking(nao4speech, nao4leds, "Thanks for letting me know.")

# Question 3 from Sam
time.sleep(1.5)
say_with_blinking(nao3speech, nao3leds, "People do a lot of different things in their free time. What do you do in your free time?")
ra_action5 = raw_input("Press 'f' (activity MENTIONED) or 'j' (Do NOT know), then 'Enter': ").lower()
if ra_action5 == 'f':
    say_with_blinking(nao3speech, nao3leds, "I see. That sounds very interesting!")
elif ra_action5 == 'j':
    say_with_blinking(nao3speech, nao3leds, "I see. That is alright. Perhaps you will discover a new hobby in the future.")


# Question 4 from Robin
time.sleep(1.5)
say_with_blinking(nao1speech, nao1leds, "It is really nice that you came over for the experiment today. Do you frequently participate in experiments?")
ra_action6 = raw_input("Press 'f' (YES) or 'j' (NO), then 'Enter': ").lower()
if ra_action6 == 'f':
    say_with_blinking(nao1speech, nao1leds, "That is great!")
elif ra_action6 == 'j':
    say_with_blinking(nao1speech, nao1leds, "It is great that you will participate today!")
