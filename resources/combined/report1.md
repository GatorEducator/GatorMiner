# Assignment

assignment-02

# Reflection by

user 1

## Data

The data is going to be subtitles of a TV show "Black Mirror". I downloaded the
subtitles from [link](https://www.tv-subs.net/), the stored the file `sample.txt`in `src`.
To generate a single string out of the subtitles I used `return_dialog` method
from [link](https://github.com/piocalderon/black-mirror-sentiment-analysis).
This method takes file name as an input and it returns a single string
that contains subtitles as a paragraph.

## Text Generation

For the text generation I used GPT-2-simple and Google Colab. I followed the guides in the
notebook([link](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce#forceEdit=true&sandboxMode=true&scrollTo=sUmTooTW3osf)). First I created my copy in the
drive. Then I uploaded the file `sample.txt` to my Google drive. I updated the
file name in the code in my copy of the notebook.
And then ran the code for finetuning. What this
code does is that it loads the data set and trains for certain number of steps,
that is one of the parameters and can be modified, but I kept the default.
When finetuning I coould also see the output. According to Max Woolf ([link](https://minimaxir.com/2019/09/howto-gpt2/))
In the output if the average loss stops decreasing it means that additional
training may not improve the model. I observed that the average loss in my output
kept decreasing until reaching 0.01. After the model finished training I ran
the cell for saving it to the drive. Then I downloaded that drive locally and
then followed the steps in the `README.md` for text generation([link](https://github.com/minimaxir/gpt-2-simple)). Since my model
was already trained, all I had to do was to load it from the file `/checkpoint/run1`,
that's where the generated model goes by default. Then I called the `generate`
function. I passed in parameters for
`length`, `temperature`, `top_k`, `top_p`, `prefix`. The `temperature` was
recommended to be between 0.7 and 1.0. So I changed it multiple times and
observed the output and finally kept 1.0. For `top_k` I set 40, which would
limit the generated guesses to top 40 guesses. The output of the `generator`
is below. If one runs `generator` again content might be different.

```
Future of technology. Its a brave choice. Im sorry, but I... I couldnt do it.
OK, I was going to play some redos from the Fraser O days. Stuff from last
night, depressing and fun. You know half the organic memories you have a
junk, just not trustworthy. Colleen works in Grain development. With half
the population you can implant false memories, just by asking leading
questions in therapy. You can make people remember getting lost in shopping
malls they never visited, getting bothered by

```

## Text Analysis

For text analysis I decided to do POS tagging. For that I used `nltk` library.
First I tokenized the generated text using `word_tokenize()` function. Then
`pos_tag()` function tags the tokens and returns as a list of tuple, with
token and respective POS. After that I decided to better visualize the
output color the tokens depending on their POS. For example nouns would be
colored cyan, verbs green and adjectives red, I left all the rest unchanged.
For coloring the output I used
ANSI escape codes([link](https://ozzmaker.com/add-colour-to-text-in-python/)).
Each color has its code, for example red: `31`, cyan: `36`, green: `32`. The
colors are given at the time of printing out.

![Logo](tagged_text.png)

## Supplemental Production

N/A

## Challenges and Learning Experiences

As I mentioned above before generating the text I trained the model in Google
Colab notebook, and then saved it to the drive, First I wanted
to try text generation in Goolge Colab, but it would fail all the time, so I
downloaded the trained model and then generated the text locally. That seemed
to work, but I am still not sure why it wasn't generating in the notebook,
using almost same steps. I suspect that it had something to do with loading
the file form Google drive.
I also had a challenge when trying to color the tokens based on the POS. So
as I mentioned above the `pos_tag()` function tags the tokens and returns as a
list of tuple. So I decided to iterate though the tuples and with
conditional logic find tokens with same POS and color them, and return as
a list. But I didn't want to have a list of words but colored text. Every
time I would print list items did not have colors. Later after research I
discovered that colors can be applied to `String` only during printing.
So I used `join()` method to return list of word as a text and print them.
That seemed to work.

## Ethical Benefits and Implications

```
(Optional) Modified Synopsis
```

Then, hypothesizing on the issues highlighted in your generated (or modified) text, answer the following questions.

1. What future technology is featured in your synopsis?

In the synopsis the technology can alter people's memory, or implant false memories

2. What are the potential social implications and/or ethical issues and/or regulatory challenges with this technology?

This technology might let people manipulate with others, indirectly force them
to make decisions, or by accessing their memory get sensitive information about
them.

3. What do you think might be a cautionary tale related to this technology?

Someone innocent gets accused of crime and goes to jail.

4. What fictional person in the future could best illustrate this caution?

Witness of the crime.

5. What is their story?

Criminal tries to escape the consequences of committing a crime by altering the memory
of a witness and making them believe that they were the one who committed the
crime.

6. Now, consider what a "Light Mirror" scenario would be for this story. That is,
what benefit can come out of the  technology featured in the story and how can
we work towards preventing the negative consequences of the future they envision?

Sometimes we wish we could simply forget a certain event, so for example if a
person has a huge trauma from past, and they are suffering, altering their
memory can let them get peace.
We can prevent the negative outcomes by restricting who can access the tool.
Such as it might only be accessed by licensed counselors to treat their patient.
