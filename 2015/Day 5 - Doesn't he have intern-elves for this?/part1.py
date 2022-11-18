from re import search


def is_nice(string):
    return search(r"(\w)\1", string) and not search(r"ab|cd|pq|xy", string) \
        and search(r"(?:[aeiou]\w*){3,}", string)


count = sum(1 for string in open("input.txt", "r").readlines()
            if is_nice(string))
print(f"The number of nice strings found under these conditions was {count}")
