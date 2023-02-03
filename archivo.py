# Import the PyCrypto library
from Crypto.Cipher import AES

# Encryption
# Define the encryption key
key = 'abcdabcdabcdabcd'

# Create an AES cipher object
cipher = AES.new(key)

# Encrypt the plaintext
encrypted_data = cipher.encrypt('My secret message')

# Decryption
# Create an AES cipher object
cipher = AES.new(key)

# Decrypt the encrypted data
decrypted_data = cipher.decrypt(encrypted_data)

# Output the original message
print(decrypted_data)
