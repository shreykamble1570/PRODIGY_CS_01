def caesar_cipher(text, shift, operation):
    # Perform Caesar Cipher encryption or decryption based on the operation
    result = ""  # Initialize an empty string to store the result

    for char in text:
        if char.isalpha():  # Check if the character is an alphabetic letter
            shift_base = 65 if char.isupper() else 97  # Determine ASCII base for case
            if operation == "encrypt":  # Encrypt the character
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif operation == "decrypt":  # Decrypt the character
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters are added as-is
    return result  # Return the final result

def main():
    # Main function to get user input and call Caesar Cipher operations
    print("Caesar Cipher Program")  # Print the program title

    text = input("Enter your message: ")  # Prompt user for the message
    shift = int(input("Enter shift value: "))  # Get the shift value from the user
    operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()  # Get the operation

    if operation in ["encrypt", "decrypt"]:  # Check if operation is valid
        result = caesar_cipher(text, shift, operation)  # Call the cipher function
        print(f"Result: {result}")  # Print the result
    else:
        print("Invalid operation. Please choose 'encrypt' or 'decrypt'.")  # Handle invalid operation input

if __name__ == "__main__":
    # Run the main function only when the script is executed directly
    main()
