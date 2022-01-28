def greeting(message, name):
    print(f"Hello! {name}")
    print(message)


l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3]

check = all(el in l1 for el in l2)

if l1 == l2:
    print("equal")

print(check)
