# Python – Swap elements in String list

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

print(str(test_list))


# method-1 by replace
res = [sub.replace("G", "-").replace("e", "G").replace("-", "e")
       for sub in test_list]
print(res)

# method-2 by join and replace
res1 = ", ".join(test_list)

res1 = res1.replace("G", "-").replace("e", "G").replace("-", "e").split(", ")
print(res1)
