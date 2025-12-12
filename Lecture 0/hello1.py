# ask user for their name
name = input("What's your name? ").strip().title()

#split user's name into first and last name
first, last = name.split(" ")

#remove whitespace froms str and capitalize
name = name.strip().capitalize()

# capitalize user's name
name = name.capitalize()
name = name.title() 

# say hello to user
print(f"hello, {name}")
print(f"hello, {first}")
