import re

def read_file(txt):
    with open(txt) as file:
        contents = file.read()
    contents = polishing_text(contents)
    return contents

def polishing_text(source_text):
    '''returns only words lower case and ignore all other operations'''
    words = re.sub("[^a-zA-Z'\\-]", " ", source_text)
    return words.lower().split()
    

# def read_file(txt):
#     with open(txt) as file:
#         contents = file.read()
#     # contents = polishing_text(contents)
#     contents = punc(contents)
#     contents = contents.split()
#     return contents

# def punc(txt):
#     unwanted = '''!()-[]{};:"\<>./?@#$%^&*_~1234567890'''
#     no_punc = ""

#     for char in txt:
#         if char not in unwanted:
#             no_punc += char

#     return no_punc
