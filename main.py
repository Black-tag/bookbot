import sys


from stats import get_num_of_words
from stats import get_occurances
from stats import sort_occurances

if len(sys.argv) < 2:
    print(f"Usage: python3 main.py <path_to_book>", end="")
    sys.exit(1)
filepath = sys.argv[1]    

def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    with open(filepath) as file:
        return file.read()


      


def main():

    """main function to print the contents of frankenstein.txt"""

    
    print("===============ANAND'S BOOKBOT===============")
    print(f"Analysing the book found at {filepath}")


    book_text = get_book_text(filepath)
    num_words = get_num_of_words(book_text)
    char_occurances = get_occurances(book_text.lower())
    sorted_list = list(sort_occurances(char_occurances))

    print("---------------WORDCOUNT---------------")
    print(f"Found {num_words} total words")


    print("---------------CHARACTER COUNT---------------")
    for char,count in sorted_list:
        if char == " ":
            continue
        print(f"{char}: {count}")

    print("===============END===============")        
   
    

    

if __name__ == "__main__":
    main()            