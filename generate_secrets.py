import secrets

print("export SECRET_KEY='{}'".format(secrets.token_hex(32)))
print("export JWT_SECRET_KEY='{}'".format(secrets.token_hex(32)))
