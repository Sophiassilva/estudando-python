conj = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 
         'dezoito', 'dezenove', 'vinte')

num = -1
while num < 0 or num > 20:
    num = int(input('Digite um número de 0 a 20: '))
print(f'Você digitou o número {conj[num]}.')
