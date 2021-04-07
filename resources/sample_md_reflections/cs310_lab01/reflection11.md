# Report by

## Timeline

| Status | Timeline | Tasks |
| :-: | :-: | :-: |
| [X] |   1 / 26    |    Planning Completed
| [X] |   1 / 28    |    Hardware Constructed / Core Algorithm Developed
| [X] |   1 / 30    |    Code Heavily Developed / Project Nearly Completed
| [X] |   2 / 2     |    Code Review Corrections
| [X] |   1 / 4     |    Writeups and Reflections Completed
| [X] |   2 / 6     |    Project Fully Completed (For the purposes of this lab)

## Hardware

- 1 x Arduino board
- 1 x small Bread Board
- 1 x Rotation Sensor
- 1 x Small Button
- 1 x Buzzer
- 4 x Green LED
- 4 x Blue LED
- 9 x Resistor (Minimum)

## Arduino Project

The application that was designed tries to guess a sequence of on/off states for
four led lights.  For the application to work correctly a user input is needed in
the form of the rotation sensor and the button.  The input given by the user tells
the application how much of the sequence it got correct, and based on that input
the application intelligently adapts its guess.  This application is useful as it
is exploring adaptive algorithms to their respective inputs and expected inputs

## Agent

Our agent is composed of the Led Lights, the Rotation sensor, the small button,
and the buzzer. This agent is rational as it adapts its answer differently depending
on the input it is given.

P: How fast the agent can guess the correct sequence

E: The computer, and outside inputs

A: Led Lights

S: Rotation Sensor, Button

## Challenges and Learning Experiences

C++ had given us some issues due to the language not being able to return arrays,
so we would have had to use pointers instead. To fix this issue we made the variables
we used global instead despite it being bad practice. Wes learned a lot about Arduino
as he had no experience with it before this lab.

## Ethical Benefits and Implications

As this is the most basic of learning algorithms that would be developing this
as there are already better and much more useful learning algorithms out there.

Learning algorithms are in everyone's pockets today, and there are applications
like this for everyday life.

Anyone with malicious intent.

Our application is not capable of causing any real harm, other than some slight
eye irritation due to the bright LEDs

Resistors to lower the brightness, and mindful programming to prevent an application
like this from being so open ended.

## Team Work

X worked on the algorithm as well as correcting Travis build errors.

Y worked on some of the basic code and converting the java algorithm to C++.

Z worked on the wiring of the agent, the demo mode, and the writing.

## End
