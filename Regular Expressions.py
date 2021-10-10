import re

# Look for string in a string
#output = re.findall('excited','i am so excited')

# Split a string when finding a specific character
#output = re.split ("!", "Split this sentence ! when you find the sign and store it in a list")

# Replace one or many values
#output = re.sub ('red','blue','I have a red car')

# \d for Digits
#output = re.findall("user\d","the winners are user1, user2, user3, userb")

# \D for NonDigits
# output = re.findall("user\D","the winners are user1, user2, user3, userb")

# \w for Word (Digits + NonDigits)
# output = re.findall("user\w","the winners are user1, user2, user3, userb")

# \W for Word (Non-Word)
# output = re.findall("user\W","the winners are user1, user2, user3, userb, user$")

# \s for White Space
# output = re.findall("Data Science","This is Data Science")

# \S for Non-Whitespace
# output = re.sub("ice\Scream","ice cream","I like ice-cream")

# zero times or 1
# output = re.findall("colou?r","This is my color. Loce this colour")

# zero times or more
# output = re.findall("@\w+\W","@John$")

#output = re.findall("\+\d{3}-\d{5}\s\d{4}", "+353-98765 4321")


# Find all email addresses
data = "ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef, ejhefjhefjhfe, johnsmith12@gmail.com, ejfefhjfehjef"
output = re.findall("\w+@\w+\Wcom", data)

print (output)
