tup = ()
tup1=('a','b','c','d')
tup2=('a','b',[1,2,3],['lemon','apple'])
# print(tup2[2][0])
# print(tup2[3][1])
# new_tuple = tup2[0:2]
# print(new_tuple)
# for item in enumerate(tup2):
#     print(item)
# print(sorted(tup1, reverse=True))

example_set={} 
myset={1,2,2,3,3,4,4,5,5,6,6} # only unique values will contains in set
# print(len(myset)) set elements will store based hash values
myset.add(24)
# sample_set1={1,2,['a','b','c']} # set elements must be immutable (list element is mutamable) but sets are mutuable
sample_set2={1,2,('a','b','c')} # set elements must be immutable (tuple element is immutable) but sets are mutuable
print(sample_set2)
# A&B, A|B
# A={1,2,3}
# B={4,5,6}
# print(A.union(B)) 

