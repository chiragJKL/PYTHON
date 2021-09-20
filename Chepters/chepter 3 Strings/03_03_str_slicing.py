a = "chirag"

# here in c  h  i  r  a  g
#         0  1  2  3  4  5  starts from  0
#        -6 -5 -4 -3 -2 -1  starts from -1
# c = name[0] or name[-6]
# h = name[1] or name[-5]
# i = name[2] or name[-4]
# r = name[3] or name[-3]
# a = name[4] or name[-2]
# g = name[5] or name[-1]........meaning it starts from 0

print(a[0])
print(a[1])

print(a[-1])  # used when long str is there and we dont know lengh
print(a[-6])

# str slicing

print(a[0:3])  # this meaning take name [0] [1] [2] ***NOT 3
print(a[1:4])  # this meaning take name [1] [2] [3] ***NOT 4
print(a[2:6])


print(a[:3])  # is same as a[0:3]
print(a[2:])  # is same as a[2:6"last latter"]

b = "lunagaria"
print(b[0:9])
print(b[0:9:2])  # means print 0 to 9 and SKIP EVERY SECOND LATTER
print(b[2:9:2])  # means print 2 to 9 and SKIP EVERY SECOND LATTER
print(b[0:9:3])  # means print 0 to 9 and SKIP EVERY SECOND LATTER

print(b[0::2])  # means print 0 to 9 (LAST) and SKIP EVERY SECOND LATTER
