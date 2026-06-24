with open("hidden_eye/story.txt", "r", encoding="utf-8") as f:
    content = f.read()

binary_str = ""
for char in content:
    if char == " ":
        binary_str += "0"
    elif char == "\u200b":
        binary_str += "1"
print(binary_str)