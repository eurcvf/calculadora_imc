def separador():
  print('')
  print('-*' * 37)

nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
peso = float(input('Informe seu peso em (KG): '))
altura = float(input('Informe sua altura em (METROS): '))

imc = peso / (altura ** 2)
peso_ideal_m = 61.23 + ((altura - 1.60) * 53.54)
peso_ideal_f = 53.69 + ((altura - 1.52) * 53.54)

if nome and idade and peso and altura:
  if imc < 18.5:
    separador()
    print(f'\nVocê está abaixo do peso! \nSeu IMC é de {imc:.2f}\n\nPESO IDEAL:\nMasculino: {peso_ideal_m:.2f}\nFeminino: {peso_ideal_f:.2f}')
    separador()
  elif imc == 18.5 or imc <= 24.9:
    separador()
    print(f'\nVocê está no peso ideal! \nSeu IMC é de {imc:.2f}\n\nPESO IDEAL:\nMasculino: {peso_ideal_m:.2f}\nFeminino: {peso_ideal_f:.2f}')
    separador()
  elif imc >= 25 or imc <= 29.9:
    separador()
    print(f'\nVocê está acima do peso! \nSeu IMC é de {imc:.2f}\n\nPESO IDEAL:\nMasculino: {peso_ideal_m:.2f}\nFeminino: {peso_ideal_f:.2f}')
    separador()
  elif imc >= 30 or imc <= 34.9:
    separador()
    print(f'\nVocê está com obesidade de 1°! \nSeu IMC é de {imc:.2f}\n\nPESO IDEAL:\nMasculino: {peso_ideal_m:.2f}\nFeminino: {peso_ideal_f:.2f}')
    separador()
  elif imc >= 35 or imc <= 39.9:
    separador()
    print(f'\nVocê está com obesidade de 2°! \nSeu IMC é de {imc:.2f}\n\nPESO IDEAL:\nMasculino: {peso_ideal_m:.2f}\nFeminino: {peso_ideal_f:.2f}')
    separador()
  elif imc >= 40:
    separador()
    print(f'\nVocê está com obesidade de 3°! \nSeu IMC é de {imc:.2f}\n\nPESO IDEAL:\nMasculino: {peso_ideal_m:.2f}\nFeminino: {peso_ideal_f:.2f}')
    separador()
else:
  print('Preencha todos os campos!')
