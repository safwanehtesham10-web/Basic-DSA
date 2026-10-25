def generate_subsequences(text, idx=0, current=""):
    if idx == len(text):
        print(f"'{current}'", end=" ")
        return
    generate_subsequences(text, idx + 1, current + text[idx])
    generate_subsequences(text, idx + 1, current)

generate_subsequences("abc")
