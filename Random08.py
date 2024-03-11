#Exercise 8: Generate random secure token of 64 bytes and random URL

# 1) Random secure token of 64 bytes
import secrets
token = secrets.randbits(64)
print(token)

# 2) Generate secure URL
demo_url = "www.demorurl.com/"
secure_url = demo_url + str(token)
print(secure_url)
