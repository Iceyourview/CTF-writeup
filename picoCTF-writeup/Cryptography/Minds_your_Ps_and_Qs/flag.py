c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021
n = 1280678415822214057864524798453297819181910621573945477544758171055968245116423923
e = 65537          

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a)*y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
p = 1899107986527483535344517113948531328331 
q = 674357869540600933870145899564746495319033
phi = (p - 1)*(q - 1)
d = modinv(e, phi)
plain = pow(c, d, n)
# print(plain)
# print(hex(plain))
print(bytearray.fromhex(hex(plain)[2:]).decode())

