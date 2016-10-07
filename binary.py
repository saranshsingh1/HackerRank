'''Count the highest number of consecutive ones in a binary number'''

n = int(raw_input().strip())            #Enter the number in decimal form

lst = []
total, ones = 0, 0

while n:
    lst.append(n % 2)
    n /= 2

print ''.join(map(str, lst[::-1]))      #Shows the input in binary form

for i in lst:
    if i:
        ones += 1
    else:
        if total < ones:
            total = ones
        ones = 0


print ones if ones > total else total

