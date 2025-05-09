
"""
#Q1
l1=["suraj","suraj",1,1,1,1,11]
for e in set(l1):
    print(e)


    


#Q2


l1={1,2,3,4,5,6,7,8,9}
l2=set()
l3=set()
for e in l1:
    if e%2==0:
        l2.add(e)
    else:
        l3.add(e)
print(l2,l3)




s1={"vivek","irfan","chiru","mohit","mote"}
l1=list(s1)
l2=[]
i=0
for e in l1:
    i+=1
    j=i
    while j<len(l1):
        l3=[]
        l3.append(e)
        l3.append(l1[j])
        l2.append(tuple(l3))
        j+=1
print(set(l2))

#Q4
s1=set(["ramesh","suraj","vivek","raju","irfan"])
s2=set(["surash","kisan","vivek","hasan","irfan"])
print(s1.intersection(s2))

"""
#Q5
N=int(input("enter a number"))
l1=[]
for e in range(1,N):
    t1=[]
    if e<=N:
        t1.append(e)
        t1.append(N-e)
        l1.append(tuple(t1))
print(set(l1))

