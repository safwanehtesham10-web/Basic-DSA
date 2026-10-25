def find_permutations(chars, prefix=""):
    if not chars:
        print(prefix, end=" ")
        return
    for idx in range(len(chars)):
        rest = chars[:idx] + chars[idx + 1:]
        find_permutations(rest, prefix + chars[idx])

find_permutations("abc")
