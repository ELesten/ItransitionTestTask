import random


def sort(array: list) -> list:
    if len(array) < 2:
        return array

    else:
        random_pivot = random.randint(0, (len(array) - 1))
        array[0], array[random_pivot] = array[random_pivot], array[0]
        pivot = array[0]
        less = []
        greater = []

        for i in array[1:]:
            if bin(i).count("1") < bin(pivot).count("1"):
                less.append(i)

            elif bin(i).count("1") > bin(pivot).count("1"):
                greater.append(i)

            else:
                if i < pivot:
                    less.append(i)

                else:
                    greater.append(i)

        return sort(less) + [pivot] + sort(greater)
