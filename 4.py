letra = input('Digite uma letra do alfabeto: ').lower()
vogal = ['a', 'e', 'i', 'o', 'u']

if letra in vogal:
    print(f'A letra {letra} é uma vogal.')
elif len(letra) >= 2:
    print('Digite apenas uma letra.')
else:
    print(f'A letra {letra} é uma consoante.')