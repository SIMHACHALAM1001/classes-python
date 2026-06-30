# question:
# input = {
#     2:3,
#     4:1,
#     5:2,
#     1:4
# }
# output : sort based on values
# { key: value}
# output = {
#     4:1,
#     5:2,
#     2:3,
#     1:4
# }

# plan input---> [],[(1,2),(2,3),(3,4)]
# input = {
#     2:3,
#     4:1,
#     5:2,
#     1:4
# }

#step1:
# [(key,value)]
#[(2,3),(4,1),(5,2),(1,4)] # input.items() // input.keys() [2,4,5,1] // input.values() [3,1,2,4]

# explanation
#[(4,1),(5,2)(2,3)(1,4)] # sort based on value  sorted(input.items(), key=lambda x:print(x), reverse=True)
# map , filter ,reduce ---> lambda x:x, data
# sort --->data, key=lambda x:x

# data = ('a','b','c','d')
# data[2]

# step2:
#[(2,3),(4,1),(5,2),(1,4)]
# (2,3) --> key=value --> 1st iteration---> x[1]--->3
#  0,1
# (4,1)---> key=value -->2nd iteration-->x[1]---> 3>1 -->(4,1)(2,3)
# (5,2)--> key=value -->3rd--->x[1]-->3>2>1 -->(4,1)(5,2)(2,3)
# (1,4)---> key=value -->4th--->x[1]--->(4,1)(5,2)(2,3)(1,4)
# result=list(sorted(input.items(), key=lambda x:x[1]))
# dict(result)---->{4:1,5:2,2:3,1:4}
# sorted ---> merge sort algorith O(n) --> sorting algorithms techniques --> bubble sort O(n^2) , quick sort O(nlogn), merge sort(o(n)) 
# [4,2,3,4] ---> nested loops --> sorting algorithms 
input = {
    2:3,
    4:1,
    5:2,
    1:4
}
# result=sorted(input.items(), key=lambda each_item:each_item[0]) # sorted based on keys
result=sorted(input.items(), key=lambda each_item:each_item[1]) # sorted based on values
print(dict(result))


# class
# object
# inheritance 
# property attribute, class attribute
# decarator, yield & generators
# django rest framework  with simple two api's
# will try to connect with sql database.