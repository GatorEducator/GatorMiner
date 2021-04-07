# Report by

### Project Selection

We will do 2.1 Baseball Detection and Tracking since it seems to be the most feasible with out current knowledge of OpenCV. Plus, this is probably the most useful out of the projects for detecting the path of a baseball/predicting a pitch.

### Timeline

| Timeline  | Tasks |
| ----------- | ----------- |
|   2/12    |    Getting opencv and book code working   |
|   2/21    |    Get ball tracking working   |
|   2/28    |    Calculate speed, location, break  |


## Learning Agent
Describe the methodology used for your learning agent (algorithms, the goals of learning, inputs, outputs, etc.)

The algorithms used were developed by using OpenCV to create a mask, detect blobs, and add circles to detected blobs. For the mask, we used COLOR_BGR2GRAY to turn the video gray, and then applied background subtraction with createBackgroundSubtractorMOG2() and morphologyEx(). We added morphologyEx() to help refine the initial background subtraction that was already present. The blob detection was performed using SimpleBlobDetector_create() on the gray video after refining parameters that were previously specified. The goals for our agent were to track the pitch of a baseball and calculate some of the aspects of the pitch. The aspects we calculated were the location of the ball in relation to the frame (x, y positions) and the speed of the pitch. We did so by improving upon Dan's original pitchtracking code. The inputs simply include the desired video, but the outputs use information from this video. The location takes the x and y positions that the ball is found at throughout the pitch. It is refined by removing any locations that are outside of two standard deviations of the mean. This is used to eliminate outliers that may not be the ball during its trajectory, or other blobs that are not the ball. These locations are printed out, becoming an important output for the program. After getting these locations, we then retrieve the framerate of the video and use it to calculate the duration of the pitch. The distance to the catcher is then divided by this duration to get the pitch speed in feet per second. Finally, we convert this to miles per hour to get the speed of the pitch as an output.

## Comparative Study
Describe the performance metrics for different environment settings (different positioning of the camera).

For our program to work, the environment must be pretty specific. The camera should be behind the pitcher and filmed vertically. Additionally, the camera quality needs to be filming in HD, otherwise it is possible to lose track of the baseball. Finally, the video should only be one pitch at a time, otherwise the calculations will be wrong. The videos we used were from Dan's comp. The other videos provided were not high enough quality and not formatted in the correct way.

## Challenges and Learning Experiences
Discuss any challenges you have encountered during the work on this lab and  describe what have you learned.

We encountered many challenges during this lab. For the first week of the lab, we
tried to understand and make changes to the ball tracking program so it would be
able to track a white object(Baseball). This was a big challenge for us because
we couldn't get the right mask or blob detection for the application to detect
white objects. After spending many hours testing and reading some documentation,
we were able to accomplish something. The application was able to detect the
baseball, but it was not very accurate and was also detecting other areas where
white. From this point, we decided to switch from the ball tracking application
to the pitch tracking application.

For the pitch tracking application, we had three major challenges. Our application is not comparable with
poor quality videos. You will need a high resolution video and a one pitch a time. If a video does not
have these two conditions, our application will not work. Calculating the speed of the Baseball was
something really difficult for us. We worked many hours to get this implementation into our
application. After testing several ways to calculate the speed, we were able get the accurate speed of the baseball.
Lastly, we tried calculate the spin rate of the baseball. For us, this one the most stressful and complicated part of the lab.
We did a lot of research to find a formula to calculate the spin rate of baseball. After spending several hours, we gave up
and decided to calculate the RPM which equals revolutions per minute. We went with this approach because it is
similar to spin rate. We found and formula, and where able to calculate the RPM, but it was not accurate. We
tried many different ways to change the formula and different conversions but we were still getting inaccurate results.
In the end, we decided not to do this implementation and instead did location of the baseball.


## Ethical Benefits and Implications
In this section, drawing on class discussions and readings, answer the following questions

1. What entities, businesses, organizations do you envision developing the type of the application you have chosen to develop?

Sport organizations such as MLB, NBA, and NFL already have or are developing applications similar to ours. Companies like Tesla, Google, and GM are using
similar algorithms as in our application for autonomous driving. The classification and detection of objects and vehicles is important for self-driving
cars since they need to avoid accidents and be able to detect what is their surrounding area.

2. Who are the intended users of this technology?

Baseball teams who want to analyze their players' pitching patterns and collect
data to improve their pitching. Sport analyst would use this technology
to collect data on the performance of players and use it for stats reporting.  

3. Who is not supposed to use this technology?

Anyone can use this technology for educational or professional purposes.
This technology is intended for everyone to use, there is no restriction on
who is supposed to use this technology

4. How can the application developed in this lab cause harm?

The application developed in this lab can't cause any harm. Everything is code
based, therefore is not really possible to this application to cause harm.

5. What solutions could be implemented to avoid the harm or to fix the harm described above?

Since this application does not cause any harm, it's not necessary to implement any solutions.

## Team Work
Describe the details of your team working strategy, specifically explain how did you complete this work as a team and describe the specific contributions of each team member.

For work meetings, we meet up every Tuesday and Thursday of every week for at least
two hours and sometimes more to work on the lab. We used teletype to work on the
coding at the same time. Instead of us working individually and pushing separate
work , we just used teletype instead. We both worked on the code at the same time, we
each assigned a task to do during our meeting times and we would work together on
challenged we faced during the lab. X worked on the math portion of the lab, for
instance Calculating the speed of the baseball. Overall we distributed the work fairly
and finished all our implementation on time.
