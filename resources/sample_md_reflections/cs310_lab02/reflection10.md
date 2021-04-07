# Report by 

### Project Selection

For the second part of Lab 02, I chose the "Ball Detection and Tracking"
project. Given my previous experience with drawing shapes, Python, and Python
frameworks, and given my lack of experience, but interest in video capture and
manipulation using OpenCV, this assignment greatly appealed to me. I always
wondered how would it be possible to capture video feed from a device's camera
using Python and how, if possible, to manipulate that feed, so when you
demonstrated Python's ability to do such that during your in-class examples
of facial and object-recognition using OpenCV, I decided that that was just the
type of artificial intelligence I was interested in and made it my priority to
learn more about OpenCV and how to use it, with the
"Ball Detection and Tracking" project being the first step to getting me feet
wet with OpenCV. After reading numerous online articles on OpenCV as well as
doing your in-class reading assignments, I feel like I have already learned
a lot about OpenCV and it is my hope that I continue to learn more long after I
have completed your class.

## Learning Agent

My learning agent consists of a Python program which takes video feed, either
user-specified or taken as a live recording from the device's video camera, and
proceeds to create a background subtractor to separate the background from the
foreground of the video feed. The next step of the program is to create
several arrays for storing the coordinates of blobs detected within our
specified area-of-interest for further use later. It is at this point in the
program that the time is taken since the beginning of the epoch in order to
later calculate the running time of the video feed submitted into the program,
which will then be used to calculate the velocity of the moving ball. After this,
a while loop begins executing (which only ends execution once the user presses
'q' on their keyboard or the video no longer has any more frames to analyze,
whichever comes first). Two variables are created to contain the individual
frames within the video feed submitted by the user (whether direct live-feed or
pre-recorded footage) for further analysis. Immediately, an if-statement is
constructed to terminate the loop if the variable that contains the individual
frames is empty. It is inside the if statement that we calculate the runtime
and velocity of the moving ball. Outside of this if statement, but still within
the while loop is where the analysis of each frame takes place.

Initially, a window is created called "Pitch" with an aspect ratio of 480 x 853,
which contains the user-submitted video feed with the same aspect ratio at the
right viewing angle. Afterwards, two copies of the user-submitted video is
created, a tracking video and a blob video. A gray version of the video feed
is also created by applying the cvtColor() method on the original video feed.
As standard with object-recognition in artificial intelligence, a blurred copy
of the grayscale version of the original video feed is created using the
.medianBlur() method of the OpenCV framework. A variable called "fgmask" is
created which subtracts the background from the grayscale copy of the original
video feed.

Next, parameters are set for the blob detector, by creating a variable named
"params" and using cv2.SimpleBlobDetector_Params(). The parameters for the
simple blob detector is that it will filter by area where the area is a minimum
of 4 and a maximum of 100. Next, it will filter by color where the blob color
is 255. Afterwards the SimpleBlobDetector is set to filter by circularity with
a minimum of 0.8 circularity and is finally set to filter by convexity with a
minimum convexity of 0.8. Finally a SimpleBlobDetector is finally created and
assigned to a variable as well as a variable to store the keypoints of the
blobs detected in the grayscale copy of the original video feed with the
background subtracted from the foreground.

A rectangle representing the strikezone is created using coordinates for each
corner as well as coordinates for the ROI (region of interest) to ensure that
we are only detecting blobs in the latter. Based on this ROI, an array of
tuples is created using a for/foreach loop in which all blobs within the
ROI is assigned an x-coordinate and a y-coordinate in the form of a tuple. This
array is then converted into a list using Python's built-in list() method and
iterated through using another for/foreach loop in which all points are
outlined with a green circle and surrounded by a rectangle
(for location tracking). Using the "writer" variable, the individual frame
(as we are still within the while loop) is written to the tracking video, which
is being displayed to the device's video screen and the entire process is
repeated for each subsequent frame until the video feed has no more frames
(i.e., you have reached the end of your video) or the user presses 'q' on their
keyboard.

