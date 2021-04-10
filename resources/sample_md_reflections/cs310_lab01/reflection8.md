# Report by

## Planning, due on January 27th, 2020 by Midnight

### Timeline

| Timeline  | Tasks |
| ----------- | ----------- |
|   Mon, 1/27/20    |    Determine Project Direction   |
|   Thu, 1/30 | Determine Hardware Design |
|   Fri, 1/31 | Finalize Project Ideas/Components  |
| Fri, 1/31 | Finalize Hardware design and begin code |
| Tue, 2/4 | Complete Code Implementation |
| Thur, 2/6 | Test the Tool|
| Fri, 2/7 | Finalize Project|

### Hardware

Tentative Components Needed:

- Arduino board
- Breadboard
- LED Lightbulbs
  - Preferably with some different colors.
- Buzzer
- Buttons (2-4)
  - EX: SparkFun Pushbutton switch 12mm
- Jumper wires (generic)
- Resistor 10k ohm
- Display of some sort
  - SparkFun 7-Segment Serial Display - Red
  - Preferably a 4-digit display
- Jumper (Busbar), Jumper Leads Set
- PCBWay Custom PCB

## Arduino Project

For our Arduino project, we have decided to create a scoreboard using a serial
display board, a breadboard, lightbulb, and Arduino Uno. After searching for
projects online nothing interested our group until we stumbled upon a
Scoreboard project. Our group then decided making a scoreboard would be both
interesting and fun, likely because our group is made of athletes, and then
began to research the necessary components such a project would need. We were
motivated to pursue this project for a variety of reasons. For one, our group
is made of athletes, meaning we regularly interact with scoreboards.
Additionally, we thought a scoreboard would be a good application idea to show
what Arduino can do and also to help us learn more. Also, scoreboards are
always needed in the niche market of sports, meaning the project has real-world
relevance as scoreboards are used around the world every day. The scoreboard
will operate with a score on each side of the 4-digit display. When a team/
player's specified button is pressed then their respective score will be
updated. Our team considered using a light sensor, which would update the score
when it cannot see light (such as when a basketball entered the basket and
triggered the sensor, indicating points have been scored) instead of a button
for more automation, but ultimately ran out of time to do so.

![Schematic](schematic.png)

There were a number of references that were useful for our group as we
completed this laboratory assignment:

