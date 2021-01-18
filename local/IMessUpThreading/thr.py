import base64
a = "😀"
x = ord(a)
print(len(a))





m = ord('Sagar')
print(type(a))
print(a)
b_en = base64.b64encode(a.encode("utf-8"))
print(b_en)
b_dec = base64.b64decode(b_en)
print(b_dec)
print(b_dec.decode("utf-8"))