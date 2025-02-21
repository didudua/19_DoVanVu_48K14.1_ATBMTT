# Trong thuật toán RSA, cho p=17, q=23, e=5. Thực hiện mã hóa thông điệp P=TenCuaBan.
def RSA(p,q,e,P):
    n = p * q
    z = (p-1) * (q-1)  
    d = pow(e, -1, z) 
    number_char = [ord(char) for char in P]
    return [pow(m, e, n) for m in number_char]

p = 17
q =23
e = 5
P = 'DoVanVu'

print(RSA(p,q,e,P))