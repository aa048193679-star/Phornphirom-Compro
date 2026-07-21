# Failed
print_column = int(input("Enter the number of column: "))
for i in range(1, 101):
    print(f"{1:>3}", end="")
    if i % print_column == 0:
        print()