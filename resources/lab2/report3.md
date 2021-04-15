# Assignment

assignment-02

# Reflection by

user 3

## Data

I used two different script data. One is scripts of Green Arrow Season Three, episode 1 to 23, and another one is scripts of Black Mirror Season One to Four, all episodes. Since there are some special symbols in these scripts, I have to use both `utf-8` and `ISO-8859-1` to encode. I manually assigned all Black Mirror scripts to have creativity score of 1 and all Green Arrow scripts to have creativity score of 0. This two selections have similar amount of word count, therefore, the data distribution should not be a big problem. I used these two datasets together with `textgen` package to generate a script text using RNN, then use these two datasets associated with the creativity score to train a KCNN model which can predict the creativity score of generated script text.

## Text Generation

Reference: https://github.com/minimaxir/textgenrnn
For text generation, I first read in scripts from both Black Mirror and Green Arrow through `utf-8` and `ISO-8859-1` encoding. I then stored combined these two datasets are stored all scripts in `src/GenScript.txt`. The next step I have done is to use `textgen` package's `textgenrnn().train_from_file("src/GenScript.txt")` to train a RNN model where the weights are stored in the `textgenrnn_weights.hdf5` file. I then used the trained weight file as input to text generation function. The sample output for a generation as follows:

Without trained weight:

```
The Internet Bros Thousands Speed As Secret Facebook Transform (Internations)
```

With trained weight:

```
 dou gthe tha theni s.be o ttshe  eatoh elah  oteic ts<inc>ttpoihhtrt  nhteoeht  u.heRa epal.e . ?e riI
```

## Text Analysis

Reference: https://towardsdatascience.com/identifying-hate-speech-with-bert-and-cnn-b7aa2cddd60d
For text analysis, I used BERT's pretrained data to apply NLP as a pre-training transformer. I first randomized the input data and chose first 25000 of random data as training dataset, 25000 to 26000 as validation set, and 26000 to 30414 as testing set. After using BERT tokenized and fitted the pretrained model, I started training KCNN with creativity score where all Black Mirror scripts have the creativity score of 1 and all Green Arrow script have the creativity score of 0. After the training KCNN, I applied cross validation with the the cv dataset. Since there is only one label, creativity score, the plot of training loss based on Epoch is meaningless. After the cross validation, I checked the accuracy rate with the testing set.

Sample one:

```
Epoch 10 Train loss: 0.53. Validation loss: 0.54. Elapsed time: 13.18s.
cross validation of the given dataset:
   label  auc
0  Score  0.786407
```

Sample two:

```
Epoch 10 Train loss: 0.53. Validation loss: 0.54. Elapsed time: 13.17s.
cross validation of the given dataset:
  label       auc
0  Score  0.786287  
```

## Supplemental Production

By applying the KCNN model we trained during text analysis to the generated script text, we can get the creativity score of the generated text. The score is between 0 and 1.

Sample one:

```
generated script is
The Internet Bros Thousands Speed As Secret Facebook Transform (Internations)
and has creativity score of:
0.4311581254005432
```

Sample two:

```
generated script is
- [AlLAUK] [hhmHOS]e-e  t hemie Aie Ya nge   toooorni,en' onr str tolot uyt Aotndgo .   ahwo,oonni to heFn r.ne ndoo  et'ttofa  yoo tou fou  rifhron rteht f ierroturan m rol enyi apeerrtso,en en nWt.dgeeaorond. t! htdthhteeaiei  eaas rhtoeigrse eaa?s to tthy tarhthoh ,tioy  aono sou  tih ro ir ndet
and has creativity score of:
0.9953184723854065   
```

## Challenges and Learning Experiences

I first faced difficulties with gathering data. The scripts I got are not in text, therefore we have to read in and encoding. However, some special characters can not be easily recognized by `srt.parse()`. I did some research and found out that I can fully avoid these errors by using both `utf-8` and `ISO-8859-1` to encode.

I also had some troubles associated with memory allocation since I have a very large input dataset. I have received the following runtime error when I am trying to fit BERT pretrained model to my dataset:

```
RuntimeError: [enforce fail at ..\c10\core\CPUAllocator.cpp:72] data. DefaultCPUAllocator: not enough memory: you tried to allocate 12000000000 bytes. Buy new RAM!
```

I then changed the default of PyTorch from using CPU to GPU, but I am still receiving runtime error:

```
RuntimeError: CUDA out of memory. Tried to allocate 7.15 GiB (GPU 0; 11.00 GiB total capacity; 7.65 GiB already allocated; 1.14 GiB free; 64.07 MiB cached)
```

I was able to solve this issue by changing `max_seq` from 100 to 5, which is the batch size for applying BERT model.

## Ethical Benefits and Implications

This program is a naïve version of recognizing creativity within the text. The ethical benefits are obvious, that quantitative creativity can help people easier monetize it, and thereby consider it more important than before.

Synopsis:

```
Creativity
```

1. What future technology is featured in your synopsis?

The idea can be used in a tool to compare and rate creative shows based on their scripts.

2. What are the potential social implications and/or ethical issues and/or regulatory challenges with this technology?

People would be more easier identifying creative show to watch, this can be imbedded by show recommendation system, but since it hurts some shows' benefits, there may be some suggestion against it. Additionally, as we are using deep learning, we don't have 100% of confident that the creativity measurement is correct.

3. What do you think might be a cautionary tale related to this technology?

When the technology gives wrong prediction about creativity since it is based on the data and may be biased. For example, in this lab, Black Mirror is the positive data and Green Arrow is the negative data. This may lead to a model which always recognize super hero shows are bad and unit shows are good in terns of creativity.

4. What fictional person in the future could best illustrate this caution?

A person who believes Immanuel Kant that humanity is a means and an end would argue relying on quantitative data is meaningless.

5. What is their story?

Argued against the happenings in the society but failed to make any impact due to the trend in the society is too strong no matter if it is the right direction of moving forward.

6. Now, consider what a Light Mirror scenario would be for this story. That is, what benefit can come out of the  technology featured in the story and how can we work towards preventing the negative consequences of the future they envision?

Regulation can prevent the worst case happening. As long as the human society still allows different voices from high intelligent and moral people, such tool can only be used on its benefits.
