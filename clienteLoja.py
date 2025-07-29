#Você irá criar um programa para ajudar a registrar as compras de clientes em uma loja
#O programa deve permitir que o usuário cadastre vários clientes, informando:
#• O nome do cliente
#• O valor total gasto pelo cliente (em reais)
#O programa deve validar se o valor gasto é um número inteiro válido. A cada cliente
#cadastrado, o programa deve guardar:
#• A soma total dos valores gastos.
#• O nome do cliente que mais gastou na loja.
#O cadastro deve continuar até o usuário optar por parar.

totalCaixa = 0
clienteMaisComprou = ''
clienteMaisComprou_Valor = 0
valorGasto = 0
while True:
  nomeCliente = input('Digite o nome do clinte: ')
  valorGasto_str = input('Digite o valor que o clinte gastou: ')
  if valorGasto_str.isdigit():
    valorGasto = int(valorGasto_str)
  else:
    print('Digito invalido')

  totalCaixa = totalCaixa + valorGasto

  if valorGasto > clienteMaisComprou_Valor:
    clienteMaisComprou_Valor = valorGasto
    clienteMaisComprou = nomeCliente
  
  continuar = input('Deseja cadastrar outro compra ?(S/N)').strip().upper()
  if continuar == 'S':
    continue
  elif continuar == 'N':
    print('******************DADOS CADASTRADOS***********************')
    print('-                                                          -')
    print(f'O total do caixa da loja hoje foi de: R${totalCaixa}')  
    print(f'O cliente que mais comprou foi o {clienteMaisComprou}que gastou R${clienteMaisComprou_Valor}')
    print('-                                                          -')
    print('*******************************************************************************************************')
    break
  else:
    print('Digito invalido')
  

