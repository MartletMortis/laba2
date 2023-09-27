def checkx(x):
    if isinstance(x, list):
        try:
            sum = 0
            for i in x:
                if i % 2 == 0:
                    sum += i
                for i in x:
                    if i == 0:
                        x.remove(i)
            print("Sum is: ", sum)
            print("New list is: ", x)

        except ValueError:
            print("No-no-no, Mr. Fish.")

    elif isinstance(x, set):
        try:
            i = max(x)
            print("Max element: ", i)
            x.remove(i)
            print("New set is: ", x)

        except ValueError:
            print("No-no-no, Mr. Fish.")

    elif isinstance(x, int):
        try:
            k = 0
            for i in range(2, x // 2 + 1):
                if x % i == 0:
                    k = k + 1
            if k <= 0:
                print("The number is prime!")
            else:
                print("The number is not prime!")

        except ValueError:
            print("No-no-no, Mr. Fish.")

    elif isinstance(x, str):
        try:
            max_count = 0
            max_char = ' '
            for i in range(len(x)):
                if x.count(x[i]) >= max_count:
                    max_count = x.count(x[i])
                    max_char = x[i]
            print("Max letter: ", max_char)

        except ValueError:
            print("No-no-no, Mr. Fish.")

    return('-----------')


print(checkx(list((0, 3, 7, 6, 4, 0, 8, 5))))
print(checkx({3, 5, -6, 9, 10, 0, -1, 4}))
print(checkx(7))
print(checkx("Hellloo!"))
