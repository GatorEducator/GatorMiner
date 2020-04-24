## Data
Describe the data used in your project and how you obtained it. Cite (provide a link to) any sources you have used.

I used the subtitles file for _Black Mirror Season 3 Episode 2 - Playtest_ as this episode title sounded the most Sci-Fi to me.
https://www.tv-subs.net/episode-90462.html

## Text Generation
Describe the techniques used for an automated generation of your script synopsis. Cite (provide a link to) any sources you have used. Include your generated text (or its snippet) below.

All I did was write a regex statement to strip out all the formatting information in the SRT file and isolate just the lines of dialogue.

```
I'm gonna have to ask you to switch that off for now.
Okay, thanks.
You know what it's kinda like?
It's kinda like a rollercoaster.
You know what I mean?
It's like a roller coaster.
Try it, try it with me.
How tall... How tall is the Eye?
How tall... How tall is Big Ben?
Since then, I've been working as a technology correspondent for about two years now. It's been great.
Cool, that's awesome. So you do, like,
TV reports and, like, you're like...
No, just the website.
```

## Text Analysis
Describe the techniques used for an automated text analysis of your automated script synopsis. Cite (provide a link to) any sources you have used. Include a graph or textual output of your analysis.

As I am working alone rather than in a team for this assignment I figured the easiest thing to do for analysis would be word frequency. I considered sentiment analysis but that would require some kind of data to model after and I wasn't sure how appropriate using a model trained on positive and negative twitter posts would be for this application. I took the output file from the text generation and tokenized it and used NLTK's FreqDist plot to display the data below.

![freq dist](freq.png)

Source:
https://www.strehle.de/tim/weblog/archives/2015/09/03/1569

## Supplemental Production
Describe the supplemental production you have created. Include an image if relevant.
Due to the Covid-19 pandemic I have not created anything (also my 3D printer is busy making face shields!). However I was considering making a statue that depending on the direction you look at the model it would read a different word. One way saying "playtest" the title of the episode the model was trained on and "generate" for the other direction.

## Challenges and Learning Experiences
Discuss any challenges you have encountered during the work on this lab and  describe what have you learned.

I have used both NLTK and textgenrnn before so neither of those packages posed many issues, tensorflow on the other hand did. It kept throwing errors for missing DLLs and such while trying to get it to run on my RTX2070 GPU. That took 2 days of troubleshooting to get working but once it did my code ran without a hitch!

## Ethical Benefits and Implications
If you are unable to discern specific themes related to future technology use from your synopsis, provide a manually edited version of your synopsis below.

```
(Optional) Modified Synopsis
```

Then, hypothesizing on the issues highlighted in your generated (or modified) text, answer the following questions.

1. What future technology is featured in your synopsis?
Full dive virtual reality.

2. What are the potential social implications and/or ethical issues and/or regulatory challenges with this technology?
What is too real? Full dive poses many ethical and regulatory issues as full dive means full control of your body. This means that while the benefits of extremely real simulations with smell, taste, touch, etc. it could also mean things like pain. There's also the possibility of simulating situations with other people that could lead to demeaning experiences against that person.

3. What do you think might be a cautionary tale related to this technology?
This idea has been explored in books, anime, and now a black mirror episode. All show how amazing the surface of this technology could be but how it ultimately poses a huge risk for peoples safety, both physically and mentally.

4. What fictional person in the future could best illustrate this caution?
This type of technology would put a lot of power into the hands of the developer, one that could lead to death if for instance the user cannot log out of the simulation be it though a bug or intentionally.

5. What is their story?
The classic story revolves around someone getting into a full dive virtual reality universe and becoming stuck in the simulation.

6. Now, consider what a ``Light Mirror`` scenario would be for this story. That is, what benefit can come out of the  technology featured in the story and how can we work towards preventing the negative consequences of the future they envision?
Things like allowing people who cannot walk, walk again. Or allowing people who cannot travel for various reasons experience other cultures and places. It could also connect people physically who cannot do so in the real world. There needs to be limits and fail safes to allow people to leave and block things like pain.


