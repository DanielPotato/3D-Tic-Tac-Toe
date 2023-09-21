def print_empty_rhombus():
    for i in range(5):
        if i == 0 or i == 4:
            print(" " * (4 - i) + "*" * 5)
        else:
            print(" " * (4 - i) + "*" + " " * 3 + "*")

print_empty_rhombus()
