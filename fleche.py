x = int(input())
x = x*2 - 1
t = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']*2

for i in range(x):
    for j in range(x):
        if i + j < x:
            print(t[min(i,j)], end="")
        else:
            print(t[x - max(i,j) - 1], end="")
        print('', end="")
    print("")

# a a a a a a a a a 
# a b b b b b b b a 
# a b c c c c c a e 
# a b c d d d a e d 
# a b c d e a e d c 
# a b c d a a d c b 
# a b c b b b b b a 
# a b c c c c c c e 
# a d d d d d d d d 