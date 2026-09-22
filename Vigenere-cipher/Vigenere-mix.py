red = "\033[31m"
reset = "\033[0m"

print(f"This program uses the Vigenere cipher to encrypt and decrypt documents.")
print(f"For encryption: reads {red}content.txt{reset} -> writes to {red}encryptionResult.txt{reset}")
print(f"For decryption: reads {red}encryptionResult.txt{reset} -> writes to {red}decryptionResult.txt{reset}\n")

def keyread(action):
    key_list = []
    key = input(f"please enter the key for {action} : ")
    for i in key:
        if 'A' <= i <= 'Z':
            key_list.append(ord(i) - 65)
        elif 'a' <= i <= 'z':
            key_list.append(ord(i) - 97)
    return key_list

def domove(keyResult, text, mode): 
    final_text = []
    if len(keyResult) == 0: # avoid blank key
        print("Error: No valid key entered.")
        return text

    keyLength = len(keyResult)
    keyIndex = 0
    for char in text:
        if 'A' <= char <= 'Z': # upper letter shift
            shift = keyResult[keyIndex % keyLength]
            if mode == "decrypt":
                shift = -shift  # decrypt
                
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            final_text.append(new_char)      
            keyIndex += 1
            
        elif 'a' <= char <= 'z': # lower letter shift
            shift = keyResult[keyIndex % keyLength]
            if mode == "decrypt":
                shift = -shift  # decrypt
                
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            final_text.append(new_char)
            keyIndex += 1
            
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

while True: # choosse encrypt or decrypt
    try:
        lockTF = int(input(f'{red}Enter 1 to encrypt, 2 to decrypt:{reset} '))
        if lockTF in [1, 2]:
            break
        else:
            print("Please enter 1 or 2")
    except ValueError:
        print("Please enter an integer")

if lockTF == 1: # main encryption
    try:
        with open("content.txt", 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {red}content.txt{reset} not found. Please create the file first!")
        exit()

    keyResult = keyread("encryption")
    print("\n--- Encryption Result ---")
    result_text = domove(keyResult, content, "encrypt")
    print("\n")

    if yesno("encryptionResult") == "yes":
        with open('encryptionResult.txt', 'w', encoding='utf-8') as file:
            file.write(result_text)
        print(f"{red}Write complete. Please check encryptionResult.txt{reset}")

elif lockTF == 2: # main decryption
    try:
        with open("encryptionResult.txt", 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {red}encryptionResult.txt{reset} not found. Please encrypt a file first!")
        exit()

    keyResult = keyread("decryption")
    print("\n--- Decryption Result ---")
    result_text = domove(keyResult, content, "decrypt")
    print("\n")

    if yesno("decryptionResult") == "yes":
        with open('decryptionResult.txt', 'w', encoding='utf-8') as file:
            file.write(result_text)
        print(f"{red}Write complete. Please check decryptionResult.txt{reset}")