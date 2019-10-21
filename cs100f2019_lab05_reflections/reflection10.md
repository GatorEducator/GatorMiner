# Reflection by 

## Using a fenced code block, please display the output from running your program

```
> Configure project :
Configured GatorGradle 0.4.4

> Task :compileJava UP-TO-DATE
> Task :processResources NO-SOURCE
> Task :classes UP-TO-DATE
> Task :jar UP-TO-DATE
> Task :startScripts UP-TO-DATE
> Task :distTar UP-TO-DATE
> Task :distZip UP-TO-DATE
> Task :assemble UP-TO-DATE
> Task :checkstyleMain UP-TO-DATE
> Task :compileTestJava NO-SOURCE
> Task :processTestResources NO-SOURCE
> Task :testClasses UP-TO-DATE
> Task :checkstyleTest NO-SOURCE
> Task :test NO-SOURCE
> Task :check UP-TO-DATE
> Task :build UP-TO-DATE

BUILD SUCCESSFUL in 1s
6 actionable tasks: 6 up-to-date
```

## For each String and Random method used, add an explanation in the list format (as shown in an example below).

- `.substring` Returns a substring with given position or index
- `Random rand` Create a new set of values within the randomizing
- `length` Returns the length of the string


## What was the greatest technical challenge that your team faced and how did you overcome it?
The greatest technical challenge I faced on this assignment was with checkstyle errors that prevented the gradle run of the program. While the build was successful, the checkstyle errors continued to plague me throughout the process. I suffered on this one more than in past labs primarily because the subject is entirely new to me, that of DNA modification and replacement/replication, and I was extra focused on the new commands and practicing the stringing methods, that I was more careless with my checkstyle mistakes. I am still struggling with one major issue, which is a compiler error in my 39th line involving the "." in "scanner.nextline", and despite my best efforts, extensive googling, and asking for TA advice, this error code will not disappear, and the code will not build completely. It is terrible. I still have not fully overcome it, and am attempting to find any workaround or solution to make the program buildable without losing completed portions of the assignment that fulfill the gradle grade assignment checks. This is the hardest and most frustrating challenge I have faced all year.

## Based on your experiences with simple DNA manipulation in this lab and reflecting on the assigned article, answer the following questions:

1. Who makes the genome editing technology?
CRISPR technically has the most advanced and currently existing genome editing technology, however the science and debate have been around for a long time and have involved numerous other companies and ethicists. In a more general sense, the older generations or "we" make the genome editing technology, as living humans, and hypothetically use it on embryos and undeveloped lives to see how genome modification works. The technology itself is made by CRISPR and other biotechnology companies, and is ready to be used, and has been used, to edit genomes of multiple species and kinds.

2. Who are the users of the genome editing technology?
The users of the technology itself, besides the scientists who would conduct the actual editing and genome procedures, are the family members and parents of those who would be edited. This leads to a GIANT grey area regarding informed consent and whether it is actually plausible to achieve, as the people who the genome editing technology is BEING USED ON or AFFECTING are the children who are not born or capable of autonomy yet, and therefore the decision is left with the parents, and they become the "users" by deciding to engage in the practice. As of current day, the only users of the technology are scientists on animals and non-viable embryos (children who will not be brought to full term or are incapable of birth), and it is limited to that thus far. "We" are the "users" f the technology, but those who have had the technology used on them, or are "influenced" by the technology, are in fact our children and future generations. They are the ones who could technically utilize or "use" the genome editing technology in its application.

3. Who is not supposed to use the genome editing technology?
The genome editing technology is not supposed to be used by those wanting to improve or enhance their own offspring, or in any way give them an advantage either physically or mentally, and is not to be used for anything other than medical necessity to prevent otherwise debilitating disease. The primary concern surrounding genome editing therapy at this time is the potential for it to be used in the wrong ways by the wrong people. A major concern is that it will widen the wealth gap and further divide the social classes by those who are able to afford gene editing and those who are not, and later on between those who are genetically superior to others DUE to their enhancements. Another concern about the gene editing being used in a negative way is to cherry pick certain qualities and attributes to improve or remove and in some way "better" the candidate. Finally, the technology should not be used by any government or individual for any purposes other than IRB approved research on non autonomous non-viable embryos.

4. How can the genome editing technology cause harm?
It can widen the gap between the wealthy and those who are more middle or low income by deciding who has access to this particular aspect of superiority. By creating our own step into evolution and trying to force the improvement of certain genes and traits for the sake of improving health, we create a level of evolution that is held in superiority, but is not accessible to all. Similarly, the thought of those who are edited being seen as superior or in some way trying to enforce this over masses who are not able to afford or access genome editing is a significant risk. The threat this poses to creating a dystopian society both domestically and internationally is on the forefront of these concerns and arguments.

5. What solutions can be developed to avoid the harm caused by the genome editing technology or to fix the harm?
Rules and regulations can be put in place to prevent unnecessary or wanton uses genome editing among the greedy or rich or downright criminally neglectful. Similarly, a "need based" approach achieves the ultimate goal of gene editing, which is to prevent unnecessary disease and genetic mutation from affecting the next generation when preventable, while still keeping the technology out of the hands of the Trump's and Putin's in the world, who would likely use this technology yo further their own means and desires. Overall, a very strict and militant approach to access and administration of genome editing is the only way to hope to prevent reckless use of such a powerful new science.


## After completing this assignment, what is task that your team wants to practice more? Why?
After this, I would like to practice the random class more, as it is the newest and still most confusing to me, as well as review the basics of string and substring methods within java coding. Other than that, I just need to calm down and make sure I review all my keystrokes and symbols to identify where I may be violating checkstyle rules.

## After completing this assignment, what is one learning experience you have valued the most?
I valued learning how to program randomization and replacement methods, but also the ethics and debate surrounding gene editing as a whole. I feel much more capable of weighing in on genome editing in social and political conversations, and have a deeper appreciation for what the software we develop is truly capable of when applies in the right context.


Final Gradle Run:

bash-5.0# gradle grade

> Configure project :
Configured GatorGradle 0.4.4

> Task :grade
Updating GatorGrader...
Fetching origin
Checking out to 'master'
Managing GatorGrader's Python dependencies...
Finished!



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
✘  The command 'gradle -q --console plain run' executes correctly
✔  The reflection.md in writing has exactly 0 of the 'Add Your Name Here' fragment
✔  The ManipulateDna.java in src/main/java/labfive has exactly 1 of the 'import java.util.Date' fragment
✔  The ManipulateDna.java in src/main/java/labfive has at least 2 multiple-line Java comment(s)
✔  The ManipulateDna.java in src/main/java/labfive has exactly 1 of the 'new Date()' fragment
✔  The reflection.md in writing has exactly 3 of the 'code' tag
✔  The reflection.md in writing has exactly 7 of the 'heading' tag
✔  The reflection.md in writing has exactly 1 of the 'code_block' tag
✔  The ManipulateDna.java in src/main/java/labfive has at least 8 of the 'System.out.println' fragment
✔  The repository has at least 8 commit(s)
✔  The file reflection.md exists in the writing directory
✔  The command 'gradle build' executes correctly
✔  The ManipulateDna.java in src/main/java/labfive has at least 1 of the '.toUpperCase' fragment
✔  The ManipulateDna.java in src/main/java/labfive has exactly 0 of the 'TODO' fragment


-~-  FAILURES  -~-

✘  The command 'gradle -q --console plain run' executes correctly
   ➔  The command returned the error code 1


	┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
	┃ Passed 23/24 (96%) of checks for cs100-01-lab05-solution! ┃
	┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
