#Write a function called "statistics" , which takes in a file name and returns a dictionary with the number of lines, words, and characters in the file.

'''
statistics('story.txt')
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''


def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return {"lines": len(lines),
            "words": sum(len(line.split(" ")) for line in lines),
            "characters": sum(len(line) for line in lines)}
