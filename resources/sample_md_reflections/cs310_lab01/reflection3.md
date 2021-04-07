# Report by

## Planning, due on January 27th, 2020 by 11am

### Timeline

| Timeline  | Tasks |
| ----------- | ----------- |
|   January 27, 2020   |   Specify hardware components   |
|   January 31, 2020   |   Project walkthrough   |
|   February 7, 2020   |   Complete Arduino project and technical writing   |

### Hardware

- Arduino board Uno
- Breadboard
- Arduino buzzer
- Led lights
- Resistors
- Male/Male jumper wires
- PIR sensor
- Image of all parts assembled:
  ![](assets/report-3d781781.png)

## Arduino Project

The project we have chosen to develop is an agent that is able to detect motion
with the use of an PIR sensor. Once the sensor detects any sort of motion it
will make a buzzer and LED light turn on as visual and audible indicators that
motion is present. This agent we chose to develop is very similar to an alarm
system but on a smaller scale. The reason this application is useful is because
it is very useful in the real world. It is useful because it reacts very
similar to an alarm system that is in place in cars and even homes around the
world. Sources that were used:[<https://create.arduino.cc/projecthub>],
[<https://wiki.dfrobot.com/PIR_Motion_Sensor_V1.0_SKU_SEN0171>],
[<https://www.ardumotive.com/how-to-use-a-passive-buzzer-module-en.html>].

## Agent

The main characteristics of our agent is to detect any sort of motion then
react by displaying an LED light as well as audible outputs through the use of
a buzzer. What makes it an agent is the ability for it to make appropriate
choices given physical inputs. It is also an agent because it is able to react
to the environment, our agent is able to react by producing visual and audible
outputs. The aspect that makes our agent rational is that it only reacts to the
environment once motion is detected, if no motion is detected then nothing will
happen. Our agent is considered a simple reflex agent. The Performance measure
for our agent is successfully detecting motion and outputting visual and audio
cues. For Environment, it would be class rooms and laboratories. The Actuators
are the buzzer module and LED light. The Sensors consisted of the PIR motion
sensor.

## Challenges and Learning Experiences

During this lab we encountered many different challenges that posed as really
valuable learning experiences. One of the main challenges that we encountered
was enabling all of our modules and sensors to operate correctly without any
errors. This was a challenge because at first we were able to get each module
to operate correctly on its own but once we started to add all the modules and
sensors together to create an agent most of them did not function properly.
What these challenges taught us was to utilize different resources to do more
research which helped us debug the problems that we encountered.

## Ethical Benefits and Implications

- What entities, businesses, organizations do you envision developing the type
  of the application you have chosen to develop? Some entities that I envision
  that would develop this type of application is organizations that utilize
  alarm systems in their products or offer security services for clients.
  Although our agent is on a very small scale it has similar features to alarm
  systems that are currently in the market today.

- Who are the intended users of this technology? The intended users of this
  product are individuals that own a home or need to establish a simple alarm
  system for their personal use. For instance, an individual would be able to
  place this agent by a door and if it detects motion it will then beep
  notifying the owner of the house that someone is present.

- Who is not supposed to use this technology? This technology is intended to
  be used by everyone but some people that are not supposed to use this
  technology is individuals that could take advantage of it. For example, if a
  potential intruder get a hold of this technology then they could potentially
  examine the technology and find a solution to bypass each of the modules and
  sensors to deactivate our agent.

- How can the application developed in this lab cause harm? This application
  developed in this lab could potentially cause harm from the buzzer module. The
  only way the buzzer could cause any sort of harm is the frequency that it
  emits. The tone of the buzzer could potentially damage an individuals hearing
  although it is very unlikely.

- What solutions could be implemented to avoid the harm or to fix the harm
  described above? A solution that could be implemented to avoid harm is
  possibly utilizing a buzzer module that emits a quieter tone that is safe
  for all individuals. Another solution is to reduce the buzzer volume in the
  source code.

## Team Work

During this project we implemented many different team working strategies to
complete this assignment. During the first part of the assignment we conducted
research together to find an interesting project that could be achieved with
the resources given to us. Once we selected a project we began to assemble the
hardware as well as develop source code for the agent. When it came to writing
the report we split up the amount of work evenly by giving certain sections to
one person and the rest to the other member of our team.
