import math

num = 2

print(math.sqrt(num))

s = 'hello'

print(s[1])
print(s[::-1])

len_s = len(s) - 1
print(s[len_s])
print(s[-1])

Test_list = [0,0,0]
Test_list1 = [0]
Test_list1 = Test_list1 *3
print(Test_list1)

list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'Good bye'

print(list3)

list4 = [5,3,4,6,1]

list4.sort()

print(list4)

d = {'simple_key':'hello'}

print(d['simple_key'])

d = {'k1':{'k2':'hello'}}

print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])


l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

print(l_one[2][0] >= l_two[2]['k1'])










