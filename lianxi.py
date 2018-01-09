s=input()
d=dict([(i,s.count(i)) for i in set(s) if i.isalpha()])
print(d.values())
for i in d.keys():
    print(i,d[i])