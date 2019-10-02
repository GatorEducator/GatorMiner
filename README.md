# textMining
Repository to host the work for the text mining and analysis of student reflection documents in the Dept of CS at Allegheny College.


### Commands

- If needed, install and upgrade the `pipenv` command: `pip install pipenv --user`
- Install the development dependencies `pipenv` command: `pipenv install --dev`
- Run command: `pipenv run python src/util/run.py samples/sample_reflection.txt`


### Planning steps

- [ ] Make sample reflection input files for testing
- [ ] Implement frequency analysis program in Python3
  - [ ] For each reflection dociment, calculate the number of occurrences of specific keywords
  - [ ] Produce a summary of these frequencies of these words across all reflection input files
  - [ ] Generate plots of results
- [ ] Research Python3 nltk (Natural Language Toolkit) libraries


## Five Questions
- Who made the technology?
- Who are the users?
- Who is not supposed to use?
- How can the software can cause harm?
- What solutions to avoid the harm or to fix the harm?
