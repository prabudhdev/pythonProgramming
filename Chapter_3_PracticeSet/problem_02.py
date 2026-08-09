letter = """Dear {name},
You are selected for the position of {position} in our company."""
print(letter.format(name=input("Enter your name : ").capitalize().title(), position=input("Enter your position : ").upper()))