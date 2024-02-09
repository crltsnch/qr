import base64

data = "U0c5c1lTQnRkVzVrYndvPQo="
def decode(data):
    try:
        decoded = base64.b64decode(data, altchars=None, validate=False)
        return decode(decoded)
    except:
        return data
    return decoded

resultado = decode(data)
print(resultado)
