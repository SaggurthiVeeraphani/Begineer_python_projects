def find_missing_number(num):
    num_set = set(num)
    ans_list = []
    for j in range(1, num[-1]):
        if j not in num_set:
            ans_list.append(j)
    return ans_list




n = int(input("enter the size of the list: "))
List = []
for i in range(0, n):
    number = int(input())
    List.append(number)

ans = find_missing_number(List)
print(ans)

