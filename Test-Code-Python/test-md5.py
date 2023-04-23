import hashlib
nonce = "15691b47-a867-49a1-b2b8-23ed714197f5"
password = "hilary"
accessToken = "{B3571F3A-F532-400D-BE5B-8AEFDDD291EA}"
message = nonce + password + accessToken
md5 = hashlib.md5(message.encode())
print (md5.hexdigest())