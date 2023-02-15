A = int(input("Enter number: "))
B = int(input("Enter begree: "))

def exponentiation(A, B):
    if B == 0:
        return 1
    else:
        return exponentiation(A, B-1)*A

print(exponentiation(A, B))
