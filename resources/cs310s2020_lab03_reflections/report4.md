## Data

The data that we used were the subtitles from the show Mr. Robot. We first downloaded the subtitles of the first season from [tv-subs.net](tv-subs.net). This was done manually and then each episode was added to a folder. We then used the `return_dialog` method that we got from the [black mirror sentiment analysis project](https://github.com/pcalderon0711/black-mirror-sentiment-analysis/blob/master/blackmirrorsentiment.ipynb) that was initially given to us. This was done to remove unnecessary data/text from the subtitles. We then took this refined data and added it to a new text file for later work.



## Text Generation

To generate this text, we utilized textgenrnn. We trained it with the subtitles that we had downloaded. We generated text directly to a text file. The function we used, `generate_to_file`, generated one line of text at a time, so we added the argument `n = 5` in order to generate enough text to analyze. The result of one run is below.


```
will the promise. I always had to be here. Im not stuffy them, thats the terting this cool. Theyvele of complication. I need to do them. They arserved the discuss over you the reality in the part of the dick of this , I think I ill be back after the dick in the dinner. I didnt want to be worried a
my decision because I dont know me traffic. Im no me. I think I have a guy the decision. I dont get a discussion. I mean<iiff me? - - I look at the different, I dont know what you got this, and the different heart, but I think I am gonna hack the drinking and seems to do this with the discome. Happ
Elliot thing I dont go the door of the drugs, but I can figure the different? I am not going to tell me they. I would be dictance to. I dont know why I for a message of my worked of the monst. I dont know, I mean, I mean. I dont be saying the right now. I didnt have all the data protocolical place.
Are my dat of the discom playing the new terry of this current thing now. I think this is alone. I dont let them. I am not glosing and the data office oh this time. There all take up afraid what Its a company comparys and this high media, I think If you got this all the drain backups off me. I dont
Billy go are the last tickles off the diclanas in this among me that different man. They be in the transition off this diffecility. I dont go this working the data like for the backups off me.</> They gotta didnt have a word. I would be handle out for him. We have to your realical melt to the dicti

```

## Text Analysis

Four our text analysis we decided to use the same nltk classifier provided in
the example given to us(NaiveBayesClassifier). We added our own training data to
train the classifier for our text data. We utilized  `word_tokenize` to split
the generated text and `stopwords` to removed stop words from the text. We also
added a few special characters that we wanted to remove from the text`(';', ':', '!', "*", "?", "<", "-", "_", ".", "/", ">", ",")`. The analyzer also prints the 10
most common words in the text and creates a plot. The classifier prints if the
text is positive, negative our natural.

Output:

`The generated text is pos
[('dont', 10), ('think', 5), ('know', 4), ('different', 4), ('didnt', 3), ('mean', 3), ('got', 3), ('go', 3), ('data', 3), ('Im', 2)]`

![top 10](writing\Figure_1.png)

## Supplemental Production

N/A this section of the lab was removed.


## Challenges and Learning Experiences

One major challenge that we faced happens to be related to our team name. Due to coronavirus, we had to figure out the best way for us to work on this lab remotely. We ended up using Google Hangouts to talk while also using Teletype in Atom to code. Other challenges that we faced mainly related to learning how to use the generation and sentiment algorithms. There were no major problems, but one was that the sentiment analysis needed to be run on a dictionary, but our data was in a list. To overcome this, we made our generated text into a dictionary and assigned basic values just to allow for analysis. Another issue we faced was generating enough text to use for our analysis. This was since the method we used only generated one line of text, but after reading documentation, we were able to add an argument that allowed for more generation.

## Ethical Benefits and Implications

If you are unable to discern specific themes related to future technology use from your synopsis, provide a manually edited version of your synopsis below.

```
(Optional) Modified Synopsis
```

Then, hypothesizing on the issues highlighted in your generated (or modified) text, answer the following questions.

1. What future technology is featured in your synopsis?

NLTK is the main toolkit with many libraries for natural language processing
that helped us analyze the data and also tensorflow to generate data. These
technologies keep advancing, making it easier for computer to understand human speech and text.

2. What are the potential social implications and/or ethical issues and/or regulatory challenges with this technology?

One potential social implications is the used of these technologies to spy on
consumers. For instance, Amazon Alexa or google home. Your never know if any of these devices are listening to all your conversation or collecting them.
Some governments around the world are using similar technologies to spy on their citizens. These are some things that we have to be concerned with.

3. What do you think might be a cautionary tale related to this technology?

Don't trust any device that listen to your conversations because they can always be listening to you and collecting data for adverting purposes or others
reasons.  

4. What fictional person in the future could best illustrate this caution?

5. What is their story?

6. Now, consider what a ``Light Mirror`` scenario would be for this story. That is, what benefit can come out of the  technology featured in the story and how can we work towards preventing the negative consequences of the future they envision?

