# Report by

### Project Selection
We will be completing the baseball video overlay and baseball detection project.
We chose this project due to our combined interest in working with film. This
project seemed like enough of a challenge but still within feasable reach of our
skill set.

### Timeline

| Timeline  | Tasks |
| ----------- | ----------- |
| 2/14/2020 | Determine problem with `otsu_and_riddler.py` |
| 2/14/2020 | Select learning algorithm |
| 2/14/2020 | Select feature descriptor |
| 2/17/2020 | Compile videos, possibly schedule to film own |
| 2/17/2020 | Overlay videos with `addweighted` function|
| 2/20/2020 | Create baseball tracking function and apply to videos|
| 2/21/2020 | Locate start and stop of baseball |
| 2/21/2020 | Project walkthrough in lab session |
| 2/24/2020 | Finalize project source code|
| 2/27/2020 | Complete lab report |
| 2/28/2020 | Final project demonstration in lab session |

## Learning Agent

This learning agent was created with the goal of detecting an object that is or
similar to a baseball for determining the accuracy of pitching. The agent takes an
overlayed video of pitching as input, and provides and output of the same
overlayed video but with tracking of a baseball from the moment it is released by
the pitcher to when it is caught by the catcher. This agent uses rotation,
reszizing, color conversion, and blob detection (with circular and convexity
parameters) algorithms to detect a moving white object through the overlayed video
and provide its tracked trajectory.

## Comparative Study

The positioning of the camera changes the ability of the detection algorithm to
locate the baseball based on the various angles of the ball and the relative
sizing in a frame due to its angle.

## Challenges and Learning Experiences

This lab was particurally difficult from a technical standpoint. With both of us
not having any prior experience with artificial intelligence or cv2, it was
relatively difficult for each of us to understand the processes associated with
this lab. Each of us had to research overlaying and object detection extensively
before writing any code, and we often hit points where we had to completely
rewrite what we had written. Hannah found the biggest difficulty in retrieving
frames from a video, and Madelyn was challenged by masking and successful
detection of such a small object (such as a baseball) We both learned from this
experience that research is very helpful in understanding a process, and should be
done before writing code. We also were able to expand our knowledge of the
abilities of cv2 both in a general way and also in a technical aspect.

## Ethical Benefits and Implications

In this section, drawing on class discussions and readings, answer the following questions

1. What entities, businesses, organizations do you envision developing the type of the application you have chosen to develop?

An application which determines the accuracy of a pitcher would through overlaying
video and baseball detection, would most likely be developed by a sports-related
business or organization such as sports teams, physical therapists and potentially
other medical practices. This application is very specific in it's usage, and
thus would not be created by another agency specializing in artifical
ingelligence. It would be most beneficial for individuals who are involved in
athletics to develop this tool, as they could create it with necessary and useful
features to help athletes improve their skills.

2. Who are the intended users of this technology?

This technology was created with the purpose of tracking a baseball in multiple
overlayed videos to determine the accuracy of a pitcher's pitch. The intended
users of this technology belong to a specific group of people who either coach, or
particiapte on a baseball team, specifically the Allegheny College baseball coaching staff and team. This technology could also be brought to a wider
auidence such as softball which also focuses on the accuracy of a pitch. Users
would most likely be pitching coaches to review the abilities of their pitchers,
or pitchers, themselves, who are trying to improve their skills.

3. Who is not supposed to use this technology?

This technology would most not likely be used by anyone who is not an athlete
(specifically baseball or softball player). This technology is very specific to
use and measurements. An individual who does not play baseball, or does not
understand the technicalities of pitching would not use this technology, as it is
not applicable to them in any way. However, it could be a good learning tool for
individuals who are not yet baseball/softball pitchers, but are interested in
pursuing the sport.

4. How can the application developed in this lab cause harm?

This application is not particurally dangerous in any way. The implications of
using this technology would cause mental or emotional harm, rather than physical
harm. With a tool that measures the accuracy of multiple pitches, there is the
possibility that a coach would be too hard on a pitcher to achieve a higher
accuracy. It is even more likely that an individual would set themselves to an
extrememly high level of achievement/precision if their pitches were being
recorded at every practice and every game. The overlaying of videos could also be
used to manipulate others and present false information.

5. What solutions could be implemented to avoid the harm or to fix the harm described above?

In order to solve the issue of misusing this technology, individuals who are using
it should be taught the ethics of this type of artifical intelligence. However,
ethics is a difficult concept in AI, as it is such a fast-growing field, and is
debated by many individuals. It is important that in order to avoid harm, that the
users of this technology keep each other accountable, to ensure that they are
using this application for the betterment of athletes and not for manipulation, or\
personal gain.

## Team Work

In order to complete this project, we split the work up into two sections: the
training and detection portion and the video overlay section. X developed
the training algorithms and the baseball detechtion technology while Y worked
to break the videos into frames, overlay each image, and build it back into a
video.
