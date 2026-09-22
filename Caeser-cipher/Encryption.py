red = "\033[31m"
reset = "\033[0m"

print(f"This program uses the Caesar cipher to encrypt documents.")
print(f"Please ensure the program is in the same folder as the file to be processed ({red}content.txt{reset})\n")
print(f"And if you need to write in file, please ensure that you have file ({red}encryptionResult.txt{reset} also)\n")
def domove(movecount, text): # shift of letter
    final_text = []
    for char in text:
        if 'A' <= char <= 'Z': # upper letter shift
            new_char = chr((ord(char) - 65 + movecount) % 26 + 65)
            final_text.append(new_char)
        elif 'a' <= char <= 'z': # lower letter shift
            new_char = chr((ord(char) - 97 + movecount) % 26 + 97)
            final_text.append(new_char)
        else:
            final_text.append(char) # keep symbol and space
            
    shifted_string = "".join(final_text)
    print(shifted_string)
    return shifted_string

def yesno(filename): # User can choose to upload result to file
    while True:
        choice = input(f"{red}Do you want to output to {filename}.txt? (yes/no):{reset} ").strip().lower()
        if choice in ["yes", "no"]:
            return choice
        print("Please re-enter yes or no")

# main logic (read txt file)

try:
    with open("content.txt", 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: {red}content.txt{reset} not found. Please create the file first!")
    exit()

# get shift num
while True:
    try:
        move = int(input("Enter the shift value for letters: "))
        break
    except ValueError:
        print("Please enter a number")
        
print("\n--- Encryption Result ---")
result_text = domove(move, content)
print("\n")

# write result
if yesno("content") == "yes":
    with open('encryptionResult.txt', 'a', encoding='utf-8') as file:
        file.write(result_text)
    print(f"{red}Write complete. Please check encryptionResult.txt{reset}")