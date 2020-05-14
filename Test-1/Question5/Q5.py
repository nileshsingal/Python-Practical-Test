#5. Given a two list. Create a third list by picking an odd-index element from the first list and even index
#elements from second.
list1= [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
odd_list=[]
even_list=[]
for i in range(0,len(list1)):
    if i%2==1:
       odd_list.append(list1[i])

    else:
        even_list.append(list2[i])
   
print("Element at odd-index positions from list one:",odd_list)
print("Element at odd-index positions from list two:",even_list)
print("Printing Final third list:",odd_list + even_list)
