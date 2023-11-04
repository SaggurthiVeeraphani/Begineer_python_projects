Outer_list = []

Outer_list_size = int(input("Enter the size of the list: "))
Inner_list_size = int(input("Enter the inner list elements size: "))

for x in range(0,Outer_list_size):
    inner_list = []
    for y in range(0,Inner_list_size):
        inner_list.append(int(input("Enter the input: ")))
    Outer_list.append(inner_list)

print(Outer_list)

ans_list = []
if Outer_list_size <= 1 :
    print("There is only one list in the input")
else:
    for x1 in range(0,Outer_list_size):
        ans_inner_list = []
        for y1 in range(0,Inner_list_size):
            ans_inner_list.append(Outer_list[y1][x1])
        ans_list.append(ans_inner_list)

print(ans_list)
