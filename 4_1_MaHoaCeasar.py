# Cho k= STT , và Plaintext = TenCuaBan. Hãy mã hóa theo thuật toán Ceasar
def Ceasar(k,Plaintext):
    Ket_qua = ''
    for char in Plaintext:
        if char.isalpha():
            if char.isupper():
                Ket_qua += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            elif char.islower(): 
                Ket_qua += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            Ket_qua += char
    return Ket_qua

k = 19
Plaintext = 'DoVanVu'
    
print (Ceasar(k,Plaintext))