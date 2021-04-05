import csv
from csv import writer

"""Categorize words according to unique mentions in correspondent assignment categories"""
categories = []
new_categories = []


def input_file():
    global filename
    """retrieve file and its categories from user input"""
    filename = input("Enter path of assignment file: ")
    category_input = input("Enter categories of assignment separated by comma: ")
    # normalize input
    global categories
    categories = category_input.split(', ')
    # TODO: add column of proportional frequencies of words



def classify_file_categories():
    """add category to list of categories if necessary"""
    global new_categories
    with open("category_frequencies/categories.txt", "r") as file_categories:
        original_list = file_categories.read()
        with open("category_frequencies/categories.txt", "a") as category_list:
            for element in categories: # TODO: change to account for different capitalization
                if (element + " ") in original_list:
                    pass
                else:
                    category_list.write(element + " \n")
                    new_categories.append(element)
    # number of assignments currently existing
    f = open('category_frequencies/assignment_categories.csv','r')
    reader = csv.reader(f, delimiter=',')
    number_columns = len(next(reader)) # Read first line and count columns
    number_assignments = number_columns - 1

    category_row = []
    # add new categories as rows
    if new_categories:
        with open('category_frequencies/assignment_categories.csv', 'a') as category_file:
            file_writer = writer(category_file)
            for element in new_categories:
                category_row.clear()
                category_row.append(element)
                for i in range(number_assignments):
                    category_row.append("False")
                file_writer.writerow(category_row)
            category_file.close()
    # add new assignment as columns
    with open('category_frequencies/assignment_categories.csv','r') as category_file:
        with open('category_frequencies/output_storage.csv', 'w') as category_file_output:
            file_writer = csv.writer(category_file_output)
            file_reader = csv.reader(category_file)
            total_rows = len(list(reader))

            category_matching = False
            row_count = 0
            for row in file_reader:
                if row_count < 1:
                    file_writer.writerow(row + [filename])
                else:
                    category_matching = False
                    row_category = row[0]
                    for element in categories:
                        if element == row_category:
                            category_matching = True

                    if category_matching:
                        file_writer.writerow(row+['True'])
                    else:
                        file_writer.writerow(row+['False'])
                row_count += 1

    # update assignment categories files
    with open('category_frequencies/output_storage.csv','r') as file_input:
        with open('category_frequencies/assignment_categories.csv', 'w') as file_output:
            file_writer = csv.writer(file_output)
            file_reader = csv.reader(file_input)
            for row in file_reader:
                file_writer.writerow(row)


def sort_word_freqs(element):
    """"quantify amount of words used by assignments of each category"""
    # add new words from dataframe to csv
    # store average proportion of use in category versus in other categories

if __name__ == "__main__":
    input_file()
    classify_file_categories()
    sort_word_freqs("bioinformatics")
