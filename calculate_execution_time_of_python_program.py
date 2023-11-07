# from time import time
# start = time()
#
# word = "North Atlantic treaty Organisation"
# a = word.split()
# ans = ""
# for i in a:
#     ans = ans + str(i[0]).upper()
# print(ans)
#
# end = time()
#
# execution_time = end - start
#
# print(execution_time)


from time import time
start = time()

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start

execution_time = round(execution_time, 4)

print("Execution Time : ", execution_time)
