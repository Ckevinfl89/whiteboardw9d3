# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "   =>  "#HelloWorld"
# ""   =>  false

def solution(s):
    # Remove leading and trailing whitespaces and split the string into words
    words = s.strip().split()
    
    # If the input string is empty or there are no words, return False
    if not words:
        return False
    
    # Capitalize the first letter of each word and join them together
    hashtag = ''.join(word.capitalize() for word in words)
    
    # Prepend a '#' to the hashtag
    hashtag = '#' + hashtag
    
    # If the length of the hashtag is greater than 140, return False
    if len(hashtag) > 140:
        return False
    
    return hashtag

def solution(input):
    if(input == ""):
        return False
    
    output = '#'

    words = input.split(' ')
    for w in words:
        output += w.strip(' ').title()

    if(len(output) > 140):
        return False
    else:
        return output
    
    def solution(string):
    new_string = '#'
    split_string = string.split(" ")

    if not string or len(string) > 140:
        return False
    
    for k, v in enumerate(split_string):
        new_string += v.title()

    return new_string