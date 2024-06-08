def cipher(text: str, shift: int) -> str:
    """Encrypts or decrypts a text using the 'Veni-Vidi-Vici' algorithm."""
    encrypted: str = ""
    for char in text:
        if char.isalpha():  # Check if it's a letter
            base: int = ord('a') if char.islower() else ord('A')  # Get ASCII base
            shifted: int = (ord(char) - base - shift) % 26  # Calculate shifted position
            encrypted += chr(base + shifted)
        else:
            encrypted += char  # If it isn't a letter, do nothing
    return encrypted

