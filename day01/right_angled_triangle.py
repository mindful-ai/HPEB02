# Program to find if the given three points form a right angled triangle

# Input

ax = float(input("AX: "))
ay = float(input("AY: "))

bx = float(input("BX: "))
by = float(input("BY: "))

cx = float(input("CX: "))
cy = float(input("CY: "))


# Process

ab_sq = (ax - bx) ** 2 + (ay - by) ** 2
bc_sq = (bx - cx) ** 2 + (by - cy) ** 2
ac_sq = (ax - cx) ** 2 + (ay - cy) ** 2

flag = False
if ( ab_sq == bc_sq + ac_sq ):
    flag = True
elif ( bc_sq == ac_sq + ab_sq ):
    flag = True
elif ( ac_sq == ab_sq + bc_sq):
    flag = True
else:
    flag = False

# Output

if(flag == True):
    print('The points form a right angled triangle')
else:
    print('The points do not form a right angled triangle')

    
