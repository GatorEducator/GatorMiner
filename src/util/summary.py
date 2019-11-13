from gensim.summarization import summarize, keywords
from pprint import pprint

text = ("The greatest technical challenge I faced on this assignment was "
    "with checkstyle errors that prevented the gradle run of the program. "
    "While the build was successful, the checkstyle errors continued to "
    "plague me throughout the process. I suffered on this one more than "
    "in past labs primarily because the subject is entirely new to me, "
    "that of DNA modification and replacement/replication, and I was extra "
    "focused on the new commands and practicing the stringing methods, that "
    "I was more careless with my checkstyle mistakes. I am still struggling "
    "with one major issue, which is a compiler error in my 39th line involving "
    "the \".\" in \"scanner.nextline\", and despite my best efforts, extensive "
    "googling, and asking for TA advice, this error code will not disappear, "
    "and the code will not build completely. It is terrible. I still have not "
    "fully overcome it, and am attempting to find any workaround or solution "
    "to make the program buildable without losing completed portions of the "
    "assignment that fulfill the gradle grade assignment checks. This is the "
    "hardest and most frustrating challenge I have faced all year. "
)

# Summarize the paragraph
pprint(summarize(text, word_count=20))

print(keywords(text))
