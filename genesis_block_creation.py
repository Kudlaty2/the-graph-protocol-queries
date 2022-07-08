from Crypto.Hash import SHA256

hash_object = SHA256.new(data=(str(0) + "0" + str(1465154705) + "Genesis block!!").encode()).hexdigest()
print(hash_object)
