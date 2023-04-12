from Crypto.Util.number import getPrime
p = getPrime(1024)
q = getPrime(1024)
keys = gen_keys(p, q)
msg = 'Hello, world!'
test_encrypt_decrypt(msg, keys)
