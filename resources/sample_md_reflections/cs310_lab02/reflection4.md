# Report by

### Project Selection

The project we chose to complete is the Baseball Video Overlay and Baseball Detection project using OpenCV.

### Timeline

| Timeline  | Tasks |
| ----------- | ----------- |
|   2/18    |    Get new videos   |
|   2/19    |    Detect the ball   |
|   2/21    |    track the ball and start working on overlay    |
|   2/24    |    Finish the report    |
|   2/28    |    Overlay          |


## Learning Agent

In our program we used blob detection algorithm. This algorithm counts number of
pixels in the blob. We chose this approach because it provides additional
information about certain regions, that edge detection did not provide. The way
algorithm works is that it creates the copy of the image and then it has
recursive cases and base cases that depend on if the pixels are on or off.

## Comparative Study

We tested this program on multiple videos from different angles, as long as
the ball is visible in the video, our tool manages to detect and track it.
Our program overlays three videos. For testing the program we imported `time`,
set the time in milliseconds at the beginning of the loop and at the end before
print statements, to see exactly how long it takes to run the program in
milliseconds.

## Challenges and Learning Experiences

We decided to use `addwighted()` to overlay the videos, however we had some
challenges when implementing it. What helped us was to check the OpenCV
documentation and we figured that basically what `addwighted()` is doing is that
it calculates the weighted sum of two arrays. Figuring out what exactly each
parameter is doing helped us implement the method. Parameters passed in would
be first input array, weight of it's elements, second input array and weight
of the second elements, output array and scalar to each sum.

## Ethical Benefits and Implications

1. What entities, businesses, organizations do you envision developing the type
of the application you have chosen to develop?

Companies that sponsor the teams, or who are involved in developing Baseball.
Colleges and Universities could also be developing these features to help,
their Baseball teams improve.

2. Who are the intended users of this technology?

We think that this technology can be used by Baseball coaches to keep track of
players and help the players improve, it can be used by umpires to keep track of
the ball on the Baseball games and make it easier to observe, this tool can be
used by the Baseball players to keep track of their improvement, and it definitely
can be used amateurs just for fun.

3. Who is not supposed to use this technology?

We think that teams should not use this technology to track other teams'
pitches.

4. How can the application developed in this lab cause harm?

This tool would not be directly threatening the human mental or physical health,
However the limitations could be that this tool might be ineffective on videos
shot from certain angles where the ball is not clearly visible.

5. What solutions could be implemented to avoid the harm or to fix the harm described above?

This can be fixed by improving the precision of our program.

## Team Work

We mostly all worked together, we would assign specific task to each other,
such as to research about certain topic, to implement, and to debug, then we
would meet up outside of class and discuss our findings and combine them.
