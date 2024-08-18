
file = open("sample.txt", "r")
lines = file.readlines()
file.close()

st = ""
zz = [".", ",", "!", "?", ":", ";", "...", "!?"]
bb = ["a", "e", "i", "o", "u", "h"]
ready_string = ""

for line in lines:
    word = line.split(' ')
    i = 0
    while i < len(word):
        if word[i] == "(low)":
            if i > 0:
                word[i - 1] = word[i - 1].lower()
                del word[i]
                continue
        elif word[i] == "(up)":
            if i > 0:
                word[i - 1] = word[i - 1].upper()
                del word[i]
                continue
        elif word[i] == "(cap)":
            if i > 0:
                word[i - 1] = word[i - 1].capitalize()
                del word[i]
                continue
        elif word[i].startswith("(low,"):
            idx = int(word[i + 1].replace(")", ""))
            if i > 0:
                for j in range(1, idx + 1):
                    word[i - j] = word[i - j].lower()
                del word[i:i + 2]
                continue
        elif word[i].startswith("(cap,"):
            idx = int(word[i + 1].replace(")", ""))
            if i > 0:
                for j in range(1, idx + 1):
                    word[i - j] = word[i - j].capitalize()
                del word[i:i + 2]
                continue
        elif word[i].startswith("(up,"):
            idx = int(word[i + 1].replace(")", ""))
            if i > 0:
                for j in range(1, idx + 1):
                    word[i - j] = word[i - j].upper()
                del word[i:i + 2]
                continue
        elif any(ext in word[i] for ext in zz):
            if word[i].startswith(tuple(zz)):
                word[i-1] = word[i-1] + word[i][0:1].rstrip()
                word[i] = word[i][1:len(word[i])]
        elif word[i].startswith("'"):
            if i != len(word)-1:
                word[i+1] = word[i] + word[i+1]
                del word[i]
            else:
                last_index = len(word) - word[::-1].index(word[i-1])
                ind = 1
                while ind > 0:
                    if not bool(word[last_index - ind]):
                        ind += 1
                    else:
                        word[last_index-ind] = word[last_index-ind] + word[last_index]
                        break
                del word[last_index]
        elif word[i] == "a" and word[i+1].startswith(tuple(bb)):
            word[i] = word[i] + "n"
        elif word[i] == "(bin)":
            word[i-1] = str(int(word[i-1], 2))
            del word[i]
            continue
        elif word[i] == "(hex)":
            word[i-1] = str(int(word[i-1], 16))
            del word[i]
            continue
        i += 1
    st = " ".join(word).split()
    st = " ".join(st)
    ready_string += st + "\n"

with open("result.txt", "w") as file:
    file.write(ready_string)
