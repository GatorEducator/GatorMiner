# Reflection by 

  The overall design of our robot was centered around utility, in that we made a blocky shape
that purely seeks to do the task that we've assigned it as opposed to attempting to make the
robot look aesthetically pleasing in the process. Our robot has 2 Ultrasonic sensors, a color
sensor, a gyro sensor, and two motors. In my programs, the robot uses "tank drive" steering,
in which the left and right sides are rotated independently in order to allow turning around
the center of mass. Our final design does not actually do this effectively because we did not
center the drive-base with the center of mass. The gyro sensor is placed approximately where
we anticipated the center of mass would be so that when the robot turns, it ideally returns a
more accurate reading of the heading of the robot when it turns. In my version of SprintRace,
the gyro sensor is used to verify that the robot is on the same course that it started on and
it turns slightly to course-correct if it is not. The wall at the end of the race will be
detected by the ultrasonic sensor and the robot/program stops. ObstacleCourse uses the front-
facing ultrasonic sensor to detect obstacles, and upon seeing an obstacle, the robot turns
right, at which point the left-facing ultrasonic sensor detects when the robot passes an object
and then turns back left. The gyro sensor is being used to verify that the robot turns the full
90 degrees each time, and the color sensor detects the red finish line at the end of the course.
BoxPush is designed to drive straight forward until the color sensor detects that the finish
line has been crossed.

  My robot has an ethical behavior for the sprint race, in that I use the gyro sensor to keep it
in its own lane so that it does not interfere with other agents unless they run into my robot.
In the obstacle course, the robot is supposed to not hit any obstacles, therefore ethically
avoiding anything important.

  The article __"Why Ethical Robots Might Not Be Such a Good Idea After All"__ by Alan Winfield
states several issues that our current society faces in terms of creating "ethical robots."
The three mentioned by the article are that robot manufacturers could design robots with anti-
consumer practices and/or to unethically improve their standing in the market. The last two issues
are fairly similar, in the way that they both deal with robots' ethics settings to be
tampered with, either by the intended consumer or an outside force that hacks into the robot.
Robots that allow the user to modify the ethics settings are problematic because their existence
implies that the users can be trusted to make ethical decisions with regard to the behaviors of
the robot. If the user decides to modify the behaviors, either through an accident or by
malicious intent, it is likely that the behaviors the robot would exhibit would not be considered
ethical by observers of the robot. If the robot is hacked, there is likely malicious intent,
and therefore it is not unlikely that these "ethical robots" would, or could. be turned into weapons.
The robots today in the races were generally intended to be ethical, however a large number of
them veered wildly off course and as a result crashed into other robots. This is an example of
the user-modified ethics settings outlined in the article because, even if the intent was an
ethical robot, the robot still exhibited unethical behavior.
