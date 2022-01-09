from sys import argv

program = argv[1]
try:
    with open(program, "r") as f:
        code = f.read()
except FileNotFoundError:
    print("Need to provide a file in current directory")
    quit()

accumulator = 0
for i in code:
    if i == "i":
        accumulator += 1
        if accumulator == 255:
            accumulator = 0

    elif i == "d":
        accumulator -= 1
        if accumulator == 0:
            accumulator = 255

    elif i == "s":
        accumulator *= accumulator
    elif i == "o":
        print(accumulator, end=" ")
