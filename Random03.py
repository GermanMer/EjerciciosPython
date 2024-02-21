#Exercise 3: Generate 6 digit random secure OTP

import secrets

#Getting systemRandom class instance out of secrets module
secretsGenerator = secrets.SystemRandom()

random_secure_OTP = secretsGenerator.randrange(100000, 999999)

print(random_secure_OTP)
