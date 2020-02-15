def catalan(n):
	num = 1
	print('0 - ',num)
	i = 0
	while num < n:
		i += 1
		num = ((4*i+2)/(i+2))*num
		print(i,' - ',num)

#catalan(1000000000)

from numba import jit

@jit
def plane(diag, L):
    num = 0
    for i in range(diag+2,L+1):
        for j in range(diag+1,i):
            num += (-1) ** ((diag + i + j)) / (diag ** 2 + i ** 2 + j ** 2)**0.5
    num = num*2
    for i in range(diag+1,L+1):
        num += ((-1) ** (diag + i*2)) / (diag ** 2 + (i ** 2)*2)**0.5
    return num

@jit
def line(diag, L):
    num = 0
    for i in range(diag+1,L+1):
        num += (-1) ** (i) / ((diag ** 2)*2 + i ** 2)**0.5 # diag*2 é um número par
    return num

@jit
def main(L):
    octant = 0
    for i in range(1,L-2):
        octant += 3*plane(i,L) + 3*line(i,L) + ((-1) ** (i) / (  3*(i ** 2))**0.5)
    for i in range(L-2,L+1):
        for j in range(L-2,L+1):
            for k in range(L-2,L+1):
                octant += (-1) ** ((k + i + j)) / (k ** 2 + i ** 2 + j ** 2)**0.5

    return 8*octant + 12*plane(0,L) + 6*line(0,L)

print(main(700))