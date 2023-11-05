method_input = input("Please enter the required method : 1.mean 2.median 3.mode : ").lower()

if method_input == "mean":
    List = []
    input_size = int(input("Please enter the size of list :"))
    for x in range(0,input_size):
        List.append(int(input("enter the input value :")))
    print(sum(List)/len(List))
elif method_input == "median":
    List = []
    input_size = int(input("Please enter the size of list :"))
    for x in range(0,input_size):
        List.append(int(input("enter the input value :")))
    if input_size % 2 == 0:
        value1 = int(len(List)/2)
        value2 = value1-1
        sum = List[value1]+List[value2]
        ans = sum/2
        print(ans)
    else:
        index = int(input_size/2)
        print(List[index])
elif method_input == "mode":
    List = []
    input_size = int(input("Please enter the size of list :"))
    for x in range(0,input_size):
        List.append(int(input("enter the input value :")))
    ans_dic = {}
    for i in List:
        ans_dic.setdefault(i, 0)
        ans_dic[i] += 1
    max_count = max(ans_dic.values())
    for key,value in ans_dic.items():
        if ans_dic[key] == max_count:
            mode = key
    print(mode)
else:
    print("please enter valid input")








