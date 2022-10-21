def test_is_valid(test):
    if isinstance(test, int):
        return 3 >= test >= 1
    else:
        return False


def find(word, letter):
    index = 0
    for character in word:
        if character == letter:
            return index
        index += 1
    return -1


print(test_is_valid(2))
print(test_is_valid("string"))
print(test_is_valid("14"))
print(test_is_valid(13))

fruit = "banana"
print(f"The third letter in banana is {fruit[2]}")
print(fruit[3:0:-1])

print(find(fruit, 'n'))
