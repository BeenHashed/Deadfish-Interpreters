from sys import argv

program = argv[1]
try:
    with open(program, "r") as f:
        code = f.read()
except FileNotFoundError:
    print("File not found")
    quit()

accumulator = 0
for i in code:
    if accumulator >= 256 or accumulator < 0:
        accumulator = 0

    if i == "i":
        accumulator += 1
    elif i == "d":
        accumulator -= 1
    elif i == "s":
        accumulator *= accumulator
    elif i == "o":
        print(accumulator, end=" ")
