# Report by

### Project Selection

For our project we decided to do project one for our implementation which is the ball tracking using videos. With this, our project name is The Simple Baseball Tracking Program. We chose to do this project because we thought it would be the most challenging and interesting since most of us enjoy watching sports. The main reason we chose it is because we felt that this project would have the most real-world implications in baseball, meaning that this is a tool that is often seen in professional sports and that would likely be the most useful when compared to other tool options. With this background we figured it would be cool to change how we viewed sports now from a different perspective.

### Timeline

| Timeline  | Tasks |
| ----------- | ----------- |
|   dates    |    task 1   |
| Feb 14 | Begin working on tracking the ball software implementation |
| Feb 21 | Finish color tracking and implement it with a baseball |
| Feb 25 | Work on slowing down videos and picture enhancement |
| Feb 28 | Be able to track a baseball within a video |


## Learning Agent

Our program takes in a video as an input and then subtracts the background of the video using OpenCV functions. The video is then converted to grayscale and the background is blurred for better ball detection. Additionally, the region of interest is also increased to detect the ball earlier when it is thrown. With this, I then created a graph to track the horizontal and vertical break points. After this, we outlined blobs (ball) with green circles to track the ball by looking at the key-points of the identified ball. The goals of learning include finding the ball and tracking information about it such as speed and the horizontal/vertical break. The information outputted includes ending position, the speed of the ball, if there was a horizontal and/or vertical break, whether the pitch was a ball or a strike, and more.

## Comparative Study

The performance metrics depending on different environment settings like camera position are the ability to find the ball based on what the background of the image or video is. Once you finally get the perfect settings and way to find a ball in one camera view, when the view changes the settings would need fixed in order to pick up the ball again. For our tool to work, the camera must be positioned almost directly behind the pitcher in order to find the ball in the region of interest. Additionally, the background must not be cluttered, meaning that the background cannot be all white for example because then there may be issues with regard to detecting and tracking the ball.

## Challenges and Learning Experiences

Over the course of this lab we have had a few struggles that have stopped our progress and from making our implementation better. One of these struggles was getting our ball detection to properly work for the first week. We could not find the ball at first until we fixed the color variables. The second big issue we had during our project was trying to find the speed of the ball. We learned from this by figuring out ways to calculate distance and time, but still ran into challenges with regard to accurately getting the time elapsed during the pitch. The integrated python time libraries were originally used and then removed because it timed the running time of program components, not the ball in the air. This meant we had to find ways to track frames and the timings of these frames to find the timing of the ball. Through this we have learned to use each other for ideas and then put the ideas into code it works much better for us as a team.

## Ethical Benefits and Implications

1. What entities, businesses, organizations do you envision developing the type of the application you have chosen to develop?

I believe that the type of people that would want this technology would be any type of video watchers for sports analysts and any sort of tracking. They would use this so they can know what their team needs to work on with regard to pitching.

2. Who are the intended users of this technology?

The intended users of this technology would be head coaches, coaches, managers, and Owners, that way they can learn how to improve and try to win the championship. Fans may also be interested to see how their favorite pitchers are performing.

3. Who is not supposed to use this technology?

The person who is not supposed to use this data is the other teams in the league. If they use this video to figure out what their opponent is doing it would gain an unfair advantage instead they can only use video of their own team. Unethical people should not use this technology as they may use it to cheat or create unfair advantages within the game.

4. How can the application developed in this lab cause harm?

The application developed in this lab could ruin the integrity of the game in some ways if it is used improperly. If this content is being used during games to create an unfair advantage for one team, then there will be harmful results. For example, one team could unfairly use these videos to find out the trajectory of the opposing teams pitches. We saw an example of this with the Houston Astros over the last few years when they were accused of cheating to win the championship.

5. What solutions could be implemented to avoid the harm or to fix the harm described above?

A solution to this issue would be let an outside company do the video processes and let this company only give each team their own pictures and videos. That way they never see any other teams videos.

## Team Work

For this lab our team work always outside of the classroom since we have weird lab schedules and we can not be together. We meet 2-3 times per week in order to finish the lab and complete the code on time. Every time we work on a lab we all work on parts of the lab together. For this lab when we meet we all worked on the code together each time. Then to complete the report we divided up the seven sections evenly and then wrote them.