- [LED bulb tutorial](https://www.youtube.com/watch?v=KLaCWez9M84)
- [Push button reference](https://wiki.dfrobot.com/DFRobot_Digital_Push_Button_SKU_DFR0029)
- [Scoreboard tutorial](https://www.hackster.io/silicioslab/creating-an-electronic-scoreboard-with-arduino-936037)
- [4-Digit Display Documentation](https://media.digikey.com/pdf/Data%20Sheets/Sparkfun%20PDFs/Using_the_Serial_7-Segment_Display_Web.pdf)
- [Help with software serial issues](https://arduino.stackexchange.com/questions/4580/error-sofwareserial-does-not-name-a-type)
- [Image referenced for button connections](https://s3-ap-southeast-1.amazonaws.com/ima-wp/wp-content/uploads/sites/5/2017/03/10134729/IMG_2098.jpg)
- [4-digit display setup video](https://www.youtube.com/watch?v=iZI1GjCvIiw)
- [Repository with examples/documentation of how to use 4-digit display](https://github.com/sparkfun/Serial7SegmentDisplay)

## Agent

Our scoreboard display shows a handful of characteristics that make it an
agent. Although it does not meet all the criteria for an agent, our Arduino
scoreboard would still be considered an agent. First, it is reactive to a
stimulus, which happens whenever the user pushes the buttons which ups the
score displayed on the screen. On the scale of agent types, our agent would
fall under a simple reflex agent because it only responds when the buttons are
pushed and does nothing else. Additionally, our agent is rational because it
maximizes the expected value, in this case by simply updating the score
successfully. Simply put, the scoreboard does the right thing given what it
knows, which would be the buttons being pressed by who is controlling the
scoreboard, making it rational. Concerning PEAS, our agent meets these
criteria. Performance measures would include the display (if it is being
displayed correctly) and safety. The environment could take on a variety of
different forms including indoor or outdoor settings, professional or amateur
settings, basketball courts, hockey rinks, soccer fields, football fields, and
more, due to the widespread use of scoreboards in sports. The agent's actuators
would include the 4-digit display and the lightbulbs that light up when goals
are scored. On the other hand, sensors would include the buttons (and the light
sensors that were previously mentioned if they would have been used).

## Challenges and Learning Experiences

During this lab, the first challenge we faced came in the form of shipping
delays. Our scoreboard did not come in until the day of the status update,
therefore we could not begin real work outside of research for our project
until about a week into the project. This challenge set us behind on asking for
additional help and working on the implementation more quickly. The second
challenge we faced was that no one in our group has had any prior experience
with regards to Arduino, specifically configuring or coding, so it was a bit of
a learning curve for us to begin with. So when we started behind with our
limited knowledge it took more time for us to begin learning how to do it and
we needed to watch many examples. Additionally, it was even challenging to get
the 4-digit serial display to power on, much less use it, because of mediocre
documentation resources about it. The final challenge we faced was perfecting
our code, as we ran into a number of bugs and small mistakes that were hard to
notice because of our lack of Arduino knowledge, so it worked perfectly. For
example, we had broken if statements because we did not realize that we were
comparing integer and byte types. Once we learned how to do the base program
figuring out the code for the implementation we needed and wanted for our tool
was difficult to find. It took a lot of looking at code and retesting to get
the output we wanted. Overall, our group learned a lot, including how to
configure basic Arduino hardware, how basic agents function and their
characteristics, and also how to program in the Arduino language.

## Ethical Benefits and Implications

1. What entities, businesses, organizations do you envision developing the
  type of the application you have chosen to develop?

  Some businesses, entities, and organizations that might need this application
  are professional sports organizations such as the NHL, NBA, NFL, and many
  others not listed. They could use this technology for the scoreboards inside
  their arenas so the fans know the score of the game. Casual athletes or youth
  sports leagues could also keep track of the scores of their recreational
  games. Also, another entity that our project could be applied to would be for
  speed enforcement signs. Blinking speed signs help people see the speed limit
  in the night to make it easier to see in the dark.

1. Who are the intended users of this technology?

  The intended user of this technology is both fans of going to live sports
  events and companies that own any sort of sports arena from big pro teams to
  neighborhood rinks. The fans will be one big user because during the game
  everyone turns to look at the scoreboard to check the time left and who is
  winning. Also, the owners of rinks need these because they can not be used
  for games if there is no technology to display the time and score. Therefore
  it is a very niche market but is something that will be needed until new
  technology is developed. If the scoreboard is small like ours, the intended
  users would likely be recreational sports enthusiasts who want to keep track
  of the scores of their own games. That being said, professional sports
  leagues also use scoreboards and they would be another potential user of this
  technology.

1. Who is not supposed to use this technology?

  People who want to unethically alter the state or score of a game should not
  use this technology. For example, a timekeeper could unethically put an
  incorrect score on the board for personal gain and such a person should be
  barred from using this type of technology. This display board technology
  could be used potentially in making a display time for a bomb. If this
  program and technology were used by groups that make them it would be very
  harmful to many people. Essentially, people should not use this technology
  for unethical purposes.

1. How can the application developed in this lab cause harm?

  It is unlikely the scoreboard itself could cause harm, unless it is faulty
  which could lead to injury or the scoreboard not properly functioning. If the
  scoreboard is not properly functioning, this could lead to revenue losses for
  professional sports leagues and even loss of time for those in other leagues.
  As we previously mentioned, the display board could be used for unethical
  purposes. An application developed could potentially be used to harm people,
  buildings, and other objects found in day to day life depending on where the
  event happens. It would cause harm by exploding and impacting everyone near
  it.

1. What solutions could be implemented to avoid the harm or to fix the harm
  described above?

  Higher standards of scoreboard testing could be implemented in order to avoid
  this harm. Testing could also be implemented with our code to prevent
  software issues. With regard to unethical uses of a 4-digit display and
  timer, the only way I could see a solution to avoid the harm would be if only
  the government had access to the board technology and were the only ones
  allowed to distribute them to licensed businesses and organizations. This
  would ensure a good knowledge of who all owns them could be kept by the
  government.

## Team Work

For our team working strategy, our group met outside of the lab once or twice
every week. All of us were always present when we worked on it
and we all contributed to the project evenly. All team members did an equal
amount of work. Then once we finished our project we all picked a different
part of the report to do and divided it evenly and worked on it since we all
had knowledge of how it worked and got put together. Overall, our team worked
very well together with regards to communication and project completion.
