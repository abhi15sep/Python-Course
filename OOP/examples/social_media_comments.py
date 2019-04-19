#It's time to define your own class! Suppose we're creating a social network application where users can comment on posts and photos.
#Create a class called Comment .  Each comment should have the following attributes:
#1. username  - the username of the person who created the comment (like "bluethecat")
#2. text      - the actual comment itself (like "omg so cute!" or "hahah")
#3. likes  - the number of likes the comment has.  Likes should default to 0
#The following code should work:
#


class Comment():
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes
