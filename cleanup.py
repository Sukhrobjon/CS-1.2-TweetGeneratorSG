import re
def read_file(txt):
    with open(txt) as file:
        contents = file.read()
    contents = polishing_text(contents)

    return contents


# def polishing_text(string):
#     punc = '''!()-[]{};:"\<>./?@#$%^&*_~1234567890'''
# #     punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~+'''
#     no_punc = ""
#     for char in string:
#         if char not in punc:
#             no_punc += char
#     return no_punc


def polishing_text(source_text):
    '''returns only words lower case and ignore all other operations'''
    words = re.sub("[^a-zA-Z'\-]", " ", source_text)
    return words.lower().split()
