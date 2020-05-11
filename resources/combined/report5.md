# Assignment

assignment-02

# Reflection by

user 5

## Data

Describe the data used in your project and how you obtained it. Cite (provide a link to) any sources you have used.
The data that we used for our project comes from the TV show "WESTWORLD" season 3, episode 3. Essentially the data that we gathered was the subtitles that were from season 3, episode 3 of "WESTWORLD". The website we obtained the data from was [TVsubs.net](https://www.tv-subs.net/subtitle-273746.html), this website has multiple shows including newer TV shows as well as notable classics. Once navigated to the website you are able to choose which episode you want as well as the season. After you select your criteria you are then able to download the transcript for your use.

## Text Generation

Describe the techniques used for an automated generation of your script synopsis. Cite (provide a link to) any sources you have used. Include your generated text (or its snippet) below.
For the part of text generation we utilized the `GPT-2` model that is based upon TensorFlow. This technique is based upon training large amounts of text that is either on the internet or you could enter your own input which we did in our case. Since, we used this model for generating text we were able to fine tune our training because it is a very complex model that is easily adjustable to suit our needs. This model also utilized the Google Colaboratory Notebook platform which made it rather simple to train our input data as well as generate text that we could use for our analysis. The link for GPT-2 on the Colaboratory Notebook can be found here; [Train a GPT-2 Text-Generating Model w/ GPU For Free](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce#scrollTo=H7LoMj4GA4n_).

Snippet of Generated Text:
```
This is a message for Nathan.

Nathan Hale.

My son.

570
00:50:46,450 --> 00:50:49,543
I haven't always been there for you.

571
00:51:55,881 --> 00:51:58,467
There's so many things I need to say.

572
00:53:03,444 --> 00:53:05,427
This might be the last time
that Mommy gets to talk to you.

573
00:53:07,444 --> 00:53:09,437
I love you so much, buddy.

574
00:53:10,444 --> 00:53:11,637
I'm so proud of you.

575
00:53:13,308 --> 00:53:15,873
I'm sorry.

576
00:53:17,592 --> 00:53:19,945
I am so sorry

577
00:53:22,608 --> 00:53:24,128
if I ever made you feel

578
00:53:24,212 --> 00:53:26,236
like you weren't
the most important thing.

579
00:53:26,298 --> 00:53:28,540
I was trying to build a life for us.

580
00:53:30,788 --> 00:53:32,017
I, uh...

581
00:53:33,001 --> 00:53:35,109
And now, I realize
that none of it even matters.

582
00:53:37,441 --> 00:53:38,478
The night that I left,
you wanted me to tuck you in.

583
00:53:39,565 --> 00:53:41,473
To sing you a song, our song.

584
00:53:42,625 --> 00:53:43,471
But I didn't have time, so...

585
00:53:47,659 --> 00:53:48,499
So I'm gonna sing it to you now. Okay?

586
00:53:51
```

## Text Analysis

Describe the techniques used for an automated text analysis of your automated script synopsis. Cite (provide a link to) any sources you have used. Include a graph or textual output of your analysis.
In order to conduct text analysis with our generated text, we utilized the Natural Language Toolkit which is a suite of libraries and programs for statistical language processing through the Python programming language. Our main focus for the analysis was calculating the frequency of each word that was present in the synopsis. The first step was to import `nltk`, then read in the synopsis by passing in a text file. After inputting the text file we were then able to use `FreqDist` to calculate the frequency of each word. The main source we referenced was [Natural Language Toolkit](https://www.nltk.org/).

Textual Output of Our Analysis.
```
[('', 33), ('I', 9), ('you', 7), ('to', 6), ('so', 4), ('a', 3), ('for', 3), ('you.', 3), ('that', 3), ("I'm", 3), ('This', 2), ('the', 2), ('of', 2), ('it', 2), ('sing', 2), ('is', 1), ('message', 1), ('Nathan.', 1), ('Nathan', 1), ('Hale.', 1), ('My', 1), ('son.', 1), ("haven't", 1), ('always', 1), ('been', 1), ('there', 1), ("There's", 1), ('many', 1), ('things', 1), ('need', 1), ('say.', 1), ('might', 1), ('be', 1), ('last', 1), ('time', 1), ('Mommy', 1), ('gets', 1), ('talk', 1), ('love', 1), ('much,', 1), ('buddy.', 1), ('proud', 1), ('sorry.', 1), ('am', 1), ('sorry', 1), ('if', 1), ('ever', 1), ('made', 1), ('feel', 1), ('like', 1)]
```


## Supplemental Production

Describe the supplemental production you have created. Include an image if relevant.
This part of the lab assignment was removed due to current conflicts, therefore we did not complete this part of this assignment.

## Challenges and Learning Experiences

Discuss any challenges you have encountered during the work on this lab and  describe what have you learned.
While working on this lab we encountered many different challenges, however we were able to overcome them. One of the main challenges we faced was finding a way to randomly generate a synopsis from our input data. We struggled with this because it was very difficult for us to generate a synopsis that actually created sentences that were comprehendible. After reviewing our options we were able to overcome this challenge by using the GPT-2 model to generate a synopsis from our input data.

## Ethical Benefits and Implications

If you are unable to discern specific themes related to future technology use from your synopsis, provide a manually edited version of your synopsis below.

```
This is a message for Nathan.
Nathan Hale.
My son.
I haven't always been there for you.
There's so many things I need to say.
This might be the last time
that Mommy gets to talk to you.
I love you so much, buddy.
I have a gadget now that allows Mommy to talk to you in the future.
I'm sorry.
I am so sorry
if I ever made you feel
like you weren't
the most important thing.
I was trying to build a life for us.
I, uh...
And now, I realize
that none of it even matters.
The night that I left,
you wanted me to tuck you in.
To sing you a song, our song.
But I didn't have time, so...
So I'm gonna sing it to you now through the gadget. Okay?
```

Then, hypothesizing on the issues highlighted in your generated (or modified) text, answer the following questions.

- What future technology is featured in your synopsis?
  The future technology that is feature in our synopsis is a gadget that allows individuals to communicate with each other forever.

- What are the potential social implications and/or ethical issues and/or regulatory challenge
  with this technology?
  Some potential social implications that relates to our technology that is featured is that it might be shocking for others if someone is able to call you forever whenever they want to.

- What do you think might be a cautionary tale related to this technology?
  A cautionary tale that could be related to this technology is that Nathan is trying to figure out how this gadget works after realizing his mom utilized this gadget to communicate with him.

- What fictional person in the future could best illustrate this caution?
  The fictional person in the future that could best illustrate this caution is Nathan Hale which is a character in out synopsis.

- What is their story?
  Nathan Hale's story is that he is curious a bout a gadget his mom used to sing him a song even though his mom stated that she will never see him again. After this event Nathan is curious and desperate to find out how this gadget works and why it's able to portray communication forever.

- Now, consider what a "Light Mirror" scenario would be for this story. That is, what benefit can
  come out of the technology featured in the story and how can we work towards preventing the negative consequences of the future they envision?
  A "Light Mirror" scenario that would be for this story is that this gadget is accessible to everyone which would allow everyone to communicate with their family members regardless of the situation they are in. We could work towards preventing the negative consequences of the future they envision by creating a law where this gadget can be used if each side of the party that utilizes this technology agrees to using this gadget for communication purposes only.
