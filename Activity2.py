Amount = int(input("Enter the amount of money for Withdrawal: "))

note_1 = Amount // 1000
note_2 = (Amount%1000) // 100
note_3 = (Amount%100) // 50
note_4 = (Amount%50) // 10

print("Number of 1000 notes:", note_1)
print("Number of 100 notes:", note_2)
print("Number of 50 notes:", note_3)
print("Number of 10 notes:", note_4)