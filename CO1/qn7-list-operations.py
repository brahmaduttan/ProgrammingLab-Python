lst1 = [6,9,3,5,7]
lst2 = [9,6,4,2,0,7,2]
print("lst1=",lst1)
print("lst2=",lst2)
a = len(lst1)
b = len(lst2)

if a == b:
    print("SAME LENGTH")
else:
    print("NOT SAME LENGTH")
    
s1 = sum(lst1)
s2 = sum(lst2)
if s1 == s2:
    print("SUM IS SAME")
else:
        print("SUM IS NOT SAME")

lst1 = set(lst1)
lst2 = set(lst2)
i = lst1.intersection(lst2)
i = list(i)
print("Common values:",i)
