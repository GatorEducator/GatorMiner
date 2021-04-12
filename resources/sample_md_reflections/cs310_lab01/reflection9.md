# Report by

## Planning, due on January 27th, 2020 by 11am

### Timeline

| Timeline | Tasks                                            |
| -------- | ------------------------------------------------ |
| 1/24     | Identify task and resources                      |
| 1/28     | Get some sort of example code working on a board |
| 1/31     | Get basic code working                           |
| 2/7      | Have enhancement code working                    |

### Hardware

- Arduino board
- IR Sensor
- LED
- Speaker
- Battery pack (for portability but not necessary)

## Arduino Project

The project we are attempting to do is to use an IR sensor to detect somebody
passing by the Arduino and then having it minimize whatever computer tab is up.
We will expand on this to have it open different applications based on other
movement instead of just closing.

The motivation for this is that it could be helpful in protecting private
information that is being worked on. Or more
unethically, could be used for people who are procrastinating on their work.

Our code will be based on the
<https://www.hackster.io/najad/tripwire-automatically-minimizes-tabs-when-someone-walks-by-ae113f>

FOLLOW UP: We could not complete this idea for our lab due to the board being
incompatible. Instead, we decided to make a small alarm system by using a
speaker and LED that go off when the IR sensor is triggered.

INSTRUCTIONS: To run this program, you need to connect the IR sensor, the LED,
and the buzzer to the board. Then you plug the board into the computer, load
the code into the Arduino IDE, select the port for the board, then verify and
upload.

The four connections for the IR are as follows:
Any ANALOG IN (UNO) to POWER (IR), Digital 8 (UNO) to DO (IR), GND (UNO) to GND
(IR), and 5V (UNO) to VCC (IR).

The two connections for the buzzer:
Plug one Connection to Digital 9 (UNO) and the other to a GND (UNO)

The LED should be plugged into Digital 13 and the GND above it on the green part
of the board.

The picture below shows you how to set up your IR sensor.
![IR Sensor Setup](mh_sesnor_series_bb.jpg)

The pictures below is how our board and sensors were set up although it is a bit
hard to see.
![Board Setup1](20200207_145551.jpg)
![Board Setup2](20200207_152002.jpg)

## Agent

Explain the characteristics/attributes of your agent, what makes it an agent
(within the discussed course content), what makes it rational, what type of an
agent it is, and what is its environment task (PEAS).

Our agent is based on 3 key parts: The LED, speaker, and the IR sensor. The LED
and speaker both act if the IR sensor is triggered (something blocks the light).
This is considered an agent because it acts in its environment by blinking the
LED and sounding the speaker when its environment changes
(the IR sensor is blocked). This agent is rational because it has a logic that
if the light is blocked, then it activates the responses in the environment.
This agent is autonomous and reflexive.

Environment Task:

Performance measure: Alerting the user

Environment: The room its in, objects in the room, how close it is to things

Actuators: LED, Speaker

Sensors: IR sensor

## Challenges and Learning Experiences

Discuss any challenges you have encountered during the work on this lab and
describe what have you learned.

There were a multitude of challenges for this lab that we faced. The first one
stemmed from neither of us knowing how to use an Arduino. This resulted in us
having to learn about the different ports on the Arduino and how to compile and
run code it. This leads us to our next challenge, the Arduino IDE. This IDE gave
us a lot of issues, from not working on Linux at first (until a reinstall and
troubleshooting) to errors from trying to upload the program to the Arduino.
We have since figured out how to deal with the little issues that still pop up
(not finding the right port). Our main challenge however came from the fact that
we could not proceed with our original idea of minimizing applications. This was
due to the fact that the Uno board cannot be used as a keyboard and interact
backwards with a computer. The only solution to this was to either order an
entirely new type of board or to change our project. We ended up changing the
project to be something simpler and possible to be done with our board.

## Ethical Benefits and Implications

In this section, drawing on class discussions and readings, answer the following
questions

1. What entities, businesses, organizations do you envision developing the type
    of the application you have chosen to develop?

We envision organizations such as banks, federal reserve, and research
facilities developing and using security systems similar to ours. Having an
infrared sensor in a security system can be very beneficial. Infrared sensors
can measure heat been emitted by an object and detect motion. Depending on the
infrared sensor's capabilities, it can detect heat from a human body. An alarm
system like ours can help enhance security systems and make it harder for
anyone to attempt any break-ins to unauthorized areas.

2. Who are the intended users of this technology?

From small to large businesses, homeowners, banks, and corporations are the
intended users of this technology.

3. Who is not supposed to use this technology?

Anyone that does not need to secure a place or business does not need this
technology. It's ideal to use a security system like ours if you are trying to
secure a home or business.

4. How can the application developed in this lab cause harm?

The application that we developed in the lab can't cause any harm unless we
create a highly concentrated infrared sensor into a narrow beam. The audio
system is not loud enough to cause damage to the human ear. Our application
is safe for anyone to use.

5. What solutions could be implemented to avoid the harm or to fix the harm
    described above?

As stated in question four, our application does not cause any harm; therefore
it is not necessary to implement any solutions.

## Team Work

Describe the details of your team working strategy, specifically explain how did
you complete this work as a team and describe the specific contributions of each
team member.

 X did must of the
implementation of the source code since, and Y focused on the hardware part of
the lab. This strategy worked out because we had to identify sections in our
Arduino board to specify in our source code for our speaker, infrared sensor,
and led light to work correctly. When it came to debugging our source code and
fixing errors, we worked together to figured our issues and find solutions. We
think we did a great job in terms of scheduling meetings, distributing the work,
and overall communicating well.
