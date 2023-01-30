words = ["abigael", "monicah", "susan", "annabelle", "annaise", "zoey"]

### dont forget the else part, when using if then else
## also make sure your if statement is correct
new_list_of_words = [word.upper() if word.startswith("a") else word for word in words]

print(new_list_of_words)