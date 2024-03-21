#---------- Início das Variáveis Globais ----------
lista_colaboradores = []
codigo_colaborador = 0
#---------- Fim das Variáveis Globais ----------

#---------- Início de cadastrar_colaborador() ----------
def cadastrar_colaborador(codigo):
  print('\n'+20*'-'+' | Bem-vindo ao menu de Cadastrar Colaboradores | '+20*'-'+'\n')
  print('Código do colaborador: {}'.format(codigo))
  nome = input('Digite o NOME do colaborador: ')
  setor = input('Digite o SETOR do colaborador: ')
  salario = int(input('Digite o SALÁRIO (R$) do colaborador: R$ '))
  dicionario_colaborador = {'codigo'  : codigo,
                            'nome'    : nome,
                            'setor'   : setor,
                            'salario' : salario}
  lista_colaboradores.append(dicionario_colaborador.copy())
#---------- Fim de cadastrar_colaborador() ----------

#---------- Início de consultar_colaborador() ----------
def consultar_colaborador():
  print(22*'-'+'| Bem-vindo ao menu de Consultar Colaboradores | '+ 22*'-')
  while True:
   opcao_consultar=input('\nEscolha a opção desejada:\n'+
                        '1-Consultar TODOS os Colaboradores\n'+
                        '2-Consultar Colaborar(es) por CÓDIGO\n'+
                        '3-Consultar Colaborador por SETOR\n'+
                        '4-Retornar ao menu\n'+
                        '>>')
   if opcao_consultar == '1':
     print('\n'+'- Você escolheu a opção Consultar TODOS  os Colaboradores')
     for colaborador in lista_colaboradores: # colaborador vai varrer toda a lista de colaboradores
         print(40*'-')
         for key, value in colaborador.items(): # varrer todos os conjuntos chaves e valor do dicionario colaborador
          print('{} : {}'.format(key,value))
     print(40*'-')

   elif opcao_consultar == '2':
      print('\n'+'- Você escolheu a opção Consultar Colaborador(es) por CÓDIGO')
      valor_desejado = int(input('Digite o CÓDIGO do colaborador: '))
      for colaborador in lista_colaboradores:
       if colaborador['codigo'] == valor_desejado: # o valor do campo código desse dicionário é igual o valor desejado
         print(40*'-')
         for key, value in colaborador.items(): # varrer todos os conjuntos chaves e valor do dicionario colaborador
           print('{} : {}' .format(key,value))
      print(40*'-')

   elif opcao_consultar == '3':
      print('\n'+'- Você escolheu a opção Consultar Colaborador por SETOR')
      valor_desejado = input('Digite o SETOR do colaborador: ')
      for colaborador in lista_colaboradores:
       if colaborador['setor'] == valor_desejado: # o valor do campo código desse dicionário é igual o valor desejado
         print(40*'-')
         for key, value in colaborador.items(): # varrer todos os conjuntos chaves e valor do dicionario colaborador
          print('{} : {}'.format(key,value))
      print(40*'-')
   elif opcao_consultar == '4':
     return #Sai da função consultar e volta para o menu
   else:
    print('Opção Inválida. Tente novamente')
    continue # Volta ao inicio do laço
#---------- Fim de consultar_colaborador() ----------

#---------- Início de remover_colaborador() ----------
def remover_colaborador():
  print(20*'-'+' | Bem-vindo ao menu de Remover Colaboradores | '+20*'-')
  valor_desejado = int(input('Digite o CÓDIGO do colaborador que deseja remover: '))
  for colaborador in lista_colaboradores:
    if colaborador['codigo'] == valor_desejado:
     lista_colaboradores.remove(colaborador)
     print('Colaborador Removido')
 #---------- Fim de remover_colaborador() ----------

#---------- Início de Main ----------
print(10*'-','Bem-vindo ao Controle de Colaboradores da Francielli Fagundes de Souza',10*'-')
while True:
  print('\n'+35*'-'+' | Menu Principal | '+35*'-')
  opcao_principal=input('\n'+
                        'Escolha a opção desejada:\n'+
                        '1-Cadastrar Colaborador\n'+
                        '2-Consultar Colaborar(es)\n'+
                        '3-Remover Colaborador\n'+
                        '4-Sair\n'+
                        '>>')
  if opcao_principal == '1':
    codigo_colaborador = codigo_colaborador + 1
    cadastrar_colaborador(codigo_colaborador)
  elif opcao_principal == '2':
    consultar_colaborador()
  elif opcao_principal == '3':
    remover_colaborador()
  elif opcao_principal == '4':
    break # Encerra o laço principal e o programa acaba
  else:
    print('Opção Inválida. Tente novamente')
    continue # Volta ao inicio do laço
#---------- Fim de Main ----------
