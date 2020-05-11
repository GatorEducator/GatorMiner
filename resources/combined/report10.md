# Reflection by

user 10

## Data
<!-- Describe the data used in your project and how you obtained it. Cite (provide a link to) any sources you have used. -->

Our team first thought about the type of show we were interested in using to train our model. We figured that NCIS would be an interesting
show because it displays new technologies in a fast-paced crime setting, which would help us reach our goal of generating a synopsis for a
science fiction show. With this in mind, we eventually found a `.srt` file for an episode of NCIS on `tv-subs.net` which we then
downloaded to use for our project. After downloading the file, however, we realized that we would need to convert this `.srt` file to a
`.txt` file for the dialog to work with `generator.py`. To do this, we wrote code (which has now been removed from the project as it is
unneeded, it appears in old commits) to save the returned dialog from `return_dialog()` in `analyzer.py` in a text file called `NCIS.txt`.
Now we had properly formatted data that could be used for our project.

Source: [NCIS Episode 17 on tv-subs.net](https://www.tv-subs.net/episode-114980.html)

## Text Generation

<!-- Describe the techniques used for an automated generation of your script synopsis. Cite (provide a link to) any sources you have used. Include your generated text (or its snippet) below. -->

When it is time to generate the text for our script we needed to use textgen. We have included a separate NCIS.txt file that includes all the information about that particular episode.
The program generator.py is responsible for training the words in the text file with textgen. During the implementation of this step we had trouble actually getting the generated output
after generator.py was finished running. The line of code that prints the output of the program to generate_text.txt is important because it now the trained data that we can use for our analysis.

```
Generated Text:
------------------------------------------
 the Both officers control the comparia on the share of the commander, the control officer toward. I thought my skin give me Wheraptabilies commanderland shoot it. It down that that she do the first time of shutted the commanders? I was doing the commander every time of the compart of the is gonna k do you know where that we was tower some she dond of her shooting there? here to complained that they want to say, I said my and maybe it. We get to do that that thinks the way me. I dont know it would he look? I know that the subricary areas should the shop? It was surgery to the commander one car to the same side got what a tard is the situation me she dont be she done her a she doesnender was their dragged so I survive without be all the can I dont be interrupt that she ready took that she was surea she dont be she done this subreddit. I was she dont talk to the satures to the same shutter officer share any shopping to it. No, Okay, I tho she dont should she shoulder than that she dont be scalped the commanders to a scream. I think that my side to the crash? I said that she says I thought he looking she dont a search? I dont do to get a compart officer and she do some she do not a house of the problems that she dort that that do it here. I know what the hell is that she deckans that up. Any other had the commanders to the next. I build a head. I made a scound the commander me. Everybody says that And she build the command to the commander. But I think a short old is that a couple. We will down, we had to shoot down. I thought the hell and a compash officer call she can Find out the subred commander. I dont though. I was probably commanders that? I was just too shooting this. I thought it was, she was this message that her last shes, I dont took too should the commander before the car she did this weeks? It doesnt out th it we had to okay, I dont took the subred and she dont travel through their she just she ready to she she shes down on the marked a room. I know. I okay and the sherd is the compart officer and she was the companta did that easy? I can read the helms out the school support, still that thought you k I saw a weird color=D#00 to the "I did the commander in Weeks" took he dont plan a compash thing. Wet done this that he made? I can get the Flood officer stranges to the course to learn the share and probably she say your commanders? I have a smash. I found that she do you know what I thund they kn commander shoots that shop say we she she she shoutded any season, so you know where that? I dont ship the commanders to the mail. Its a flannoud thunder in my second of the ship the commander. I dont shoot that is that the last night. So you know what it is about the command to know about the cute ready to a compash to she should he plan. Well, The car offing that everyone? I shoulder shes those officer and the good thing? I dont know what the compant. Weeks have the ones could not every time I dont she shoutdly so she dont try to those was out the ready officer officer suspiats talk to took here. I see your a source on a source officer she dont break the districal than the last door shows that commander. No she saw a tir that ship to the compart officer command that the subricary car, that we dont took for the oiland that saying a surprise of the problems that she driver incredical th what it is the deck is the compartmand to the doughs officer. I loved though. I thought it was the compant or someone should? I know. I needed that we say that she said that she do the commanders leave. What is the compart officer? Any subscrible steam. We made a problem in the commatic episode?" W car commanders are the compart officer color=triday. I did the streaks all she dont she she can be all the commander stream. Well, I said that scientistical comtutration was she shouldnd down. Thats she dont think the subtle is commanders where its through the same car to she shoulder that she do t the Commander share to talk to the compart on the shop. I dont show me. Commander shoots that she do Flowes the commanders to here to starboary to she she shoulden the car tell officer officer before the cat as a survive did like. I had just the same cause your sea in a server I see what are something tomarde. I dont know what it its a ship officer and she do that shop in those she not she even ha my car can bother. I thought it was in the subrest image. I made. I just come to her find me. I did the both off these she doesnt to the is a second-officer officer. Well, but Lieutenant Commander on because for not she and dont be we survive? I dont have a surverance off. I had the tower. I though I sandered the commanders where are she was on the commander. I talk to the way and gonna know where? I can do two she dont read herr. I saw her officer shop, I dont think that. I can say you got the aircraptance you shoulden the commant that owners on the comparting commander is the compart suicid one does it come? I need, I arrest to she do that she do you thought that she do you made your compant to the control today. Well, I thought I did improved not to stare that the other officer locks the commander your your senate better for what the tell you shoulder the season to make the compart o a ship old talk to the snow shooter to the commatic beach that was tell you to she saw ah me. We need the compart. Any self- Weeks dont us the car to she shouldnd her scalp and I dont be actually a mark to those password. I thought you this is her every time that she dont though it was too so we we the trainer took the commander closes that she says is transor that they she dont think about the commander idea the hell the to-mother that car is that? I was a lot officer commander. I dont "I should you know where" that she do this. What she do we know that the showing? We would have too drove? here that is commanders shoutd commanders and they shoulder your best she dont be shooting that I do the way. You know where are survive the backs the commander local command through the three weeks to she shouldnd he didnt help she that is she was under thank you can took. I got a commander on the she dont thank you to the down. It isnt surgery to the commander here. We were they saying you the compart of the. I thould her Commander Commander shouts she dreaks today. Compares through this. Commander took the commander. I thought a some steam. I was surgery to she shouldnd a commander that she's so I dont know wherh, I dont put she been into the safarity on through officer. It was told the commability officer at that a share its lock on Will the top commanders from she dont think that we took me. I dont bothe the shop. I dont have she you shout the course? I dont should we have too ready. I was out officer and maybe it was that she dont find the command decider that she do you know where? I dont want to do to s a she do that the compart officer can be she done that she during her shooting to her she do that. I dont town a secret for lock. I be she dont ibade its into the word. Well, I are, she doesneques the way. I think that the crashes that your compartmand shoot suicide shop. I dont do to that shop sho the guy took there. Got it. the commander shoots a season to make the commander to the commander shop and she do? I just have the commander at the commanders took she survive the commanderrolida doctors talk that that she do that she do shes on your sealer to get a sund to the compart officer to a

------------------------------------------
```

## Text Analysis
<!-- Describe the techniques used for an automated text analysis of your automated script synopsis. Cite (provide a link to) any sources you have used. Include a graph or textual output of your analysis. -->

We use SentimentIntensityAnalyzer to analyze the NCIS dialog in order to get a negative
or positive emotion. We included a for loop with a nested if-else that measures the
polarity list and prints out a sentence of whether it is positive or negative and
also prints the polarity number. The sentiment is on a scale from -1 to 1 and thus,
any value below zero results in a negative polarity and any value above zero is
a positive polarity. We have this sentiment analyzing the text that is generated
from our `generator.py` file. We have it read through that file and measure
the sentiment polarity. It reads through the file by opening the the text file,
splitting it into strings, and measuring the polarity and saving it into a list.
Along with our sentiment analysis, our generator outputs a temperature with each
paragraph it displays. These temperature range from 0 to 1. The higher the temperature
the more positive the paragraph will be. By doing both analyzers, we are able to
get a cohesive sentiment on the paragraph as a whole and then individual ones for
each separate group. To see the textual output that is analyzed, go to `generated_text.txt`.
The sentiment that was produced when we ran it was

```
-- This episode contains positive emotions.
-- The sentiment rating: 0.982.
```

## Challenges and Learning Experiences
<!-- Discuss any challenges you have encountered during the work on this lab and  describe what have you learned. -->
Our biggest challenge was understanding the code we were using and knowing how
to properly run a sentiment analysis on it. Initially when we saw the code from
the given websites (on the assignment sheet), we were unsure of how it was actually
working. We knew we need to find a file of subscripts but how it was suppose to
work, we were unsure. After reading through and breaking up the code line by line,
we were able to understand what was happening. We then went and added our own
process of sentiment analysis. The only problem with this was that it was on the
whole text file/dialogue rather than our generated text. It seemed easy to transfer
our thought process but in reality, it gave us some problems. We struggled with it
actually being able to grab the code and read it from the command line interface.
Consequently, after some research we found that we were able to generate straight
into a file. WE then just needed to open that file, which allowed for the sentiment
analysis to occur on the generated data. From our first issue with our analyzer,
we learned that if you take the time and break apart the code found, it can be useful
and you can add valuable functions. Our second challenge, allowed us to learn how
to run an analysis on generated text that was within our command line interface.

## Ethical Benefits and Implications
<!--
If you are unable to discern specific themes related to future technology use from your synopsis, provide a manually edited version of your synopsis below. -->

1. What future technology is featured in your synopsis?

There don't seem to be any specific future technologies to be found in the synopsis but there are a variety of existing and modified
technologies mentioned. One technology that is mentioned is the idea of a `subreddit`, which is an online community usually based on a
centralized topic. The synopsis generated by our code mentions `subreddits` a couple of times and when mentioned, they seem to be in the
context of talking with police officers. With this, it seems that the future technology featured in our synopsis would be regarding a
tool/website with subreddits that promote communication between officers and civilians to stop crime.

2. What are the potential social implications and/or ethical issues and/or regulatory challenges with this technology?

Our synopsis generated text about a technology that related the usage of subreddits to the police. There are a number of social
implications that could come with this tool which would include a possible strengthening or weakening of relationships between the public
and police, less overall crime, and more. There are also some ethical issues that come with this, such as civilians reporting information
to the police out of emotion or the police becoming too close to (certain) civilians which could result in a conflict of interest.
Regulatory challenges associated with this technology might come in the form of regulation to stop the police from sharing too much
information with the general public.

3. What do you think might be a cautionary tale related to this technology?

One cautionary tale related to this comes in the form of Melvin Colon in a [CNN article](https://www.cnn.com/2012/08/30/tech/social-media/fighting-crime-social-media/index.html). He was arrested after making
incriminating remarks online which he thought was private. Additionally, the article mentions that police often look at public information
and sometimes create fake online identities to befriend suspects and view their private information. If a `subreddit` was used for police
and civilian interaction, civilians will have to be wary what they post.

4. What fictional person in the future could best illustrate this caution?

One fictional person in the future that could best illustrate this caution would be a civilian we will call Jack. Jack was involved in
crime and after leaving this lifestyle, got himself into some unexpected trouble. We will discuss this fictional story more in the next
question.

5. What is their story?

Jack was involved in a gang that was smuggling illegal firearms. After he got mad at other gang members over what he felt was an unfair
share of the profits, he left the organization. A few years down the line and now living a life free of crime, Jack decides to go onto the
new police `subreddit` and report his former gang out of spite. This results in the police investigating Jacks claims and arresting the
gang. However, during the investigation the other gang members tell the police Jack was involved in the gang and evidence is found that
supports this theory. Now Jack is being investigated by the police as well and is subsequently arrested for his former role in the gang
despite living crime free for years.

A police-civilian subreddit could help to stop crime but may also have unintended consequences for those using it.

6. Now, consider what a `Light Mirror` scenario would be for this story. That is, what benefit can come out of the  technology featured in the story and how can we work towards preventing the negative consequences of the future they envision?

Benefits that could come out of this technology include a strengthened relationship between the police and the public in addition to
reducing crime. Some negative consequences of this technology could be the police sharing classified information with the public or
civilian privacy could be breached by the police. These negatives could be mitigated by placing regulations on what information the police
can share on the `subreddit` and by educating civilians about being mindful of the information they put online.
