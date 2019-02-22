import re

def read_file(txt):
    """Read the file and returns the list of the words from text source"""
    with open(txt) as file:
        contents = file.read()

    contents = polishing_text(contents)
    return contents

def polishing_text(source_text):
    '''returns only words and ignore all other operations'''
    words = re.sub("[^a-zA-Z'\\-]", " ", source_text)
    return words.split()
    


