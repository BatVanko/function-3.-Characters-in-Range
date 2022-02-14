def range_characters(f, s):
    first = ord(f)
    second = ord(s)
    for ch in range(first + 1, second):
        print(chr(ch), end=" ")


char1 = input()
char2 = input()
range_characters(char1, char2)
