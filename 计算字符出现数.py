from collections import Counter

V2EX = 'ebreredfdfhdlfhferdlhgfdnhe' 
v2ex_count = { str : V2EX.count(str) for str in set( V2EX )} 
print(v2ex_count)
print(Counter(V2EX))