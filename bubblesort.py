num=[5,8,4,7,99,20]

def b_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
    print(num)

b_sort(num)
