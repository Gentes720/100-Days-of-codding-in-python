with open(f'/home/gentes/Documents/My 100 days pycodes/32/032/letter_templates/letter_1.txt', 'r') as letter:
    lines = letter.readlines()
lines[0] = f" boom"

final = ''.join(lines)
print(final)

