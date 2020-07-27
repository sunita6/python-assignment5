#sort increasing order but all zeros should be at right hand side

print("sorting the list")
str1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
str1.sort(key=lambda v:v==0)
print(str1)

#output
#sorting the list
#[1, 2, 10, 4, 1, 56, 2, 1, 3, 56, 4, 0, 0, 0, 0, 0]
