def fibonacci_number(n):
    F = [0, 1]
    if n <= 1:
        return n
    for i in range(2,n):
        F.append(F[i-1] + F[i-2])
    return F[n-1]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

