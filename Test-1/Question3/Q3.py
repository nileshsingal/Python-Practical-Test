# Arrange String characters such that lowercase letters should come first


inputStr = input("Enter String :")
words = inputStr.split()
lower = []
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = ''.join(lower + upper)
print(sortedString)
