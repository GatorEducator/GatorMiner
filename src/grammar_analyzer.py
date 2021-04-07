import language_check

# Mention the language keyword
def grammar_analyzer(data: str) -> str:
    '''A tool to check grammar error in reflection'''
    tool = language_check.LanguageTool('en-US')
    i = 0

    # Path of file which needs to be checked will be parse to data in main method
    with data as file:
        for line in file:
            matches = tool.check(line)
            i = i + len(matches)
            pass

    # prints total mistakes which are found
    # from the document
    print("No. of mistakes found in document is ", i)
    print()

    # prints mistake one by one
    for mistake in matches:
        print(mistake)
        print()
