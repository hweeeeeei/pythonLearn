# Base64是一种用64个字符来表示任意二进制数据的方法。
import base64

print(base64.b64encode(b'binary\x00string'))

print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))

# url safe的base64编码，把字符+和/分别变成-和_：
print('url safe', base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))

# Base64是一种通过查表的编码方法，不能用于加密
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
