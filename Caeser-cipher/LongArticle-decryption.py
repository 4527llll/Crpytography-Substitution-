red = "\033[31m"
reset = "\033[0m"

def manyE(text): # count the most letter as "e"
    countword = [0] * 26  
    
    for char in text:
        if 'a' <= char.lower() <= 'z':
            countword[ord(char.lower()) - 97] += 1
            
    # grap the index and return as the letter (ascii)
    max_char = chr(countword.index(max(countword)) + 97)

    encrypt_shift = (ord(max_char) - ord('e')) % 26
    decrypt_shift = (26 - encrypt_shift) % 26
    
    print(f"The highest number have been count of letter is '{max_char}'。")
    print(f"The original displayment is calculated as: {encrypt_shift}，do decryption shift: {decrypt_shift}...\n")
    return decrypt_shift

def domove(movecount, text): # decryption main logic
    final_text = []
    for char in text:
        if 'A' <= char <= 'Z':
            new_char = chr((ord(char) - 65 + movecount) % 26 + 65)
            final_text.append(new_char)
        elif 'a' <= char <= 'z':
            new_char = chr((ord(char) - 97 + movecount) % 26 + 97)
            final_text.append(new_char)
        else:
            final_text.append(char)
            
    return "".join(final_text)

def yesno(filename): # write or not
    while True:
        choice = input(f"{red}Do you want to output to {filename}.txt? (yes/no):{reset} ").strip().lower()
        if choice in ["yes", "no"]:
            return choice
        print("Please re-enter yes or no")

if __name__ == "__main__":
    print(f"This program uses Frequency Analysis (Targeting 'e') to decrypt long documents.")
    print(f"Please ensure the file is named {red}decryptionResult.txt{reset}\n")
    
    # read file
    try:
        with open("encryptionResult.txt", 'r', encoding='utf-8') as de:
            decryption_text = de.read()
    except FileNotFoundError:
        print(f"Error: {red}decryptionResult.txt{reset} not found. Please create the file first!")
        exit()

    shift_amount = manyE(decryption_text)  # get shift
    
    print("--- Decryption Result ---")
    result_text = domove(shift_amount, decryption_text)
    print(result_text)
    print("\n")
    
    if yesno("decryptionResult") == "yes":  # write out
        with open('decryptionResult.txt', 'w', encoding='utf-8') as file:
            file.write("**************** Frequency analysis result ****************\n")
            file.write(result_text)
        print(f"{red}Write complete. Please check decryptionResult.txt{reset}")