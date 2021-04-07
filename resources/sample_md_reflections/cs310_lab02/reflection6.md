# Report by

### Project Selection

Our team will be opting to create implementation 2.2 involving the baseball video
overlay and baseball detection. We believe it is the simplest implementation returning
the greatest value return in terms of both utility and learning experience. Consequentially, while implementations 2.1 and 2.3 employ a variety of interesting
image detection algorithms, our team is interested in learning more advanced AI
concepts (deep learning, neural nets, etc.) before tackling issues like these.

### Timeline

| Timeline | Tasks |
| :-: | :-: |
| 2 / 14 | Timeline Organized |
| 2 / 19 | Decide on Classifiers / Algorithm |
| 2 / 24 | Project Implementation |
| 2 / 26 | Report and Travis Build |
| 2 / 28 | Project Deadline |

## Learning Agent

The final implementation of this tracking application does not implement an active
learning agent, but relies exclusively on the simple blob detection provided by
opencv. To discuss previous approaches, the most successful attempt used a pre-trained
YOLO model in conjunction with TensorFlow and Keras in order to detect any and all
"Sports Ball" related items. However, when applied to the provided videos, the model
was horribly inconsistent in detection across frames. An advanced blob detection
solution also produced inaccurate output. The most reliable and accurate solution
was achieved using the aforementioned opencv solution, although I would attempt
to utilize imageAI given more time.

## Comparative Study

Positioning the camera behind either the pitcher or catcher necessitates the adjustment
of size to compensate for the increasing or decreasing distance from the camera.
The maximum and minimum requirements for positive matches must be adjusted to cover
the full range of distances. Additionally, the initial resolution of the video greatly
intensifies the effects of median blur, thus the original 1920x1080 resolution was
favored over the suggested 480 width at the expense of runtime performance. The
optimal position would likely be head level equidistant from both pitcher and catcher.
To track horizontal break, however, an angle of 30-60 degrees may suffice in order
to capture the relative distance between the strike zone and endpoint of the ball's
trajectory.

## Challenges and Learning Experiences

As previously mentioned, the trained AI methods resulted in a massive amount of
false negatives. As the models we utilized were primarily pre-trained, we did not
have any means by which to adjust the parameters for feature assessment or other
aspects of data classification. Again, given more time, I would have enjoyed learning
more about Scikit, imageAI, TensorFlow and Kers, but opencv yielded the most accurate
solution feasible given the time constraints (refer to teamwork section below).
Having said, this provided an opportunity to closely examine the functionality and
capabilities of opencv beyond the examples dicussed in class.

## Ethical Benefits and Implications

In this section, drawing on class discussions and readings, answer the following questions

1. What entities, businesses, organizations do you envision developing the type of the application you have chosen to develop?

As previously detailed by the Coach, both college division and professional baseball
teams utilize tracking applications such as Trackman and Saber Metrics in order
to quantify and assess a variety of performance-oriented metrics.

2. Who are the intended users of this technology?

In terms of ball-tracking in the sports context, any sufficiently competitive and
advanced sports league.

3. Who is not supposed to use this technology?

Taking the program outside of the sports context, applying object-based detection
in conjunction with autonomous drones leads to ethical debate in warfare circumstances.

4. How can the application developed in this lab cause harm?

As referenced above, when used either in conjunction with militaristic drones or
faulty self-driven machines, object detection combined with autonomy can result
in false judgements and wreak havoc.

5. What solutions could be implemented to avoid the harm or to fix the harm described above?

The refinement of classification models, stricter establishments of parameters,
adherence to proper ethical application (e.g. non-military use), and tendency to
favor supervised over unsupervised learning can all result in the mitigation of
destruction.

## Team Work

Due to extremely unfortunate circumstances, our group was understaffed during the
period in which we attempted to complete the majority of work. Both X and Y
experimented with multiple approaches to image tracking including blob detection
random tree classification through ensemble. However, due to the poor performance
of both of these implementations, Z ultimately implemented a solution utilizing
simple blob detection provided by opencv. Z also devised the video overlay
functionality and trajectory logging functionality (preserving the coordinates to
avoid the premature display of trajectory paths).
