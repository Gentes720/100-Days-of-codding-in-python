# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# # student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# # for (index, row) in student_data_frame.iterrows():
# #     #Access index and row
# #     #Access row.student or row.score
# #     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.


# import csv

# with open('/home/gentes/Documents/My 100 days pycodes/26final/nato_phonetic_alphabet.csv') as file:
#     reader = csv.DictReader(file)
#     data = {row['letter']: row['code'] for row in reader}

# name = input("Enter a word: ").upper()
# output_list = [data[letter] for letter in name if letter in data]
# print(output_list)

import pandas
data = pandas.read_csv('/home/gentes/Documents/My 100 days pycodes/26final/nato_phonetic_alphabet.csv')
nato_alpha = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter your name :").upper()
output_list = [nato_alpha[letter] for letter in name]
print(output_list)

