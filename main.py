def reverse(n):
    rev = 0
    while (n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10

    return rev

if __name__ == '__main__':

    # Random four numbers within 1-9
    # from max to min, minus from min to max
    # Repeat and rinse, within 7 iteration, the pass word will be shown.
    num = 1234



    for i in range(7):
        if (reverse(num) > num):
            num = reverse(num) - num
        else:
            num = num - reverse(num)
        print(num)


    print("Kristen is my fiancee")


