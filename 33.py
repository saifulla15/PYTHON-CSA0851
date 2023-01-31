def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*fact(n-1))

def Small_List(nums):
    l=len(nums)
    ans=[]
    count=0
    for i in nums:
        for j in range(i+1,len(l)):
            if (nums[j]-i)<0:
                count+=1
        ans.append(count)
        count=0
    return ans

L=[8,1,2,2,3]
f=(Small_List(L))
print(f)
for i in range(len(f)):
    print(fact(f[i]), end="  ")
