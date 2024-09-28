def rail_fence_encrypt(text, key):
    """
    Encrypts the given text using the Rail Fence Cipher with the specified key.
    
    Parameters:
    - text (str): The plaintext to encrypt.
    - key (int): The number of rails (key) to use for encryption.
    
    Returns:
    - str: The encrypted ciphertext.
    """
    try:
        if key <= 0:
            raise ValueError("Key must be a positive integer.")
        
        # Remove spaces from the text
        text = text.replace(" ", "")
        
        # Initialize the matrix with 'X' as filler
        matrix = [['X' for _ in range(len(text))] for _ in range(key)]
        flag = False
        row, col = 0, 0

        # Populate the matrix in a zig-zag pattern
        for char in text:
            if row == 0 or row == key - 1:
                flag = not flag
            matrix[row][col] = char
            col += 1
            row += 1 if flag else -1

        # Read the matrix row-wise to get the encrypted text
        encrypted = ''.join([matrix[r][c] for r in range(key) for c in range(len(text)) if matrix[r][c] != 'X'])
        return encrypted
    except Exception as e:
        print(f"Encryption Error: {e}")
        return None

def rail_fence_decrypt(cipher, key):
    """
    Decrypts the given ciphertext using the Rail Fence Cipher with the specified key.
    
    Parameters:
    - cipher (str): The ciphertext to decrypt.
    - key (int): The number of rails (key) that was used for encryption.
    
    Returns:
    - str: The decrypted plaintext.
    """
    try:
        if key <= 0:
            raise ValueError("Key must be a positive integer.")
        if key == 1:
            return cipher
        if not cipher:
            return ""

        # Initialize the matrix with placeholder characters
        matrix = [['\n' for _ in range(len(cipher))] for _ in range(key)]
        flag = False
        row, col = 0, 0

        # Mark the positions with '*'
        for _ in cipher:
            if row == 0 or row == key - 1:
                flag = not flag
            matrix[row][col] = '*'
            col += 1
            row += 1 if flag else -1

        # Fill the '*' positions with actual cipher characters
        index = 0
        for r in range(key):
            for c in range(len(cipher)):
                if matrix[r][c] == '*' and index < len(cipher):
                    matrix[r][c] = cipher[index]
                    index += 1

        # Read the matrix in zig-zag manner to get the decrypted text
        result = []
        flag = False
        row, col = 0, 0
        for _ in cipher:
            if row == 0 or row == key - 1:
                flag = not flag
            if matrix[row][col] != '\n':
                result.append(matrix[row][col])
            col += 1
            row += 1 if flag else -1

        # Remove any trailing 'X' characters used as fillers
        decrypted = ''.join(result).rstrip('X')
        return decrypted
    except Exception as e:
        print(f"Decryption Error: {e}")
        return None

def brute_force_rail_fence(cipher):
    """
    Attempts to decrypt the given ciphertext by trying all possible keys.
    
    Parameters:
    - cipher (str): The ciphertext to decrypt.
    
    Returns:
    - tuple: A tuple containing the decrypted text and the key used, if successful.
    """
    try:
        if not cipher:
            print("Cipher text is empty.")
            return None, None

        print("\nStarting Brute Force Decryption...\n")
        for key in range(1, len(cipher) + 1):
            decrypted = rail_fence_decrypt(cipher, key)
            if decrypted is None:
                continue
            print(f"Trying Key={key}: {decrypted}")
            while True:
                response = input(f"Is this the correct decryption? (Y/N): ").strip().lower()
                if response == 'y':
                    print(f"Success! Decrypted Text: {decrypted} | Key Used: {key}")
                    return decrypted, key
                elif response == 'n':
                    break
                else:
                    print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        print("Brute force attempt failed to find the correct key.")
        return None, None
    except Exception as e:
        print(f"Brute Force Error: {e}")
        return None, None

def main():
    """
    Main function to run the Rail Fence Cipher program with a user menu.
    """
    while True:
        print("\n=== Rail Fence Cipher ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Decrypt")
        print("4. Exit")
        
        choice = input("Select an option (1/2/3/4): ").strip()
        
        if choice == '1':
            # Encryption Option
            text = input("\nEnter the text to encrypt: ").strip()
            if not text:
                print("Error: Text cannot be empty.")
                continue
            try:
                key = int(input("Enter the key (positive integer): ").strip())
                if key <= 0:
                    print("Error: Key must be a positive integer.")
                    continue
                encrypted = rail_fence_encrypt(text, key)
                if encrypted:
                    print(f"\nEncrypted Text: {encrypted}")
            except ValueError:
                print("Error: Invalid key. Please enter a positive integer.")
        
        elif choice == '2':
            # Decryption Option
            cipher = input("\nEnter the cipher text to decrypt: ").strip()
            if not cipher:
                print("Error: Cipher text cannot be empty.")
                continue
            try:
                key = int(input("Enter the key (positive integer): ").strip())
                if key <= 0:
                    print("Error: Key must be a positive integer.")
                    continue
                decrypted = rail_fence_decrypt(cipher, key)
                if decrypted is not None:
                    print(f"\nDecrypted Text: {decrypted}")
            except ValueError:
                print("Error: Invalid key. Please enter a positive integer.")
        
        elif choice == '3':
            # Brute Force Decryption Option
            cipher = input("\nEnter the cipher text to brute force decrypt: ").strip()
            if not cipher:
                print("Error: Cipher text cannot be empty.")
                continue
            decrypted, key = brute_force_rail_fence(cipher)
            if decrypted:
                print(f"\nBrute Force Successful! Decrypted Text: {decrypted} | Key: {key}")
            else:
                print("\nBrute Force Failed to decrypt the text.")
        
        elif choice == '4':
            # Exit Option
            print("\nExiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
