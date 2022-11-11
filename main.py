# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def mail_merge():
    letter = ""
    names = []
    with open("Input/Letters/starting_letter.txt") as letter:
        letter = letter.read()
    with open("Input/Names/invited_names.txt") as names:
        names = names.read().split()
    for name in names:
        with open(f"Output/ReadyToSend/Letter_to_{name}.txt", "w") as invite:
            letter = letter.replace("[name]", name)
            invite.write(letter)


mail_merge()
