'''
[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
'''
a = [[1,2],[3,4],[5,6]]
b = [j for i in a for j in i]
# for i in range(len(a)):
#    for j in range(len(a[i])):
#        b.append(a[i][j])
print(b)
c= "he"+"lo"
print(c)
