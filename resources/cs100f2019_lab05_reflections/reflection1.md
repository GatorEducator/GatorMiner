# Reflection by 

## Using a fenced code block, please display the output from running your program
```
Sun Oct 06 00:18:07 EDT 2019

Manipulate the DNA string: 'ATCG '

Complement of ATCG is TAGC
Inserting G at position 3 gives ATCGG
Deleting from position 3 gives ATC
Changing position 3 gives ATCA
Thank you for using the Manipulation program.
 
```

## For each String and Random method used, add an explanation in the list format (as shown in an example below).

- `nextInt`: assign an integer value to the next user defined term
- `charAt`: returns the character at the specified index
- `replace`: replace the original letter(s) with another 


## What was the greatest technical challenge that your team faced and how did you overcome it?
Coming up with the strategy that avoid the problem generating when converting A to T, T to A or C to G, G to C.
If the converting command order is wrong, then the actual DNA sequence will be in a disorder. Then my soulution is 
make the origianl DNA sequence order into lower case and then during the converting process, directly convcrt the 
lower case to upper case, so all the four convering command line will not interference each other. It is a little
bit frustrating when the checkstyle thing does not allow the name of sting or data in the format of dna_origianl 
while the input file is written as dna_input. I thought naming in this way will make it much clearer about the 
actual meaning of different variables.and which number represents which position also confuesd me for a while.

## Based on your experiences with simple DNA manipulation in this lab and reflecting on the assigned article, answer the following questions:

1. Who makes the genome editing technology?
   Biological scientists
2. Who are the users of the genome editing technology?
   Biological scientist or doctor
3. Who is not supposed to use the genome editing technology?
   anyone who is not professional in this field
4. How can the genome editing technology cause harm?
   break the balance of the natural gene esquence
5. What solutions can be developed to avoid the harm caused by the genome editing technology or to fix the harm?
   setting up facilities to watch out all these experiments or citi training

## After completing this assignment, what is task that your team wants to practice more? Why?
random package, there are so many fun things could be done with this. and most of reecent are focusing on the game
of string literature, such as changing a letter at some place. It is fun at first but not so with time goes on. 
I am looking forward to some poroblem even involing some challenging math to be more interesting.

## After completing this assignment, what is one learning experience you have valued the most?
when doing the converting staff, learning that the comuptational strategy is a big part of the programming
editting. some simple logical difference will result in a huge difference in the output. so it is always 
worthy to think all the things through before starting writing the program.And still, I do not know using 
docker run or gradle run at the upper directory is the most convenient way to compile or run. since I am
using vim editor, I feel using javac and java command to compile and run at the code directory is the best 
way for me. 
