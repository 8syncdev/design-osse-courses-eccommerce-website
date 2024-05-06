PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher", #* * PBKDF2PasswordHasher is a secure hashing algorithm.
    "django.contrib.auth.hashers.ScryptPasswordHasher", #* * ScryptPasswordHasher is a secure hashing algorithm.
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher", #* * BCryptSHA256PasswordHasher is a secure hashing algorithm.
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher", #* * PBKDF2SHA1PasswordHasher is a secure hashing algorithm.
    "django.contrib.auth.hashers.Argon2PasswordHasher", #* * Argon2PasswordHasher is a secure hashing algorithm.
    #* "django.contrib.auth.hashers.SHA1PasswordHasher", #* * SHA1PasswordHasher is a security risk, because it is not a secure hashing algorithm.
    #* "django.contrib.auth.hashers.MD5PasswordHasher", #* * MD5PasswordHasher is a security risk, because it is not a secure hashing algorithm.
    #* "django.contrib.auth.hashers.CryptPasswordHasher", #* * CryptPasswordHasher is a security risk, because it is not a secure hashing algorithm.
]