f = open("/home/sherry/repos/py-stuff/iranian-dictionary/temp.txt", "w")
num = 0

# remove first repeating pattern before our clean name words, we're avoiding change in raw
with open("/home/sherry/repos/py-stuff/iranian-dictionary/raw-source/raw.txt") as file:

    for line in file:
        num = num + 1
        text = f'<div class="nmlst">{num}) <strong><a href="../'

        if text in line:
            line = line.replace(text, "")
            f.write(line)
f.close()

# remove EVERYTHING after our clean word
with open("/home/sherry/repos/py-stuff/iranian-dictionary/temp.txt") as file:

    word = ""
    for line in file:
        for letter in line:
            # easiest way to avoid html bullshittery messing with our word, since it's repeated
            if letter == "/":
                break
            word += letter
        word += "\n"

# write clean words in finish.txt
    with open("/home/sherry/repos/py-stuff/iranian-dictionary/finish.txt", "w") as f:

        f.write(word+"\n")
