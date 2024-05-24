from Crypto.Util import number
from math import gcd as bltin_gcd

def hexPrint(val):
   return str(hex(val))[2:].upper()

e_professor = int('2E76A0094D4CEE0AC516CA162973C895', 16)
N_professor = int('1985008F25A025097712D26B5A322982B6EBAFA5826B6EDA3B91F78B7BD63981382581218D33A9983E4E14D4B26113AA2A83BBCCFDE24310AEE3362B6100D06CC1EA429018A0FF3614C077F59DE55AADF449AF01E42ED6545127DC1A97954B89729249C6060BA4BD3A59490839072929C0304B2D7CBBA368AEBC4878A6F0DA3FE58CECDA638A506C723BDCBAB8C355F83C0839BF1457A3B6B89307D672BBF530C93F022E693116FE4A5703A665C6010B5192F6D1FAB64B5795876B2164C86ABD7650AEDAF5B6AFCAC0438437BB3BDF5399D80F8D9963B5414EAFBFA1AA2DD0D24988ACECA8D50047E5A78082295A987369A67D3E54FFB7996CBE2C5EAD794391', 16)

n_length = 1024

# 2 primos aleatorios
#p = number.getPrime(n_length) 
#q = number.getPrime(n_length) 
p = 92392736051404410760489211138928933084669142998113543808554897627750570982116408258371998695213555237792397733512856385994918816918636640713870525296026613920083515907015615429890827328183359151438284540091182946989292605495678930433105724422398902024307550415183491566255289753386220625618362623001389119187
q = 137406368247632677945311369058109307236482989410461182032063774518640481878456792323974011119473612130724019393467401749836208406613788893164893361085919637031221752813994486285238514963123326738206678556176402892018710905234658833475432118894544955465633191531566947144539267520653729422507479354428458273103

N_a = p * q 
L = (p-1) * (q-1) # euler

# achar um E que seja primo relativo de L
e_a = None
e_a = int('E6A45B1F1BFBD3DCD7CBD688D78BB47F', 16)
while (not e_a): 
  val = number.getRandomNBitInteger(128)
  if bltin_gcd(val, L) == 1: # algoritmo euclidiano de achar Greatest Common Divisor
     e_a = val
     break

# calcular um inverso de E em Z_L
d_a = pow(e_a, -1, L) # pode estar errado https://stackoverflow.com/questions/48839772/why-is-time-complexity-o1-for-powx-y-while-it-is-on-for-xy

# minha chave publica
PK_a = (e_a, N_a)
print("e_a = ", hexPrint(PK_a[0]))
print("d_a = ", hexPrint(d_a))
print("\nN_a = ", hexPrint(PK_a[1]))

#### Chaves simetricas
#s = number.getRandomNBitInteger(128) # valor aleatorio de 128 bits
#x = (s ** e_professor) % N_professor # cifrar a chave c/ a chave do professor  # pode estar errado https://stackoverflow.com/questions/48839772/why-is-time-complexity-o1-for-powx-y-while-it-is-on-for-xy
#sig_x = (x ** d_a) % N_a             # assinar mensagem com minha chave privada

s = int('E621977578D75D3992C9A0B988A42F24', 16)
x = pow(s, e_professor, N_professor)
sig_x = pow(x, d_a, N_a)


print("\ns = ", hexPrint(s))
print("\nx = ", hexPrint(x))
print("\nsig_x = ", hexPrint(sig_x))