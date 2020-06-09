# Assignment

assignment-02

# Reflection by

user 8

## Data

I used subtitles from the first two episodes of Battlestar Galactica.
I downloaded the `.srt` files from [tv-subs](https://www.tv-subs.net/) that
was provided in our assignment sheet. To improve accuracy of the data for the
use of the project, I manually removed most of the music or non verbal subtitles
that are typically in brackets. I also removed html italic tags manually.

## Text Generation

Describe the techniques used for an automated generation of your script synopsis. Cite (provide a link to) any sources you have used. Include your generated text (or its snippet) below.

For automated text generation I used [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple)
in a Google colab notebook. I chose the basic
provided training model, and trained the model for 43 rounds, getting about 0.5 loss averages.
I then generated the text seen below.

```
Be careful out there...

Be careful out there... - Akojo...

Akojo... akojo, mei no karasu. I see. I see. What? No problem. I'll put them on the line. - All right. And how long until they're gone? 10 days. - X amount. - Okay. Lets set up a patrol here... before somebody gets hurt. BALTAR: County, county. Its the Federalist, the old colonialist. Its the same as the red light district. It says its the same as nigger, but with a different spelling. GAETA: Boomer. Boomer is the new form of the old monikers. Its a civilian-led protest, but actually a federal protest. Thats just great, isodating a government. Really? [Chuckling] We had a civilian-led civilian protest... a federal one. It was called the Boomer, but theyre the Cylons. Theyre the Cylons, aren't they? Theyre the Cylons, belong to the next generation. BILLY: I want us to have a child, BILLY. That, and a child, and a mighty, mighty great, mighty great, mighty great... and theyll make us. BILLY: You know what? I want us to have a child, too. BILLY: I want us to have a child, too. See, the Cylons look like us. Theyre the Cylons, aren't they? Theyre the Cylons, belong to the next generation. BILLY: You dont know how relieved you are to see us, do you? A little sad, dont you? Im sure some day if youre a good Cylon hell reward you... with a lovely little walking toaster of your very own. BILLY: You cant be serious. - Its Dr. Amarak. - What was that? Im so sorry for interrupting you while you were speaking. You were just saying? I was just saying that a Dr. Amarak... - has requested to speak with the President... regarding a mysterious anomaly... that has afflicted all of us. - Id bephalting you... for one minute at a time. - Is that your Dr. Amarak? You were saying something about something? I was just saying that... a few minutes ago... the President requested to speak with the President regarding a strange anomaly...... regarding which he has requested that we... ask him a few simple personal... and professional... questions. A few days ago, the Cylons... escaped from their servitor ship and began to attack the fleet... taking advantage of the current time break... to continue their attack on the President. Is that what you were saying? The truth is, the Cylons still lurk around the bowels of our FTL port, holding a grudge that we must cut off their heads if they want to survive. - And why are they holding a grudge? - Because theyre Cylons. Theyve been tracking down Cylons all along. A Cylon maybe tracking them, but theyre not showing up. So theres not a whyset wayward BLL... to jump. - Dr. Amarak. - Yes. It is. BILLY: The Cylons still lurk around the bowels of our FTL port. BILLY: Theres a Cylon fleet waiting to jump. Theyve got ships that destroyairlyreaching our fleet. Theyve got bombers that killfast... butarent showing up. Are you there? Yeah, Im here. How about we jump? Callyx: Lets get some of the old men and women in the party... into a coma. Callyx: Ms. Gaeta. Gaius. Gaeta: Well go. Someone hasto jump. Someone hasto jump. Gaeta: We havena jump. GAETA: Boomer. GAETA: Sir. GAETA: ...are recognizing the fourth command. There are 446 ships remaining in our bow... from across the universe. We have no idea when they left or where they are headed. What are we doing here, Gaius? Go back to Raven Rock. Its all wrong. There are 446 people aboard this ship. Why are we showing up? We had a medical error and our FTL drive is down. There may have been other causes... such as the extinction of large swaths of the old world, we do not know the answer to. help us God. Or do you? God is a complex system. Coincidental, serendipitous events... are bound to occur. Happens all the time. Amen. FRASER: [Over PA] Landing base Team Alpha, check three. No. APOLLO: Twelve more contacts, all feeling the effects of the last ship... have passed
```

## Text Analysis

To complete the text analysis portion of this assignment, I used a previous assingment
that rated the sentiment of words in a file and provided an overall score. Each sentiment
word and its rank is stored in the `sentiment.txt` file. Below is the overall calculation
based on those sentiment words.

```
Score by summation : -29
Number of sentiment words: 222
```

## Supplemental Production

Describe the supplemental production you have created. Include an image if relevant.

This part of the lab assignment was removed due to a move to remote education.

## Challenges and Learning Experiences

The largest challenge I faced at first was setting up `tensorflow` and `textgenrnn` locally
on my device. After stuggling with that for awhile, I was able to get both working in a
Google colab notebook. However, `textgenrnn` would not produce coherent words with the
training model I had choosen and the amount of data I had. So, I chose to use a different
tool tot generate my text, which worked well. I feel that through this challenge I
further understand the importance of choosing the corrent training model for the data
you are using. I also stuggled with knowing how long I should train my model. It took about
an hour to get to round 43 and I was unsure as to when the training was going to stop on
its own or if I was supposed to stop it myself. This I hope will come with more practice
and with more knowledge of the tools I am using.

## Ethical Benefits and Implications

The overall theme of Battlestar Galactica is that there are two
societies, one human, one robot. In this scenario, AI has evolved to the
point of being self sufficient. While this is an example of "perfect AI",
it is something many people think about when they think about AI in general.
Will it be able to be controled?

Then, hypothesizing on the issues highlighted in your generated (or modified) text, answer the following questions.

1. What future technology is featured in your synopsis?

    Self sufficient AI.

2. What are the potential social implications and/or ethical issues and/or regulatory challenges with this technology?

    There are major social implications with self sufficient AI. Is this AI
    allowed to exist? If so, does it exist within society normally, are we
    aware of what is AI and what is human? Is anyone able to regulate this
    technology?

3. What do you think might be a cautionary tale related to this technology?

    There is a point where the technology overcomes the need for any type of
    humanity and can exist completely on its own.

4. What fictional person in the future could best illustrate this caution?

5. What is their story?

6. Now, consider what a `Light Mirror` scenario would be for this story. That is, what benefit can come out of the  technology featured in the story and how can we work towards preventing the negative consequences of the future they envision?

    While we have discussed the very real challenges to ethical AI, I'd say
    self - sufficient AI, if ethical, could be used positively in many ways.
    However this all still depends on what we as a society can agree on as
    "ethical".
