a1 = {'a':1, 'b':13, 'd':4, 'c':2, 'e':30}
a1_sorted_keys = sorted(a1, key=a1.get, reverse=True)
a1_sorted_keys_2 = sorted(a1, key=a1.get)

print(a1_sorted_keys)
print(a1_sorted_keys_2)
