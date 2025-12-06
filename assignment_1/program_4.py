# A cashier has currency notes of denominations 10, 50 and 100.
# If the amount to be withdrawn is input through the keyboard in hundreds,
# find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.

cash = int(input("Enter the amount: "))

# 100 notes
n_100 = cash // 100
cash = cash % 100

# 50 notes
n_50 = cash // 50
cash = cash % 50

# 10 notes
n_10 = cash // 10
cash = cash % 10

print(n_100)
print(n_50)
print(n_10)
