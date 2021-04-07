# Report by

## Deadline for the proposal is January 27th

### Timeline

|   Timeline    | Tasks |
| ------------------- | ----------- |
|   1/29 - Wednesday    |    Draft of code for both agent (the parking aid)   |
|   1/31 - Friday   |   Code review and start working on hardware    |
|   1/3 - Monday   |   Finish building the agent |
|   1/5 - Wednesday   |    Significant progress: to the point of completion.   |
|   1/7 - Friday   |   Completely done the Project, report submitted |

### Hardware

- Arduino UNO & Genuino UNO (1)
- PIR Motion Sensor(generic) (1) [link](https://www.sparkfun.com/products/13285)
- buzzer module (1)
- Jumper wires(generic) (8)

## Arduino Project

Create a prototype of the parking aid with main focus on motion detection. When
motion is detected the LED starts blinking and the buzzer goes off, when there
is stillness the agent doesn't take any action.

## Agent

We think that our device is an Agent because it has characteristics that object
doesn't have. Such as: it exhibits autonomy, it has control over its state and
behavior and there is no outside intervention. It is goal-directed(detect motion)
and reactive(make signal once detected). We think that this is a good representation
of simple reflex agent. There is an agent and an environment. The agent has sensor
(PIR motion sensor) to answer the question what is the world like now? It has
condition-action rules, based on that the agent makes decision: Signal when there
is a motion, no signal when no motion is detected. We consider this system rational,
since it does "right thing" based on given situation. Where "right thing" is whether
to take action or not, and the given situation can be motion or stillness.

PEAS:

- Performance measure: safety, precision, correctness
- Environment: car parks, streets, garage
- Actuators: LED, buzzer module
- Sensors: PIR motion sensor

## Challenges and Learning Experiences

We faced many challenges in this lab. The first challenge was getting the Arduino
Uno to function with the code we were uploading. We first had some faulty hardware
and had some incorrect connections to and from the board. Once that was fixed we
were still having the same issue so we switched from our laptops to the desktops
in the lab as these have the Arduino program installed so we could use this instead
of the web application. These changes helped us get the Arduino Uno to function
correctly with our code. Another issues we can into was with the PIR sensors.
The first sensor we trying to use was not displaying it was working so we switch
to another sensor that was a bit less complex and it work just fine so we went
with it. The last issue we had was with the buzzer module. We got it to come
on correctly but after the sensor and leds cut off it would still make noise so
we decided not to use the buzzer, just the leds.

## Ethical Benefits and Implications

What entities, businesses, organizations do you envision developing the type
of the application you have chosen to develop?

- Parking garage companies could use this to stop accidents occurring in their
  parking lot
- Home security systems could use this to ward off intruders

Who are the intended users of this technology?

- People that have a fear of getting into accidents while parking
- People that have a fear of home invaders
- People that live in crime sensitive neighborhoods

Who is not supposed to use this technology?

- People that have do not have a fear of getting into accidents while parking
- People that have do not have a fear of home invaders
- People that do not live in crime sensitive neighborhoods

How can the application developed in this lab cause harm?

- It may cause people to be too comfortable while parking. It should be used
  as an aid not a replacement for normal safety  precautions.
- Home invasions can still happen. You still need other measures to keep your
  house safe.

What solutions could be implemented to avoid the harm or to fix the harm
described above?

- Give a precaution on the box to only use this product as an aid, not a
  replacement

## Team Work

We all worked together to get the task accomplished. If something needed to be
fixed or something needed troubleshooting we all tried to figure out the issue
together until it was resolved. As far as the planning we all looked for a
project until we all agreed on one as a group. Overall we functioned as a team,
no one did one part on their own or did not carry as much responsibility. If
something needed done we worked as a team to accomplish the task.
