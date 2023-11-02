#
from collections import defaultdict


def group_anagrams(List):
    new_dict = defaultdict(list)
    for i in range(len(List)):
        val = List[i]
        sorted_val = str(''.join(sorted(val)))
        new_dict[sorted_val].append(val)
    return new_dict



#This is for input number
number_of_elements = int(input("Please enter the number of elements: "))
List = []

for x in range(0, number_of_elements):
    input_str = str(input("Enter the value: "))
    List.append(input_str)

print(group_anagrams(List).values())