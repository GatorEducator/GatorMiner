# Reflection by 

## Using a fenced code block, please display the output from running your program

```

  String dna = scanner.nextLine();
  System.out.println(dna.toUpperCase());


  // : Compute the complement of the DNA String
  String dna2 = "";
  dna2 = dna.replace("A", "t");
  System.out.println(dna2);
  dna2 = dna.replace("T", "a");
  System.out.println(dna2);
  dna2 = dna.replace("G", "c");
  System.out.println(dna2);
  dna2 = dna.replace("C", "g");
  System.out.println(dna2);

  // : Insert a randomly chosen DNA letter into the DNA String at a random position
  Random rand = new Random();
  int num1 = rand.nextInt(dna2.length());


  // : Delete a DNA letter from a randomly chosen position in the DNA string
  dna2 = dna2.replace(dna2.substring(num1, num1 + 1), "");
  dna2 = dna2.replace(dna2.substring(num1, num1 + 1), "");
  int pos = rand.nextInt(dna2.length());
  // : Change a random position in the DNA String to a randomly chosen DNA letter
  dna2 = dna2.replace(dna2.charAt(pos), "ACGT".charAt(rand.nextInt(4)));
  // : Display a final thank you message
  System.out.println("Thanks for using DNA Program");

```

## For each String and Random method used, add an explanation in the list format (as shown in an example below).
for the first string i used dna2 i was telling the program that i was using the DNA as a variable.

the random method i used was tell the program that rand was my variable for random
the random used was to get a random letter chosen in the DNA string.
- `nextInt`: consetetur sadipscing elitr
- `String dna2 = ""` i Used this to show that the dna2 variable needs to replace the letters in the dna String
- `random rand` i used random because i needed to pick a random positions in the dna string to insert a new dna letter


## What was the greatest technical challenge that your team faced and how did you overcome it?
The greatest technical challenge that i faced was probably figuring out how to get a random position in the DNA string to a random letter it took me a while to under stand how to do it. one I used the charAt I and used rand I got it to work. this challenge took me a lot of time to figure out and with a little bit of help from one of the technical leaders i was able to figure it out.


## Based on your experiences with simple DNA manipulation in this lab and reflecting on the assigned article, answer the following questions:

1. Who makes the genome editing technology?
Watson Health Solutions is a big maker of genome editing technology.

2. Who are the users of the genome editing technology?
the users of genome editing technology are doctors and scientist trying to cure diseases.

3. Who is not supposed to use the genome editing technology?
people that are not properly trained in working with genome editing

4. How can the genome editing technology cause harm?
the use of genome editing can cause you to lose year off of your life. you are also more likely to get cancer, it can be used in biological attacks, and unintended consequences for future generations.

5. What solutions can be developed to avoid the harm caused by the genome editing technology or to fix the harm?
solutions to avoid the harms caused by genome editing could be to not even get involved in genome editing in the first place.


## After completing this assignment, what is task that your team wants to practice more? Why?
the task that i would like to practice more is replace, substring and charAt. i have a lot of trouble with substring and the hardest part for me is memorizing the codes i forget what to use and mix up the codes. the more we use the codes and do more programs i think i will start to remember them but as of know that is the hardest part for me.



## After completing this assignment, what is one learning experience you have valued the most?
the learning experience that i value the most is probably the TODO of compute the  complement of the DNA String i valued this because i did it by myself and i think it shows that i am starting to learn and remember how to do some parts of the coding we use. i also think that it gives me confidence that i will be able to use all the codes we use and memorize and use them correctly. each Lab and practicals we do i think i get closer and closer to using  all of our codes correctly.




✔  The reflection.md in writing has at least 300 word(s) in total
✔  The ManipulateDna.java in src/main/java/labfive has at least 8 single-line Java comment(s)
✔  The reflection.md in writing has exactly 2 of the 'list' tag
✔  The ManipulateDna.java in src/main/java/labfive has at least 5 of the 'String' fragment
✔  The file ManipulateDna.java exists in the src/main/java/labfive directory
✔  The ManipulateDna.java in src/main/java/labfive has exactly 0 of the 'Add Your Name Here' fragment
✔  The ManipulateDna.java in src/main/java/labfive has at least 3 of the '.nextInt' fragment
✔  The ManipulateDna.java in src/main/java/labfive has at least 2 of the '.substring' fragment
✔  The ManipulateDna.java in src/main/java/labfive has at least 2 of the '.charAt' fragment
✔  The ManipulateDna.java in src/main/java/labfive has at least 4 of the '.replace' fragment
✔  The command 'gradle -q --console plain run' executes correctly
✔  The reflection.md in writing has exactly 0 of the 'Add Your Name Here' fragment
✔  The ManipulateDna.java in src/main/java/labfive has exactly 1 of the 'import java.util.Date' fragment
✔  The ManipulateDna.java in src/main/java/labfive has at least 2 multiple-line Java comment(s)
✔  The ManipulateDna.java in src/main/java/labfive has exactly 1 of the 'new Date()' fragment
✔  The reflection.md in writing has exactly 3 of the 'code' tag
✔  The command 'gradle build' executes correctly
✔  The reflection.md in writing has exactly 7 of the 'heading' tag
✔  The reflection.md in writing has exactly 1 of the 'code_block' tag
✔  The ManipulateDna.java in src/main/java/labfive has at least 8 of the 'System.out.println' fragment
✔  Repository has at least 8 commit(s)
✔  The file reflection.md exists in the writing directory
✔  The ManipulateDna.java in src/main/java/labfive has at least 1 of the '.toUpperCase' fragment
✔  The ManipulateDna.java in src/main/java/labfive has exactly 0 of the 'TODO' fragment


	┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
	┃ Passed 24/24 (100%) of checks for cs100-01-lab05-solution! ┃
	┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


BUILD SUCCESSFUL in 1m 17s
1 actionable task: 1 executed
bash-5.0#
