# Reflection by

user 7

## Data
The data used in this project are subtitles from Season 2 episode 6 from Rick and Morty. This show is about a grandfather and his grandson who travel the universe carrying out weird adventures. In the episode that I picked the main characters take a look at a battery they made so they would never run out of power. Coincidentally the battery runs out of power so the characters have to figure out what is going on with the battery.

## Text Generation
To generate text I first had to get the text from the saved file and read it into a string. After this every character in the file was sorted and given a number. After this the model then learned the sequences of the numbers and tried to predict the next words. Now all of the training has been completed I ran my model for 300 EPOCHS. While this may seem like a lot each EPOCH only look seconds to run and the more times through the data the better. Finally the predicted text appeared once the model is done. I modeled my program after the step by step instructions found on https://www.tensorflow.org/tutorials/text/text_generation

```
Recthing you do matters! Your existence is a lie! If that were really true, then... I'm here to see Ron Morty. Conf re dobse my brank. Aad hie! Thanks to the skans just sounds like slavery with extra steps. Ooh-la-la, someone's gonna get laid in college. Rick, a word? What the hell was that? I know. It's a prehistoric planet, Morty. Now let's get out of here a meniverse is the biggest dick that's never existed. Why do you think, the general vibe and stuff.That's you. That's how you talk. Hey, that's my deer! Aaaaaaah! Raah! I de'ple wordd "Eek barba dirkle"? To rist my balls absote of slaves. Told you, Zeep. Oh, they won't be slaves. They'll work for each other and pay each obliged". Oh. Right. Uh, b-blow me. No, no, no. Blow me Zeep, you have an honored guest from beyond untolves taking mo real alo sef ep. There'r justod of that became the carbon in your mother's ovaries aw har You need to tell these people they're in a battery, Rick. It's messed up. There's caterers down ther kiss abo
```

## Text Analysis
To get the Text Analysis I first read the text file into a string and then clean the text, removing any unwanted characters like stop characters. Then using the nltk API I assigned values to each word and counted the frequency. After getting the frequency of all of the words I plotted the top 35 words to show how many times they occurred.

## Challenges and Learning Experiences
One challenge I had was trying to run tensorflow on a gpu. I have a desktop computer with a dedicated graphics card so I tried to set up tensorflow to run on it. Unfortunately from what I saw online tensorflow can only be run on a Nvidia GPUs while I have an AMD GPU. Another issue I had was with a variable name and trying to track it through the program. This was causing me to get weird error messages but once I found out that I had one instance of the variable spelled with a typo and changed it. One final challenge I had was getting the model to accurately predict text. To try and combat this problem I bumped up the EPOCHS and this seemed to help a little bit. Finally the biggest issue was getting an accurate summary of the show, I worked on this for a while but could not quite get the model to give a super accurate summary.

## Ethical Benefits and Implications
Some of the themes related to this technology would be a never-ending powersource, irony, and improper working conditions.

Then, hypothesizing on the issues highlighted in your generated (or modified) text, answer the following questions.

1. What future technology is featured in your synopsis?
-A battery that never runs out of charge because another universe is inside the battery and the society that exists generates power for the battery, so in theory the battery should never run out. This could fix the world's energy problem and make the world carbon neutral

2. What are the potential social implications and/or ethical issues and/or regulatory challenges with this technology?
-The big issue with this technology is that the society in the battery has no idea that they are just being used for their manpower. The characters in the episode actually touch on this idea and Morty actually calls it slavery.

3. What do you think might be a cautionary tale related to this technology?
-In the episode the civilization in the battery figures out the same way to generate power, and the civilization they create does the same thing. This cycle could keep happening and none of these societies have any idea they are just basically working for free for the civilization that created them.

4. What fictional person in the future could best illustrate this caution?
-This issue is touched of twice in the episode, once by one of the main characters, Morty and then by Rick once they go to the second created universe.

5. What is their story?
-When the main characters battery dies they must go into the battery to find out why. Morty is naive to how the battery works and once Rick tells him he calls it "slavery with extra steps". Once in the made up universe Rick and Morty see the scientist who had the same idea as Rick and they then go it that universe where Rick then says the same thing to the scientist that Morty said to him. Rick of course just wants the battery to function and with the new created universe they do not get any energy so he wants them to get rid of the universe.

6. Now, consider what a ``Light Mirror`` scenario would be for this story. That is, what benefit can come out of the  technology featured in the story and how can we work towards preventing the negative consequences of the future they envision?"
-The only way that I can really see preventing the negative consequences of this technology is by making sure the people in the created universe know their purpose and that get some sort of compensation for the work.
