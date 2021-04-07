# Report by

## Planning, due on January 27th, 2020 by 11am

### Timeline

| Timeline   | Tasks       |
| -----------| ----------- |
|   dates    |    task 1   |
| 1/27       |   Planning
| 1/30       |   Start Code
| 1/31       |   Finish Code
| 2/3        |   Test Code
| 2/4        |   Finish Report
| 2/7        |   Make final changes to lab


### Hardware 

- Arduino board
- in an itemized list, specify specific sensors, motors, etc. to be used in your project
- Bread board
- Highlight LED
- Digital Light Sensor
- Hard Jumper Wire
- Power supply/USB Cable
- DuPont Line


## Arduino Project

Describe the application you have chosen to develop and provide a motivation for why it is a useful application. Include  references of all sources you have used throughout this project (URLs are sufficient).

I have chosen to create an application that consists of LEDs and a light sensor. I originally was working with just two LEDs and two light sensors. My
intial intention was to have the two lights sensors turn the LEDs on and off by detecting if light was there or not. I would have designed to do
the opposite fuctions. However, I did not have all the parts to assemble this kind of project. Instead, I took my initial idea and combined it with
another source that I found on Youtube. In this other project they had a series of LEDs that had a siren like affect. One LED would turn and then off, and
this step would repeat in the next LED and so on. In my application, I added one light sensor and some more code to see how the two projects would work
together. When the lights sensor detects that there is no light, the LEDs will turn on and do the siren pattern. This is a useful application because
it can be used for caution or alert warning. For example, when it dark outside LEDs can be turned on so that people and cars can see where certain
objects are in the environment around them.


## Agent

Explain the characteristics/attributes of your agent, what makes it an agent (within the discussed course content), what makes it rational, what type of an agent it is, and what is its environment task (PEAS).

In my agent I have a series of LEDs that blink one after another like a siren. The next part to my agent is the light sensor, which detects if there is light
in the environment. The reason that my agent is rational is because it can be used for safety measures. The LEDs act to alert everyone that surrounds
them. When there is no light or when it is dark, the light sensor will send the signal to each of the LEDs and will turn them all on. The specific environment could
be located on freeways, police cars, and airplanes that are flying. In all of these environments, the application's main job is to alert people and keep everyone
cautious and safe.

Below is a picture of how my application actually looks:

![Logo](projectPic.jpg)

In order to run this application you have to set the hardware as follows:

1. You need a 5V battery or equivalent power source
2. You need to connect your power source to the UNO R3 board
3. Next, you will need several pieces of standard wire that will be connected on the digital side of the UNO board to the bread board.
4. Connect one end of the LEDs on the positive side of the bread board and the other in the neutral area.
5. Each wire should be lined up with one LED
6. Lastly connect the digital light sensor the UNO R3 board. You will need to connect the VCC wire to the 5V power source, the ground wire to the GND port on
the board, and the DO wire the the positive side of the bread board that the LEDs are on.

## Challenges and Learning Experiences

Discuss any challenges you have encountered during the work on this lab and describe what have you learned. 

While I was working on this lab I ran into a few challenges. One of the main challenges I had was working alone.
The schedule that I have this semester is difficult to work around, which made finding time to do this project
much harder. I also had to deal with learning how to use Arduino all by myself and had to develop a project
on my own with no one to collaborate with. The next challenge I had was finding a project that was doable in
terms of hardware. I struggled for about a week trying to find a project where I had all the pieces. In the end,
I had to change my project because I just didn't have one piece that I really needed. After doing this lab I
have learned that working in groups really does make a difference. Collaboration is key when it comes to
computer science.

## Ethical Benefits and Implications

In this section, drawing on class discussions and readings, answer the following questions

1. What entities, businesses, organizations do you envision developing the type of the application you have chosen to develop?

Any organization that has to take safety or cautious measures will use an application that is similar to the one that I have
developed in this lab. For example, air planes use blinking lights in the sky to alert other aircrafts. Another example can
be the police. There are many instances where police are involved and they have to block of certain areas to keep the surrounding
public safe.

2. Who are the intended users of this technology?

This type of technology is for people who are trying to make the environment around them a safer place. Anyone
who has to take safety measures will use this type of software.

3. Who is not supposed to use this technology?

This technology is not suppose to be used by people who will abuse it. In the past there have been cases where blinking
lights have actually caused harm to the public. One example is when a person shined a laser up into a pilot's eye while
he was flying. This can be very dangerous and can have many consequences.

4. How can the application developed in this lab cause harm?

The application involves LEDs or lights, and even though they are meant to make people be more aware, they can also
distract them as well. LEDs can hinder the performance of drivers if someone is intentionally shining them at people.

5. What solutions could be implemented to avoid the harm or to fix the harm described above?

One solution that can be implemented to avoid the situation that is described above is to only sell higher quality LEDs
and software to corporations that really need them. LEDs that are used by police and airplanes cost millions of dollars
already, so, cost can be another solution to stopping people from abusing them.

## Team Work

Describe the details of your team working strategy, specifically explain how did you complete this work as a team and describe the specific contributions of each team member.

The entire lab was complete by myself, but I had a specific plan that I followed. I knew that working on this lab would
require a significant workload because of the research. I needed to manage my time so that I could not only program the
hardware, but do the necessary research to learn how to use Arduino. I made sure that I understood the type of project
that I was developing. This in end helped me work around not having a group because I was already confident enough
knowing what I was going to do.