After the video has ended (and thus we are now outside of the while loop), if
the coordinates of the last blob detected within the ROI are determined to be
within the previously described rectangle that serves as our strikezone,
"STRIKE" is printed to the screen, otherwise "BALL" is printed, the video
capture is released, and all windows are closed.

## Comparative Study

Based on several tests I've run, it appears the program performs as expected
(which is very impressive to me, even though I know according to the
implementation there is no room for error under normal circumstances). In
other words, different pitching angles do not appear to affect the performance
of the algorithm, which is further proof of its validity and the strength
of its implementation.

## Challenges and Learning Experiences

The main challenge of this project was simply learning the OpenCV framework
and getting familiar with the lab starter kit, but this could be better
described as a learning process as, given my previous experience with Python,
once I ran the program several times and read through the program once, I was
fully familiar with the program, how it ran, and how to add my own changes to
the program in order to track the location and the velocity of the baseball
during runtime. In fact, I would like to take this project futher, if possible.
Maybe other interesting changes could be made to the program's implementation in
order to track other features of the ball during travel?

## Ethical Benefits and Implications

1. What entities, businesses, organizations do you envision developing the type of the application you have chosen to develop?

Perhaps the most obvious entity/business/organization that would be interested
(and already has) developed this type of application would by the MLB
association, which uses the software to track various statistics regarding each
pitcher's pitch. Other entities include the U.S. Navy for use with the
object-tracking programs located within each airplane (given resurged interest
in UFOs flying within U.S. Navy airspace (although admittedly the program
would have to be edited in order to track such objects versus baseballs).
Additionally, from this logic, most, if not all other branches of the U.S.
military would be interested in such object-tracking software as well for
national security purposes as well as combat strategy, which was the subject
of controversy given Google's now-cancelled contract with the Pentagon years
ago to employ AI in order to aid in the accuracy of images used for drone
strikes.

2. Who are the intended users of this technology?

Perhaps the most obvious would be any and all sports analysts, whether they
be coaches, announcers, or the players themselves. The information relayed by
this software would allow for players and coaches to better adjust their
strategies according to their own as well as other player (i.e., rival teams')
pitching characteristics given the highly strategic nature of the game of
baseball (or any other national sports conference for that matter).

3. Who is not supposed to use this technology?

Those with no experience regarding the game of baseball and/or use for the
information relayed by the program, such as pitch velocity as well as ball
location during its travel to the home plate. As you would imagine, such
individuals would have no use, and possibly interest in such interest,
rendering it meaningless to them.

4. How can the application developed in this lab cause harm?

Such software, when properly modified, could be used to
detect a whole range of objects not previously intended for use with this
program, such as the previously mentioned drone strikes Google was previously
slated to aid in recognizing through the use of artificial intelligence.
Given the nature of explosive devices, the previous history of military
organizations around the world intentionally or accidentally targetting
private citizens (or even military actors for that matter), object-detection
programs such as this program could aid in the perpetuation of human harm and
even death on a scale and level of accuracy that would be hard if not impossible
without the aid of programs such as this one.

5. What solutions could be implemented to avoid the harm or to fix the harm described above?

As with the case of self-driving cars, this program could be modified, perhaps
dramatically for recognition of forbidden objects
(such as humans/civilians, animals, etc.) to reduce the chance of non-combat
entities being harmed in the usage of this program, albeit modified, in combat
operations by the U.S. military or any other organization around the world. In
such situations, if the presence of a 'forbidden object' is detected during
runtime, the program could be immediately terminated or any further actions by
this, or any other programs could be halted until the 'forbidden objects' are
no longer detected by the program. As mentioned previously, this does not
entirely eliminate the chance that unintended targets are accidentally harmed
in the process of combat operations, but does considerably reduce the chance of
this situation occurring.
