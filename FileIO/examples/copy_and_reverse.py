#Write a function called "copy_and_reverse", which takes in a file name and a new file name and copies the reversed contents of the first file to the second file.

'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''


def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])