import chilkat
import hashlib
# This example requires the Chilkat API to have been previously unlocked.
crypt = chilkat.CkCrypt2()
s = "GeeksForGeeks"
crypt.put_HashAlgorithm("sha1")
crypt.put_EncodingMode("hex")
# Other possible EncodingMode settings are:
hash = crypt.hashStringENC(s)
print("SHA1: " + hash)

# Hash using MD2
crypt.put_HashAlgorithm("md2")
hash = crypt.hashStringENC(s)
print("MD2: " + hash)

# Hash using MD5
crypt.put_HashAlgorithm("md5")
hash = crypt.hashStringENC(s)
print("MD5: " + hash)

# Note: SHA-2 is a set of cryptographic hash functions (SHA-224, SHA-256, SHA-384, SHA-512)

# Hash using SHA-256
crypt.put_HashAlgorithm("sha256")
hash = crypt.hashStringENC(s)
print("SHA256: " + hash)

# Hash using SHA-384
crypt.put_HashAlgorithm("sha384")
hash = crypt.hashStringENC(s)
print("SHA384: " + hash)

# Hash using SHA-512
crypt.put_HashAlgorithm("sha512")
hash = crypt.hashStringENC(s)
print("SHA512: " + hash)

# Hash using HAVAL
# There are two additional properties relevant to HAVAL:
# HavalRounds, and KeyLength.
# HavalRounds can have values of 3, 4, or 5.
# KeyLength can have values of 128, 160, 192, 224, or 256
# initializing string
str = "GeeksForGeeks"

# encoding GeeksforGeeks using encode()
# then sending to SHA224()
result = hashlib.sha224(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())

print("\r")









