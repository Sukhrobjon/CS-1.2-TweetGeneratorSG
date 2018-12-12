def read_file(txt):
    with open(txt) as file:
        contents = file.read()
    contents = contents.lower()
    contents = polishing_text(contents)
    contents = contents.split()

    return contents


def polishing_text(string):
    punc = '''!()-[]{};:"\<>./?@#$%^&*_~1234567890'''
#     punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~+'''
    no_punc = ""
    for char in string:
        if char not in punc:
            no_punc += char
    return no_punc
