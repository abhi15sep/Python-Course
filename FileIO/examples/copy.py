#Write a function called "copy", which takes in a file name and a new file name and copies the contents of the first file to the second file.


'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

#Copy should copy contents from one file to another.  For example, after running:

#copy('story.txt', 'story_copy.txt') # None
#We would expect the contents of story.txt and story_copy.txt to now be the same.

def copy(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text)


