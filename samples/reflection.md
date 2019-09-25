# Reflection by Please Enpu

## What are the rules to which a valid password must adhere?

A valid password must include at least every one of the following elements:
uppercase letter, lowercase letter, special symbol, and numbers. Uppercase letters
include `A B C D E F G H I J K L M N O P Q R S T U V W X Y Z`. Similarly,
lowercase letters include `a b c d e f g h i j k l m n o p q r s t u v w x y z`.
In my program, special, symbols include`! @ # $ % ^ & *`, and numbers include
all ten numbers from 0 to 9. The password must have at least six characters.

## Give five examples of invalid passwords, explaining why they are invalid.

`1 2 3 4 5` is an invalid because it only has five characters, which are all
digits. `1 2 3 4 q w s d o` is an invalid password because it does not include
uppercase letters, and special symbols. `1 2 q w e r Q W E R T` is an invalid
password because it does not include special symbols. `q w e r Q W E R ! @ # $`
is an invalid password because it does not include digits. `1 Q q ! @` is an
invalid password because it does not have at least six characters in the password.

## What was your strategy for checking whether a password was valid or not?

I start by declaring a lot of boolean instances, to check the true or false if
the password contain a required element. The program check the length of the
password first, because there is a built-in method in the array class that can
return the length of the password. If the length is lower than six characters,
then it will just return false, skipping all the other unnecessary check on
digits, special symbols, uppercase and lowercase letters. After this, it checks
every character in the password if it has those required elements. As soon as it
meets every requirements, it will return true and exit the loop.

## What did your doubling experiment reveal about the performance of your checker?

Most of the data in the ratio column are 1, and there are a few of 2 and 3 as well.
It shows that my password checker performs faster than linear function. If it grows
in linear function, the ratio should mostly be 2. However, I added a specific check
in `PasswordChecker.java` that whenever the checker finds the password has met
with all the requirements, it will just exit the loop. Thus, the ratio shown in
the output is not exactly linear since it did not go through the whole array
every time. For example, it might only went through the first 4 or 5 characters,
and exit the loop.

## Using the big-Oh, what is the likely worst-case time complexity of your checker?

The worst-case time complexity will be like O(n) since there is only one `for`
loop executed in the whole program. This could also be called as a single nest
program. The worst-case will be like when the program goes through the whole
array till the last position then it finally determines whether it is an invalid
or a valid password. And the growth rate is a linear function, which means the
time increased in the same growth rate as the input sizes.
>This function arises in algorithm analysis any time we have to do a single
basic operation for each of n elements. For example, comparing a number x to
each element of an array of size n will require n comparisons. The linear
function also represents the best running time we can hope to achieve for any
algorithm that processes each of n objects that are not already in the computer’s
memory, because reading in the n objects already requires n operations

## What challenges did you face during this assignment? How did you handle them?

This lab assignments requires more than the previous couple lab assignments. In
this lab assignment, we need to implement not only the `PasswordChecker` to
check the validity of the password, but also the algorithm to randomly generate
valid passwords and invalid passwords. We also need to implement the `Experiment`
class and the `ResultsTable` to display the right outputs, including the message
and the ratios, sizes, and timings. There are also a few bugs in the test cases
that need us to find out. It took me a little while to generate the random password,
and I learned more about `char` datatype during this assignments. I found out we
must use single quotation mark to declare a char. If we use the normal double
quotation mark, it will just automatically become a `String` variable.

```
Starting a campaign of experiments with valid passwords …
  Running round 0 with input size 250
  Running round 1 with input size 500
  Running round 2 with input size 1000
  Running round 3 with input size 2000
  Running round 4 with input size 4000
  Running round 5 with input size 8000
  Running round 6 with input size 16000
  Running round 7 with input size 32000
  Running round 8 with input size 64000
  Running round 9 with input size 128000
… Finishing a campaign of experiments with the password checker …
Results of an experiment campaign with valid passwords :
Size (#)        Timing (ms)     Ratio (#)
250             0               0
500             0               0
1000            1               0
2000            1               1
4000            1               1
8000            1               1
16000           1               1
32000           2               2
64000           2               1
128000          7               3
Starting a campaign of experiments with valid passwords …
  Running round 0 with input size 250
  Running round 1 with input size 500
  Running round 2 with input size 1000
  Running round 3 with input size 2000
  Running round 4 with input size 4000
  Running round 5 with input size 8000
  Running round 6 with input size 16000
  Running round 7 with input size 32000
  Running round 8 with input size 64000
  Running round 9 with input size 128000
… Finishing a campaign of experiments with the password checker …
Results of an experiment campaign with invalid passwords:
Size (#)        Timing (ms)     Ratio (#)
250             0               0
500             0               0
1000            1               0
2000            1               1
4000            1               1
8000            1               1
16000           1               1
32000           2               2
64000           2               1
128000          7               3

```
