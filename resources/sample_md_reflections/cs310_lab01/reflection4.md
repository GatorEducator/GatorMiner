# Report by

## Planning, due on January 27th, 2020 by 11am

### Timeline

| Timeline  | Tasks |
| ----------- | ----------- |
|   Jan 27    |    Planning   |
|   Jan 31    |  Material received  |
|   Feb 3     |  Wheels and motors assembled  |
|   Feb 5     |  Wires, battery, and Bluetooth assembled |
|   Feb 6     | Attempted to upload working code. |
|   Feb 7     | Turn in Lab. |

### Hardware

- Arduino board
- Transistor
- Diode
- 2-4 Motors
- Motor Drive Shield
- Bluetooth Module
- Chassis and wheels
- Bread board
- Various wires + resistors

## Arduino Project

Our motivation for this project was to create a "smart" car. We draw inspiration
from a project on the Arduino website. <https://www.youtube.com/watch?v=Q36NbjPMV5k&t=221s>
This link helped us to figure out how to create the build.
<https://create.arduino.cc/projecthub/samanfern/bluetooth-controlled-car-d5d9ca>
this link gave us the initial inspiration for the project.

## Agent

Our car is a simple reflex agent that we plan to sophisticate further. The performance
of the car is to drive straight, its sole mission is to keep moving forward at all
costs. The environment that we would require of this agent consists of an open arena,
a straight track with no obstacles to impair the agent. The actuators of the car
consist of the hardware, the connection of motor to wheel, and battery to motor.
The interaction between these components as triggered by the Arduino board is what
allows our car to move. Currently, the sensors of our car is very limited, which
is why such a controlled environment is required. As we move forward with the car,
however, we will be installing a simple sensor that causes the car to turn when
it detects a wall in front of it. This sensor will allow the car to operate in a
much more dynamic variety of environments.

## Challenges and Learning Experiences

We have struggled throughout every process of this project. From the moment we tried
to test the arduino board to flicker a light to our "smart" car that runs aimlessly
in a circle only to stop after it gets tired. Our first road block was assembling
the car. We had problems with wiring the car, and we had to look through several
circuit modules and videos to see where which wire goes to which port. Our second
road block after assembling the car, was uploading code. For some reason, we were
unable to upload the code while the motor drive shield was connected to the arduino
board, so we took it off and voila, one of the motors started moving. Having only
one motor run was not the expected outcome, but nonetheless was an exciting feat.
For some reason the motor would only spin when it was connected to the laptop, and
we assumed it had to do something with the amount of energy going through the motors.
However, we found that there was some resistance in the wheels preventing them from
spinning. Once we got those removed, we had all four wheels turning, but then would
eventually stop for what we assume is a lack of power. Our last road block is something
we cannot confront. Our idea for this car is to have an application on a phone to
send commands for the car to execute. However, the bluetooth module we received
only works for android phones, and even though we downloaded an emulator on the
laptop, there was no way to connect the bluetooth.

## Ethical Benefits and Implications

This "smart" car could be useful for many different implementations. It could be
used for an Amazon warehouse, where it can carry heavy boxes in a predetermined
path. Or in a more controversial use, it could be used in military fashion for strapping
an explosive and sent in a predetermined route.
This machine could be used for many various purposes. Each user can use this car
for whatever their intended purpose could be. I believe this machine is not something
that is groundbreaking, but would be used for convenience.
I don't think there is a specific type of people who are not supposed to use this
technology. Like discussed previously, it could be used for malicious intentions.
However, this is something that is so accessible that if someone were to use it
for their malicious intention, it would already be developed.
The only harm this application can cause is the purpose of that application. If
the purpose of the application is to cause harm, it would cause harm.
We suppose that to avoid harm for this application is to implement universal access
to each machine with a key system for multiple people in power. For example, if
the machines go awry, two or three people of power can execute a kill switch to
prevent from further damage or harm.

## Team Work

We collaborated effectively on this project. Both of us showed up during lab time,
and we operated simultaneously on the car. This meant that while one of us was
soldering, the other would be ensuring that the wires were positioned correctly.
While one of us was assembling the car, the other would be looking at the next steps
of assembly. While one of us was coding the car, the other would work on the descriptions
in the reflection. Overall we successfully divided the labor within this project.
