# Reflection by 

We started by trying multiple attempts using the `movePilot` class to create a
chassis to control the movements of our robot. After several failed attempts,
and many hours of research and test iterations, we gave up on the idea of
`movePilot`, and used delayed stop commands with Boolean values set to true to
start and stop the two motors synchronously. Though this was not as idea as
creating a `movePilot` class, and utilizing the chassis commands, we were able
to implement course stability through the use of a gyroscope that kept the
robot focused and on a straight line course. By first zeroing the gyro before
setting the robot out, the robot had a reference for what "straight ahead" was,
so whenever the robot felt it varied more then 5บ in either direction the
opposite motor would decrease by roughly %10 power output to course correct.
Once the gyro felt the robot was back on the correct heading both motors were
returned to full power. This was just one of the methods use to keep the robot
ethical. Once we had the robot moving forward, and maintaining a straight line,
we used the ultrasonic sensor to monitor the path ahead. In the sprint race the
ultrasonic sensor was used to detect the finishing wall, stopping the robot
when it encountered the wall, or stopping point. The obstacle avoidance race
used similar tactics again using the gyro to stay on course, only this time
with two ultrasonic sensors instead of just one. In order to avoid obstacles,
one sensor would look ahead for obstacle, and the other was placed on the left
side of the robot to look for openings where the robot could pass through. If
or when an obstacle was detected the robot would break one wheel and turn 90ยบ
to the right, reveling a second ultrasonic sensor. The robot would then
continue on the now 90ยบ path with the side sensor looking for the first
available gap next to the obstacle, once a large enough gap was found the robot
would break one wheel and turn -90บ back to a straight line and continue
forward. This cycle would continue, looking for obstacles in front, turning
90บ, and looking for a clear path, until the robot reached the red line, where
the color sensor would detect the red strip and stop the robot and program. The
box pushed used a combination of these tactics, with the gyro keeping a
straight course, and the color sensor looking for a red strip marking the
finish line. The box push had a delay installed so once the robot crossed the
red line it made sure the box made it into the goal.

Our Robot took a more ethical approach to these tasks, by staying in its own
lane, and avoiding obstacles the robot tried to stay out of trouble and
complete races under its own steam and merit. We used the gyro to keep as
straight a heading as possible to prevent the robot from interfering with other
robots paths, as well make sure we could stay on track for where the course
was. Other robots had complete disregard for the racing grounds, and some were
even programed to run into the paths of other robots taking them out of the
race. That idea illustrating the concept of an unethical robot, winning by
bringing down the competition and not under its own prowess. Our conceptual
method for acting unethically was to have the second ultrasonic sensor blast
ultrasound in the reverse direction, or rather any direction that wouldn't
interfere with our primary sensors data, but rather corrupt our competitors
sensor data. This would have in practice have been very unethical, as it gives
our robot a strong advantage to complete its task, but creates a massive
challenge for other robots to overcome in their goal of completing their own
tasks. As we've seen with other robots using slightly more obvious methods,
this method could be considered a lot more stealthy, and thus harder to
compensate for. Where other robots used their physical chassis to disrupt the
movement toward the finish line, our robot would not have had to stray from its
intended path while still vastly throwing the competition into a frenzy of
disarray. Sadly we did not actually test to see if this method was effective
against our robots, and there was not enough control over the race environment
to see if the intended effect took place.
