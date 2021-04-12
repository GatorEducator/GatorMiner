# Report by

### Project Selection

We will do a mixture of projects one and two. If we can detect the
baseball movement it won't be difficult to predict where it will
land. With the combination of both projects it will make the
project more interesting. We will implement a CNN in the
training part of the lab.

### Timeline

| Timeline  | Tasks |
| ----------- | ----------- |
|   2/14/20    |    Start    |
|   2/17/20    | Implement object detection in videos |
|   2/21/20    | Train our predictive model |
|   2/24/20    | Verify model with sample videos. |
|   2/28/20    | Implement the overlay "if possible" |

|   dates    |    task 1   |



## Learning Agent

We used some pre-trained deep learning models to complete this project. We used the `yolo3_mobilenet1.0_coco`,
`ssd_512_resnet50_v1_voc`, and `simple_pose_resnet18_v1b` neural network models to detect the
people, skeletal mesh, and sports ball or baseball. The `yolo3` neural network model
tracks the people and puts a skeletal overlay over the detected people. The `ssd_512`
model is used to detect the sports ball. The `pose_resnet` network model
is used to apply the skeletal mesh to the people. The output of these deep learning
models is the detection and labeling of the discovered objects. It will only show
objects when the confidence is above `50%`. The Convolutional neural networks models we used
are pre-trained, which contains weights for 600 (`yolo3_mobilenet`) to 10000 (`ssd_512`) different
objects. For each frame of the video, the pre-trained neural network models will try predict the
possible objects by locating bounded boxes in `bbox` variable. The confidence score will also be
calculated for each possible detection in `scores` variable, associated with the object type stored
in the `ids` variable. The detection with `scores` higher than 0.5 will be presented on the image
after we fit the pre-trained model. Since these variables are in NDarray type, we can use
`np.squeze()` to reduce the unnecessary dimensions. For the pose detection we
used the `yolo3_mobilenet` to detect where the person is then within the `bboxes`
we apply the `pose_resnet` model to detect the pose.

## Comparative Study

In our comparative study we evaluated the metrics for different environmental
settings by using the provided video clips with and without the net. When using
the video clip from a different perspective our person and skeletal mesh worked
correctly, but we couldn't detect the ball due to the speed at which it was
thrown and the resolution of the video. We then used a different video format to
see if the increased resolution would yield better detections. The resolution
didn't change and the ball was too fast to be detected. Although more
people were detected. In conclusion the resolution of the video is correlated
with the improved detection of the people and sports ball.

```
python src1/baseball_dt.py -v src1/Videos/pitch01.m4v -fs 1

The ball traveled from: [
[314.59766]
<NDArray 1 @cpu(0)>,
[370.44693]
<NDArray 1 @cpu(0)>] to [
[314.895]
<NDArray 1 @cpu(0)>,
[373.3154]
<NDArray 1 @cpu(0)>]
The distance is
[80.83187]
<NDArray 1 @cpu(0)>
It took 0.01694915254237288 seconds
Sports Ball Speed 11689.08
```

```
python src1/baseball_dt.py -v src1/Videos/pitch02.m4v -fs 1

The ball traveled from: [
[264.13882]
<NDArray 1 @cpu(0)>,
[378.2546]
<NDArray 1 @cpu(0)>] to [
[304.846]
<NDArray 1 @cpu(0)>,
[434.42258]
<NDArray 1 @cpu(0)>]
The distance is
[185.43295]
<NDArray 1 @cpu(0)>
It took 0.4576271186440678 seconds
Sports Ball Speed 432.9288888888889
```

```
python src1/baseball_dt.py -v src1/Videos/pitch04.m4v -fs 1

The ball traveled from: [
[340.34286]
<NDArray 1 @cpu(0)>,
[518.62524]
<NDArray 1 @cpu(0)>] to [
[340.1992]
<NDArray 1 @cpu(0)>,
[518.2746]
<NDArray 1 @cpu(0)>]
The distance is
[251.98325]
<NDArray 1 @cpu(0)>
It took 0.1864406779661017 seconds
Sports Ball Speed 1062.6436363636365
```

```
python src1/baseball_dt.py -v src1/Videos/pitch05.m4v -fs 1

The ball traveled from: [
[308.6103]
<NDArray 1 @cpu(0)>,
[450.02173]
<NDArray 1 @cpu(0)>] to [
[357.95438]
<NDArray 1 @cpu(0)>,
[522.459]
<NDArray 1 @cpu(0)>]
The distance is
[232.8254]
<NDArray 1 @cpu(0)>
It took 0.01694915254237288 seconds
Sports Ball Speed 11689.08
```

## Challenges and Learning Experiences

The first challenge we had was using a neural network that would update the
image by at least one frame per second. Initially we implemented a `Mask_RCNN`
deep learning model but unfortunately it was extremely slow due to the
structure of the network. Our own tests indicated that it could take anywhere
from 36 seconds to 46 seconds. To try and get around the speed problem
we narrowed the classes to just the sports ball,
but this didn't make it run faster. We then tried out multiple neural networks
but we decided against using them because it couldn't detect a `Sports Ball`.
After implementing the `yolo3_mobilenet`, `yolo3_darknet`, `ssd_512` neural networks
our program ran as intended.

The second challenge that we faced was working with the `numpy` arrays to
calculate the distance and determine the threshold at which we should
consider that the ball has been thrown. To solve the threshold problem Lancaster
implemented a conditional logic structure that could determine when the baseball
was thrown and caught. After that we needed to determine how we could calculate
the speed at which it was thrown. Initially we didn't know how to abstract the data
and had to extensively research the topic to get the data that we needed. Lancaster
researched Euclidean distance and implemented the code to calculate it. We then
calculated the distance based on the known distance of `60ft 6in` between the
thrower and the catcher.

## Ethical Benefits and Implications

1. What entities, businesses, organizations do you envision developing the type of the application you have chosen to develop?

We envision that amateur and professional sports teams could use and expand
the program that we have developed. In order for other sports
to utilize the technology the deep learning model would have
to be trained using data containing a soccer ball or a foot ball.
By training it using data for the desired sport it would make
the model more effective at detecting the sports ball.

2. Who are the intended users of this technology?

The intended users of this technology would be Baseball sports teams. Potentially
other sports teams could use the program but it would have to be adjusted for
accuracy for games that don't use balls such as fencing or horse racing.

3. Who is not supposed to use this technology?

There are ethical concerns about the military using
the technology to make them more effective at fighting. For instance if a group
got their hands on our program they could change it to evaluate how
well they could throw round objects such as grenades. 

4. How can the application developed in this lab cause harm?

The application could harm people if it were used to evaluate the effectiveness
of fighters. Instead of detecting a sport's ball it could be changed to detect
fists and track the speed of punching. In addition to the the skeletal mesh
could be used to rate the effectiveness of a persons pose while punching.

5. What solutions could be implemented to avoid the harm or to fix the harm described above?

A solution to the previously mentioned problems would be to restrict the access
to the program so that only a few groups of people can use it. In addition
to that we could only train the model to detect objects like a sports
ball, baseball glove, and a baseball bat. That way it could not be easily
changed to fit a nefarious purpose.

## Team Work

We met and worked together in Alden. In order to avoid merge conflict, we only have one person
to make changes at one time. Additionally, since it takes a while for each frame of the image to
fit pre-trained models, we have one computer run the video, and another computer edit the code.
