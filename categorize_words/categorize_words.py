"""Categorize words according to unique mentions in correspondent assignment categories"""

categories = []


def input_file():

    """retrieve file and its categories from user input"""
    filename = input("Enter path of assignment file: ")
    category_input = input("Enter categories of assignment separated by comma and space: ")

    # normalize input
    global categories
    categories = category_input.split(', ')


def classify_file_categories():

    """add category to list of categories if necessary"""

    with open("category_frequencies/categories.txt", "r") as file_categories:
        original_list = file_categories.read()
        with open("category_frequencies/categories.txt", "a") as category_list:
            for element in categories:
                if (element + " ") in original_list:
                    pass
                else:
                    category_list.write(element + " \n")


if __name__ == "__main__":
    input_file()
    classify_file_categories()
