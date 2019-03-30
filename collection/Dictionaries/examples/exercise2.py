#Given the dictionary below:

# artist = {
#     "first": "Neil",
#     "last": "Young",
# }

#Declare a variable called full_name  that is equal to artist's first  and last  names with a space between. You must reference the values associated with those keys in the artist dictionary.
# print(full_name)

#Concatenation Solution
#Solution using string concatenation:
artist = {
    "first": "Neil",
    "last": "Young",
}

# concat first and last name with a space
full_name = artist["first"] + " " + artist["last"]


#Format() Solution
#Solution using the format() method:

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = "{} {}".format(artist["first"], artist["last"])


#F-String Solution

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"
