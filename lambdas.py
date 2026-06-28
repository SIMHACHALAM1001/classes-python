# lambda , filter, map, reduce

# lambda ---> anonymous function --> a function with out a name
# add = lambda a,b,c: a if a==5 else b+c
# print(add(3,6,7))

# sample ---> name of the function
# def sample(args):
#     print(args)

# sample("hello")

# filter  ---> even numbers from the list 
# data [10, 17, 30, 19, 20] ---> [10, 30, 20]

# data = [10, 17, 30, 19, 20]
# filter_data =list(filter(lambda a:a%2==0,data))
# print(filter_data)

# map ---> changing the data in the list
# data [2,4,5,6] ---> [4,8,10,12]
# data = [2,4,5,6]
# map_data = map(lambda a: a*2, data)
# print(list(map_data))

# reduce ---> reducing the data in the list to a single value
# data [2,4,5,6] ---> 2+4+5+6=17 --> output is 17
# from functools import reduce

# data = [2,4,5,6]
# count = 0
# count = count+a
# count = count+a
# count = count+a
# count = count+a
# print(count)
# a --> 2
# b --> 4
# a-- none, b =5 # a=6(4+2), b=5
# a-- none, b =6 # a=11(6+5), b=6
# a-- accumulator, b = element of the list

# reduce_data_no_sum_logic = reduce(lambda a,b: '', data)
# print(reduce_data_no_sum_logic)

# reduce_data_sum = reduce(lambda a,b: a+b, data)

# print(reduce_data_sum)

# data = [2,4,5,6]
# # result=[]
# # for item in data:
# #     result.append(item*2)
# # print(result)
    
# yz = [item*2 for item in data if item%2==0]
# print(yz)

# data = [4,6,3,5,8]
# print(sorted(data, key=lambda x: print(x) or 0))