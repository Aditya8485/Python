example = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    [0]
]

print(example[0][0]) #accessing individually

for row in example:
    print(row)
    for col in example:
        print(col)

        """This one is nested loop , mean loop in loop
        That's all about 2d lists & nested Loops..."""