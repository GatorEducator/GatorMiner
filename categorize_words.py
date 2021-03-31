categories = []

def input_file():
    # prompt user for file and its categories
    filename = input("Enter path of assignment file: ")
    category_input = input("Enter categories of assignment separated by comma and space: ")

    # normalize input
    global categories
    categories = category_input.split(', ')

def classify_file_categories():
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
