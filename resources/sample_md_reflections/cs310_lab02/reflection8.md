# Report by

### Project Selection

Baseball Pitch Detection - Appropriately named because it utilizes the SimpleBlobDetector
to detect, specifically, a baseball.

### Timeline

| Timeline  | Tasks |
| ----------- | ----------- |
|    Feb. 19  |     Configuration of OpenCV Tutorial   |
|    Feb. 21  |     Pipfiles, all dependencies installed   |
|    Feb. 23  |     Extensive of OpenCV Tutorial |
|    Feb. 25  |     Compilation of Video / Final Code  |
|    Feb. 28  |     Reflection |


## Learning Agent

This project used the SimpleBlobDetector algorithm to track the baseball.
This algorithm involves several steps. First the video will undergo thresholding, which converts each frame in our video to multiple binary images. Additionally, parameters can be set to specify what type of `blob`
the program is detecting, such as blob size, and whether it is darker or lighter, circularity of the blob, concave or convexivity of the blob, and the inertia ratio of the blob which is how elongated it is. The goal of learning for our program was for it to be able to detect a baseball over the course of a video. This tracking would allow us to calculate items such as speed, and ball rotation, if we were able to obtain data about the frames per second of the video, we would be able to determine speed of pitch. We anticipated inertia ratio could be used to calculate spin rate. The input for this program consisted of the video that we would be running the program on. The output consisted of wheter or not the pitch was a strike or ball, and any other info we could ascertain.

## Comparative Study

There are various metrics that affect this program, and they mainly consist of the difference between videos that we could run the program on. One metric is the positioning of the camera for each video. As this varied, the program is limited in its ability to draw the `strike zone` for each video. Another metric to consider is the quality of the video that the program will run on. We found that if the videos were too low of quality, the algorithm was unable to detect the baseball as a blob. A third environment factor is the fact that this program is limited to baseball, and using it on softball would require adjusting the parameters of the program. The program also requires a certain style of video, for example, it would be useless to run the program on a video that did not contain a full pitch, and that didn't keep the ball in view for the entirety of the video.

## Challenges and Learning Experiences

There were a number of challenges that we encountered during this lab. One of the main challenges of the lab was figuring out how to calculate pitch speed. Since the video is slowed down upon execution, using a simple timestamp would not be a reliable way to gather this data. We were concerned about the accuracy of the final result, considering that to gather this data the program needs to track the ball consistently throughout the course of a pitch. We had some trouble successfully tracking the ball for awhile, but this turned out to be the result of some low quality video and parameters that needed to be adjusted. Over the course of this project, I learned quite a bit about the SimpleBlobDetector algorithm and how to use it to track data. Interpration of this data turned out to be more difficult, however. Using a `for-loop` we were able to iterate through the keypoints during the tracking, but figuring out what to do with this data proved more tricky. I am confident in my ability to set up a SimpleBlobDetector environment after this project, and to set the parameters and path of the algorithm correctly to yield an output consistently after this lab.

## Ethical Benefits and Implications

In this section, drawing on class discussions and readings, answer the following questions

1. What entities, businesses, organizations do you envision developing the type of the application you have chosen to develop?

In this case, I believe the entities that would most benefit from developing a program like this is any baseball organization such as Major League, Minor League, College, and even Little League. These organizations stand to gain from developing a program that can provide a bunch of data for them to analyze. This this program is primarily based around collection of data, it can provide useful insight into the performance of pitchers, and whether they are making progress over a course of time. I do believe the program could be expanded to include other sports such as soccer, tennis, football, and more, with manipulation of the parameters of the program.

2. Who are the intended users of this technology?

The intended users of this technology are the data scientists that would be operating the program for the benefit of baseball coaches and teams. This means that the program doesn't require an exceptional User Interface, as would be the case if the program was created for non-technical users.

3. Who is not supposed to use this technology?

I would argue that small-time baseball teams should avoid use of the program as it seems unethical to analyze children with techniques such as this for what is supposed to be a fun sport.

4. How can the application developed in this lab cause harm?

The application here could have drastic repercussions if used to analyze and push children to improve performance in Little League baseball. This would instill in children a comparison mindset that will affect their futures negatively through anxiety and stress, and ultimately hold them back as science points to comparison as being harmful to productivity and general success.

5. What solutions could be implemented to avoid the harm or to fix the harm described above?

The best way to prevent exploitation of the technology here would be to integrate some sort of person-detector that was able to detect the age of the people within a video. This could then prevent data from being interpreted or documented if the persons were under a certain age or size. This would be difficult to integrate, for there is always the risk that the program would end up excluding certain users who are not children but simply of small stature. As such, it would have to be carefully refined.

## Team Work

Over the course of this project, we talked at great length about the best approach. We worked out a roadmap that we adhered to as best we could, although we both have busy schedules. When it came time to write the actual code, it was necessary to work from remote locations towards the success of this project. X adjusted the parameters of the code, and ensured that it would work with the specific video we selected. Y contributed towards initial breakthroughs in getting the program to run in our adapted environment, such as reprogramming the inputs. Both members discussed the strategy behind our approach, and studied the SimpleBlobDetector mechanics carefully. X wrote the reflection.
