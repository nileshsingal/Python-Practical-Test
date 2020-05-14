# Given2strings,s1ands2,create a new string by appending s2 in the middle of s1

def appendMiddle(s1, s2):
  middleIndex = int(len(s1) /2)
  middleThree = s1[:middleIndex-1:]+ s2 +s1[middleIndex-1:]
  print(middleThree)
  
appendMiddle("Chrisdem", "IamNewString")
