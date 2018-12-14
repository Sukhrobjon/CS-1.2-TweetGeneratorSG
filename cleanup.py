import re

def read_file(txt):
    with open(txt) as file:
        contents = file.read()

    contents = polishing_text(contents)
    return contents

def polishing_text(source_text):
    '''returns only words lower case and ignore all other operations'''
    words = re.sub("[^a-zA-Z'\\-]", " ", source_text)
    return words.split()
    


