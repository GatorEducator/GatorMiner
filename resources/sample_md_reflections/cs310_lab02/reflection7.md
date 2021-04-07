# Report by

### Project Selection
Identify your project to be implemented (name the project and why you chose it)

The project that our group decided to do was Project 1. Our group wanted to do this project because we thought it was interesting how a program could track a baseball in a video that is playing.

### Timeline

| Timeline   | Tasks |
| -----------|----------- |
|   dates    |   task 1   |
| 2/14/20    | Part 1 programs|
| 2/14/20    | Project selection|
| 2/21/20    | Finish detection program for Project|
| 2/26/20    | Test programs|
| 2/27/20    | Finish Report|


## Learning Agent

Describe the methodology used for your learning agent (algorithms, the goals of learning, inputs, outputs, etc.)

Within our project for lab 2, we used blob detection which is the algorithm present in our code. This
is the algorithm that uses a green line to track the ball from when it leaves the pitchers hands to when
it lands in the catchers glove.  The input is the pitching videos in a .mov format. The outputs are
the speed of the ball an and the point when the ball reaches its destination.


## Comparative Study

Describe the performance metrics for different environment settings (different positioning of the camera).

One positioning aspect would be if the camera was facing perpendicular to the path of the ball. In this
case, we think that we could have got a more accurate time of when it hits the glove.

To explain a bad positioning aspect, it would have not been helpful to have the camera facing the
pitcher because we would not know when the ball would reach the pitchers glove.

## Challenges and Learning Experiences

Discuss any challenges you have encountered during the work on this lab and  describe what have you learned.

During this lab, we faced many challenges but managed to work through them. At first, we planned on using
our own code that we found from the internet but realized it was extremely hard to edit and fix to track
the ball instead of moving cars. To resolve this, we used the code that was given to us and edited it from there. Another challenge we faced was not being able to download dlib onto our laptops.  We had to go down a different route by not using this because we failed at the download process.  Although we did learn a
lot by completing this lab.  For example, we learned about different algorithms and how to choose a specific one for your program. We also learned how to track a moving object and then track the speed.  We researched a
lot about the speed equation and was able to hard code it into our program which was a huge learning experience.

## Ethical Benefits and Implications

In this section, drawing on class discussions and readings, answer the following questions

1. What entities, businesses, organizations do you envision developing the type of the application you have chosen to develop?

This application would be useful to any baseball team that uses data and different metrics in practices.  Higher level leagues such as college ball and the MLB would benefit from a program like this in order to
visualize the path and speed of the ball at the same time.

2. Who are the intended users of this technology?

The intended users of this application would be baseball players and teams that want to
see their pitch.  Baseball players and coaches could use the application to think of ways to improve
the bad and to keep up with the good.

3. Who is not supposed to use this technology?

People not involved with that baseball division should not be able to use this technology. Individuals could alter numbers and essentially use the software to exploit the game. It could give a team an advantage over the rest because they would have the accurate stats and the other teams would be given misleading data.

4. How can the application developed in this lab cause harm?

One way that this application could cause harm is if the video input is blurry
or if it is poorly recorded.  If that is the case, the speed and tracking could
be read wrong and the user would be using wrong data.  This wrong data could
drastically hurt a baseball player and their team.

5. What solutions could be implemented to avoid the harm or to fix the harm described above?

A solution to be implemented to avoid the harm is to not let the program read the
video unless it is clear enough to be tracked the entire path.  Pitches that are inputted
that are not fully able to be tracked or if they are glitchy should not be used by the
program. The program should be able to compare videos and know which one is the
most clear.

## Team Work

Describe the details of your team working strategy, specifically explain how did you complete this work as a team and describe the specific contributions of each team member.

To complete this work, we met most Tuesday nights for a few hours to
work together.  We would take turns editing and pushing while the others would research
different algorithms or equations.  The other nights that we did not meet up in person,
we would communicate through a slack group message and talk about our findings and
tasks.  Each team member did not have a specific role.  We all did a little bit of everything
and contributed equally.  The one part that was individual was Chris who was the only one
who had OpenCV downloaded on his laptop.  He was the main one who would run the code once
we made changes to the code.
