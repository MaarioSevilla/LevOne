# -*- coding: utf-8 -*-
import random
import binascii
import math
import sympy
from sympy import mod_inverse

print("**** Tarea 5 **** \n\n")

##########################################################################################################

print("\n\n --- Selección de 2 números primos aleatorios de 1024 bits para Alice (pa, qa) y Bob (pb, qb). --- \n\n")

def getRandPrime(bitsLength):
    number = random.getrandbits(bitsLength)
    while not sympy.isprime(number):
        number = random.getrandbits(bitsLength)
    return number

# Alice
pa = getRandPrime(1024)
qa = getRandPrime(1024)
# Bob
pb = getRandPrime(1024)
qb = getRandPrime(1024)

print("\t Llave privada de Alice: (pa) {}".format(pa))
print("\t Llave privada de: (qa) {} \n".format(qa))
print("\t Llave privada de Bob: (pb) {}".format(pb))
print("\t Llave privada de: (qb) {}".format(qb))



##########################################################################################################

print("\n\n --- Cálculo de n=p*q para cada usuario (na y nb). --- \n\n")

# ALICE
na = pa * qa
# BOB
nb = pb * qb

print("\t Calculo de Alice (na): {} \n".format(na))
print("\t Calculo de Bob (nb): {}".format(nb))

##########################################################################################################

print("\n\n --- Cálculo de phi(n) para cada usuario (phi(na) y phi(nb)). --- \n\n")

# ALICE
phina = (pa-1) * (qa-1)
# BOB
phinb = (pb-1) * (qb-1)

print("\t Calculo de Alice phi(na): {} \n".format(phina))
print("\t Calculo de Bob phi(nb): {}".format(phinb))

##########################################################################################################

print("\n\n --- Generación de la llave e para cada usuario (ea y eb). --- \n\n")

ea = getRandPrime(1024)
while ea > phina:
    ea = getRandPrime(1024)

print("Valor de ea: {}".format(ea))
da=mod_inverse(ea,phina)

eb = getRandPrime(1024)
while eb > phina:
    eb = getRandPrime(1024)

print("Valor de eb: {}".format(eb))
db=mod_inverse(eb,phinb)

print("\t ea (ea): {} \n".format(ea))
print("\t da (da): {} \n".format(da))
print("\t ea (eb): {} \n".format(eb))
print("\t da (db): {} \n".format(db))

##########################################################################################################

print("\n\n --- Alice y Bob comparten su llave publica n, e --- \n\n")

print("\t Alice comparte su llave publica (ea): {} \n".format(ea))
print("\t Alice comparte su llave publica (na): {} \n".format(na))

print("\t Bob comparte su llave publica (eb): {} \n".format(ea))
print("\t Bob comparte su llave publica (nb): {} \n".format(na))

##########################################################################################################

print("\n\n --- Conversión de la cadena de texto de m a número entero --- \n\n")

message="hola"
m = int(binascii.hexlify(message.encode("utf-8")), 16)

print("\t Mensaje original: {}".format(message) )
print("\t Valor numérico: {}".format(m))

##########################################################################################################

print("\n\n --- Alice envía el mensaje cifrado de Alice --- \n\n")

c=pow(m,ea,na)

print("\t mensaje cifrado c (c): {} \n".format(c))


##########################################################################################################

print("\n\n --- Bob descifrado el mensaje de Alice  --- \n\n")

mrecovered = pow(c,da,na)

print("\t Mensaje recuperado (mrecovered): {} \n".format(mrecovered))

print("\n\n --- Bob convierte el mensaje a texto --- \n\n")

decrpyt =binascii.unhexlify(format(int(mrecovered), "x").encode("utf-8")).decode("utf-8")  # numero a texto

print("\t Mensaje en texto: (decrpyt) {}".format(decrpyt))

##########################################################################################################

print("\n\n --- Caso donde m > n --- \n\n")

message="Donec rutrum congue leo eget malesuada. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec sollicitudin molestie malesuada. Cras ultricies ligula sed magna dictum porta. Donec sollicitudin molestie malesuada. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Proin eget tortor risus. Nulla quis lorem ut libero malesuada feugiat. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Sed porttitor lectus nibh. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi."

m = int(binascii.hexlify(message.encode("utf-8")), 16)

print("\t Mensaje original: {}".format(message) )
print("\t Valor numérico: {}".format(m))

print( "\t Longitud de na: {}".format(na.bit_length()))
print( "\t Longitud de m: {}".format(m.bit_length()))

if (m.bit_length() > na.bit_length()):
    m_str = str(m)
    print("\t Longitud de m_str: {}".format(len(m_str)))
    m_str_length = int(math.ceil(float(m.bit_length())/float(na.bit_length())))
    print("Cantidad de submensajes: {}".format(m_str_length))
    m_fractions = list()
    for i in range(m_str_length):
        fraction = m_str[:m_str_length]
        m_str = m_str[m_str_length:]
        m_fractions.append( int(pow(  int(fraction), ea, na)))
    for i in m_fractions:
        print("Fragmento del mensaje encriptado: {}".format(i))
    ##########################################################################################################

    print("\n\n --- Bob descifrado el mensaje de Alice  --- \n\n")

    m_recovered_list = list()
    for c in m_fractions:
        fraction =  mod_inverse(pow(c, da), na)
        m_recovered_list.append(fraction)
    for i in m_recovered_list:
        print(i)
    mrecovered = ''.join(m_recovered_list)

    print("\t Mensaje recuperado (mrecovered): {} \n".format(mrecovered))

    print("\n\n --- Bob convierte el mensaje a texto --- \n\n")

    decrpyt =binascii.unhexlify(format(int(mrecovered), "x").encode("utf-8")).decode("utf-8")  # numero a texto

    print("\t Mensaje en texto: (decrpyt) {}".format(decrpyt))