#TODO: Create a letter using starting_letter.docx 
with open('/home/gentes/Documents/100 days of coding/24. Day 24 - Intermediate - Files, Directories and Paths/7.3 mail-merge-project-start/Input/Letters/starting_letter.docx') as file:
    letter_contents = file.read()
new_contents = letter_contents.replace("[name]", "Gentes")

with open('/home/gentes/Documents/100 days of coding/24. Day 24 - Intermediate - Files, Directories and Paths/7.3 mail-merge-project-start/Input/Names/invited_names.txt') as file:
    names = file.readlines()

for name in names:
    stripped_name = name.strip()
    new_contents = letter_contents.replace("[name]", stripped_name)

    with open(f'/home/gentes/Documents/100 days of coding/24. Day 24 - Intermediate - Files, Directories and Paths/7.3 mail-merge-project-start/Output/ReadyToSend/letter_for_{stripped_name}.docx', mode="w") as file:
        file.write(new_contents)
        
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp