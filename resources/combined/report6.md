# Assignment

assignment-02

# Reflection by

user 6

## Data

Describe the data used in your project and how you obtained it. Cite (provide a link to) any sources you have used.

The data that we used in our project came in the form of video source code, which we drew from to complete the lab. We stored the data that we obtained in multiple files that were contained in the `data` folder. The output of the program is also stored in the `data` folder. We obtained it from an `opensubtitles` website that stores the scripts for many movies and television shows. The following links are the sources that we used to complete this laboratory assignment.

Link to sources:
- [Source Text](https://www.opensubtitles.org/en/ssearch/sublanguageid-all/idmovie-136913)

## Text Generation

Describe the techniques used for an automated generation of your script synopsis. Cite (provide a link to) any sources you have used. Include your generated text (or its snippet) below.

The default configuration using textgenrnn was employed. With the subtitles being provided in very short fragments, a total of 50 epochs were used in order to generate moderately cohesive dialogue that retains the stylistic properties of the source material. In terms of the input material, a file containing the collation of dialogue from every episode (without foreign and non-Unicode symbols) was used. As per the default configuration, snippets as concise as the original input lines were displayed at various different "temperatures" in order to cover a diverse range of possible generated snippets.

```
1834/1834 [==============================] - 280s 153ms/step - loss: 0.7286
Epoch 41/50
1833/1834 [============================>.] - ETA: 0s - loss: 0.7168####################
Temperature: 0.2
####################
I see.

I see.

I was so happy to save Mayuri without the IBN 5100.

####################
Temperature: 0.5
####################
So what did you get?

I don't know what was in the man.

No, I guess I was still theoretically,

####################
Temperature: 1.0
####################
Next up, I'll have to check my father's far,

Right here. Noticed to...

The D-mail has survived with memories...
```

Links to sources:
- [TextGenRnn](https://github.com/minimaxir/textgenrnn)

## Text Analysis

Describe the techniques used for an automated text analysis of your automated script synopsis. Cite (provide a link to) any sources you have used. Include a graph or textual output of your analysis.

The default pipeline provided by the Stanford NLP package was employed. This package tokenizes a sentence and analyzes both words and word fragments based upon their function within the sentence, their governing word, and relationship to the dependent word.

```
Example 1:
The             the             DT      2   det
D-mail          d-mail          NNP     4   nsubj
has             have            VBZ     4   aux
survived        survive         VBN     0   root
with            with            IN      6   case
memories        memory          NNS     4   obl
...             ...             .       4   punct
Example 2:
Even            even            RB      4   advmod
if              if              IN      4   mark
he              he              PRP     4   nsubj       
looks           look            VBZ     9   advcl
here            here            RB      4   advmod
,               ,               ,       9   punct
I               I               PRP     9   nsubj
'll             will            MD      9   aux
get             get             VB      0   root
me              I               PRP     9   iobj
a               a               DT      13  det
time            time            NN      13  compound
machine         machine         NN      9   obj
.               .               .       9   punct
Example 3:
Wh              wh              NN      0   root
-               -               ,       1   punct
Where           where           WRB     1   appos
are             be              VBP     3   cop
there           there           RB      3   advmod
?               ?               .       1   punct
```

Links to sources:
- [Stanford NLP](https://stanfordnlp.github.io/stanfordnlp/)

## Supplemental Production
Optional: Describe the supplemental production you have created. Include an image if relevant.

This part of the lab has been revoked.

## Challenges and Learning Experiences

There were several challenges that we had during the completion of the third lab. The first problem that we had during the completion of this lab was that we didn't know what tools that we wanted to use to accomplish the guidelines set from the lab. After investigating the multiple tools suggested to us in the assignment sheet we were then able to decide what we wanted to use. We ended up using `stanfordnlp` and `textgenrnn`. We also had a problem where we didn't have an idea about what source text we wanted to use for the project. But after talking among ourselves in the group we decided on using an online script of a movie related to the genre of `Black Mirror`. As a group we didn't have many problems working remotely since the semester was moved to online. We learned how to use NLP tools based on the chosen sample text and how to work remotely in an effective manner.

## Ethical Benefits and Implications

The main benefit of these technologies is that it can automatically generate potential messages that you would want to send based on your previous writing samples. This would reduce the time to communication, and would make life easier. While it would be very nice to be able to automatically generate text for any given occasion, that would not make the text generated genuine. Not only is it not ethical by any means, it could also be risky.  As no computer program is perfect, the same would hold true to a program like this. The generated text could be incorrect or just rude to the recipient. If this was the case then it would be better to use the AI as a guide of where to take the message. While convenient it would take away the human or polite aspect of communication. And if both sides are responding with an AI then nothing would come of the conversations at all. There are also concerns about how identity fraud could be committed. Imagine if someone sampled your writings and created fake messages and sent them to your boss, family, and professors. That could cause havoc. Therefore NLP technologies use should be used cautiously by ethical professionals.

```
(Optional) Modified Synopsis
```

If you are unable to discern specific themes related to future technology use from your synopsis, provide a manually edited version of your synopsis below.

Since we have configured our text generator to resemble concise subtitle fragments, we did not produce a singular, cohesive synopsis paragraph. However, the below contains a collection of fragments pertinent to the plot of the anime:

```
Line 1169: I was so happy to save Mayuri without the IBN 5100.
Line 1187: The D-mail has survived with memories...
Line 1205: It's not that you succeeded!
Line 1283: I can't even see the experiment.
Line 1312: I was so happy to be our experiments.
Line 1321: That was a special cell phone, too.
Line 1339: I can't even see the lab and change the future.
Line 1350: Even if he looks here, I'll get me a time machine.
Line 1352: I have a use to see it a message.
Line 1359: Save Mayuri.
Line 1386: If you like failure... But...
```

Then, hypothesizing on the issues highlighted in your generated (or modified) text, answer the following questions.

1. What future technology is featured in your synopsis?
The future technology that is in this synopsis is the time machine in line 1350


2. What are the potential social implications and/or ethical issues and/or regulatory challenges with this technology?
The implications of this technology would be mostly negative as changing the past or going to the future creates a paradox of sorts.  For instance, someone goes back in time to save someone, and them being saved changes the future forever, preventing the person from going back to save them, and this loops on forever.

3. What do you think might be a cautionary tale related to this technology?
There is no way to know the consequences of meddling with time.

4. What fictional person in the future could best illustrate this caution?
A scientist who makes a time machine to go back in time to save a loved one.  No matter the consequences.

5. What is their story?
The scientist who back in time unintentionally is the reason why that person dies.

6. Now, consider what a ``Light Mirror`` scenario would be for this story. That is, what benefit can come out of the technology featured in the story and how can we work towards preventing the negative consequences of the future they envision?
This technology can still be useful for many purposes.  For instance, this technology would allow for completely accurate records of history, or perhaps a look into some future technologies if the time machine can go that way.  With this technology there must be an extreme amount of planning before it is used in anyway shape or form, due to the large amount of damage it could cause.  Many government policies and fail safes would have to be implemented in order for this technology to be considered safe.
