# Report by

## Planning, due on January 27th, 2020 by 11am

### Timeline

| Timeline  | Tasks |
| ----------- | ----------- |
| 1/24/20    |    Finalize project and complete timeline   |
| 1/27/20 | Acquire materials |
| 1/29/20 | Assemble hardware and produce sound |
| 1/30/20  | Test sound and produce lights: prep for walkthrough |
| 1/31/20   | Lab session |
| 1/5/20    | Ensure agent reacts to environment|
| 2/7/20    | Complete project |

### Hardware

- Arduino board
- UNO R3
- Breadboard
- Jumper cables
- [SparkFun Mini Speaker - PC Mount 12mmm 2.048kHz](sparkfun.com/products/7950)
- Red and Green LEDs
- Buttons
- Buzzer

## Arduino Project

We chose to model our lab after this project we found on
[Hackster](https://www.hackster.io/techarea98/super-mario-theme-song-with-piezo-buzzer-and-arduino-2cc461).
This project simply connects a buzzer to an arduino, allowing it to play a song.
We added two features to this project. TO make it responsive to its environment,
we added a button that allows a user to control when and what song is played
through the buzzer. We also added an LED light to indicate when the song is being
played.

## Agent

Our agent is a simple reflex agent that contains two states, when the button is
high (not pressed) and when the button is low (pressed).

We feel the agent exists in a fully observable, episodic, static environment.
The only component of the agent's environment is the button.
No data builds when the agent takes action, therefore making it episodic.
Nothing in the environment changes besides the state of the button.

The actuators related to our agent are the buzzer and the light that
take action when the button is pressed.

The sensor for our agent is the button which detects whether action is taken
or not.

## Challenges and Learning Experiences

Discuss any challenges you have encountered during the work on
this lab and  describe what have you learned.

We were at first challenged by the basic set up of a the
arduino and the breadboard.
After watching tutorials and reading documentation,
we gained more confidence in
what to do.
Our next challenge involved using a speaker. We attempted to add a speaker to
the agent, however we struggled to understand how to connect the speaker with a
resistor and chose to
stick with the buzzer.
Another challenge we had was having to transpose the sheet music
for The Office theme song, which was very time consuming. Overall, we had few
challenges while completing this lab.

## Ethical Benefits and Implications

In this section, drawing on class discussions and readings,
answer the following questions

We envision this being used for entertainment purposes.
The LEDs lighting up when the sound is being played
could also be used as an assistive technology for those
who are hearing impaired.

The intended users would likely be children or collectors.

This is an innocent technology that honestly does not have any ethical concerns as
it just plays a song. We don't see a reason to bar
anyone from using it. However, anyone with mal intent could find a way to
use this inappropriately.

If the volume was set to a very high level and would not stop it could cause
physical harm to those in the space in which it goes off.

By including a resistor, we could limit the flow of power that would prevent
the volume from getting too loud.

## Team Work

Describe the details of your team working strategy, specifically explain
how did you complete this work as a team and describe the specific
contributions of each team member.

We met many times as a team to work on this assignment together. We each had ideas
that we brainstormed and merged to create this agent. We both did research when we
got stuck on a task and both worked with both the physical and coding parts of the
project.
