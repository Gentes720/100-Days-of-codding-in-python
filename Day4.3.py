row1 = ["_","_","_"]
row2 = ["_","_","_"]
row3 = ["_","_","_"]

map = [row1, row2, row3] 
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the  treasure ")
list_position = list(position)
print(list_position)
map[int(list_position[1])-1][int(list_position[0])-1] = "X" # map[index of line][index of row] to access a specified location.
print(f"{row1}\n{row2}\n{row3}")