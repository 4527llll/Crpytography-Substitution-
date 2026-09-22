red = "\033[31m"
reset = "\033[0m"

def brute_force_caesar(ciphertext): # bruteForce function
    all_results = "" 
    
    for shift in range(1, 26):
        decrypted_text = []
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                new_char = chr((ord(char) - 65 - shift) % 26 + 65)
                decrypted_text.append(new_char)
            elif 'a' <= char <= 'z':
                new_char = chr((ord(char) - 97 - shift) % 26 + 97)
                decrypted_text.append(new_char)
            else:
                decrypted_text.append(char)
                
        result = "".join(decrypted_text)
        line_result = f"Tried shift {shift:2d} : {result}\n"
        print(line_result, end="")  
        all_results += line_result  
        
    return all_results

def yesno(filename): # User can choose to upload result to file
    while True:
        choice = input(f"{red}Do you want to output to {filename}.txt? (yes/no):{reset} ").strip().lower()
        if choice in ["yes", "no"]:
            return choice
        print("Please re-enter yes or no")

if __name__ == "__main__":
    print(f"This program uses the Brute-force attack to decrypt documents.")
    print(f"Please ensure the program is in the same folder as the file to be processed ({red}content.txt{reset})\n")
    
    try:
        with open("encryptionResult.txt", 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {red}encryptionResult.txt{reset} not found. Please create the file first!")
        exit()
        
    final_results = brute_force_caesar(content)
    print("\n")
    
    if yesno("decryptionResult") == "yes":
        with open('decryptionResult.txt', 'w', encoding='utf-8') as file:
            file.write("**************** Brute-force result ****************\n")
            file.write(final_results)
        print(f"{red}Write complete. Please check decryptionResult.txt{reset}")