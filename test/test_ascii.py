import binascii
asc_1 = '10'
#3位对齐补0
num_3 = asc_1.zfill(3)
#转换成16进制ascii码
asc= binascii.b2a_hex(num_3.encode('utf-8'))
print(asc.decode())