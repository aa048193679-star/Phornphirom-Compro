# Success
Score1 = int(input("Enter your score for test 1: "))
Score2 = int(input("Enter your score for test 2: "))
Score3 = int(input("Enter your score for test 3: "))
Average  = (Score1 + Score2 + Score3) / 3
print("The average score is " , format(Average, '.2f'))
if Average > 95:
    print("Congratulations!\nThat is a great average!")