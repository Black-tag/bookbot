def get_num_of_words(book_text):
    """ counts the number of words in the book text"""  
    words = book_text.split()
    words_list = list(words)
    # print(words_list)
    return len(words)
    


def get_occurances(text):
    """ count the occurance of every character in the book data """
    occurances = {}
    for char in text:
        if char in occurances:
            occurances[char] += 1
        else:
            occurances[char] = 1 
    return occurances      


def sort_occurances(dictionary):    
    return sorted(dictionary.items(),key=lambda x:x[1], reverse=True)   