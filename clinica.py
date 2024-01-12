from datetime import datetime

lista_pacientes = [] #lista vazia de pacientes
lista_consultas = [] #lista vazia de consultas marcadas
id_global = 0 #variável inicial de id definida como 0
id_consulta = 0

#função de cadastro de colaboradores
def cadastrar_paciente(id):

  print('------------------MENU CADASTRAR PACIENTE---------------------')
  nome = str(input('Nome completo do paciente: '))

  while True:
        telefone = input('Número de telefone (apenas 11 dígitos): ')
        if telefone.isdigit() and len(telefone) == 11:
            break
        else:
            print('Número inválido! Digite novamente')

 # verificação para o número de telefone/paciente ja cadastrado
  if any(paciente['telefone'] == telefone for paciente in lista_pacientes):
      print('Paciente já cadastrado! Tente novamente.')
      return
  else:
      print('Paciente cadastrado com sucesso!')


  paciente = { #dicionário para inserir os pacientes
      'id': id_global,
      'nome': nome,
      'telefone': telefone,
      }
  lista_pacientes.append(paciente.copy()) #adicionando o dicionário na lista

def marcar_consulta(id):

  print('------------------Pacientes Cadastrados---------------------')
  for pacientes in lista_pacientes: #for que mostra toda a lista/dicionário de pacientes

    for key, value in pacientes.items(): #for para mostrar todos os pacientes com chave e valores
      print(f'{key}: {value}')
  print('--------------------------')

  while True:
      print('------------------MENU MARCAÇÃO DE CONSULTAS---------------------------')
      print('Digite o id do paciente ao qual deseja marcar uma consulta:')
      consulta = int(input('>>'))

      # encontrar o paciente na lista de pacientes
      paciente_encontrado = None
      for paciente in lista_pacientes:
          if paciente['id'] == consulta:
              paciente_encontrado = paciente
              break

      if paciente_encontrado:
          print('Agora escolha a especialidade: \n 1- Clínica Geral\n2- Pediatria\n3- Ginecologia\n4- Odontologia\n')
          especialidade = int(input('>>'))

          if especialidade not in [1, 2, 3, 4]:
              print('Especialidade não encontrada. Tente novamente')
              return

          if especialidade == 1:
              especialista = 'Clínico Geral'
          elif especialidade == 2:
              especialista = 'Pediatra'
          elif especialidade == 3:
              especialista = 'Ginecologista'
          elif especialidade == 4:
              especialista = 'Dentista'

          # continua o agendamento
          try:
              # Tenta converter a string para um objeto datetime usando strptime
              input_data = input("Digite a data e hora da consulta (Exemplo: 01/01/2024 10:10): ")
              data_agendamento = datetime.strptime(input_data, "%d/%m/%Y %H:%M")
          except ValueError:
              print("Formato de data/hora inválido. Tente novamente.")
              continue

          #obter a data e hora atuais
          data_atual_formatada = datetime.now().strftime("%d/%m/%Y %H:%M")

          #conversao de string
          data_atual = datetime.strptime(data_atual_formatada, "%d/%m/%Y %H:%M")

          if data_agendamento <= data_atual:
              print("A consulta não pode ser agendada para uma data retroativa. Tente novamente.")
              return
          elif any(
                consulta['especialista'] == especialista and
                consulta['data_agendamento'] == data_agendamento
                for consulta in lista_consultas
            ):
                print("Já existe uma consulta marcada com a mesma especialidade, data e horário. Escolha novamente")
                return
          else:
              print("Consulta agendada para:", data_agendamento.strftime("%d/%m/%Y %H:%M"))


          agendamento = {
              'id_consulta': id_consulta,
              'paciente': paciente_encontrado['nome'],
              'especialista': especialista,
              'data_agendamento': data_agendamento
          }

          lista_consultas.append(agendamento.copy())
          return
      else:
          print('Paciente não encontrado. Tente novamente')
          return

def remover_consulta():
    print('---------------MENU DE CANCELAMENTO DE CONSULTA---------------------')
    for consulta in lista_consultas:
        for key, value in consulta.items():
            print(f'{key}: {value}')
        print('--------------------------')

    consulta_cancel = int(input('Digite o id da consulta a ser cancelada: '))

    # indicar se a consulta foi encontrada e removida
    encontrada = False

    for consulta in lista_consultas:
        if consulta['id_consulta'] == consulta_cancel:
          print(f"Você deseja cancelar a consulta com ID {consulta_cancel}? (s/n)")
          resposta = input().lower()
          if resposta == 's':
              lista_consultas.remove(consulta)
              print(f"A Consulta de ID {consulta_cancel} foi cancelada.")
              encontrada = True
              break
          else:
              print(f"A consulta de ID {consulta_cancel} continua marcada.")
              encontrada = True
              break

    if not encontrada:
        print('Consulta não encontrada.')



#PROGRAMA PRINCIPAL
print('Bem-vindo(a) ao Sistema da Clínica de Consultas')
while True:
  print('*' * 75)
  print('--------------------------MENU PRINCIPAL-----------------------------------')
  print('Escolha a opção desejada:\n1- Cadastrar paciente\n2- Marcar consultas\n3- Cancelar consulta\n4- Sair')
  menu = input('>>')

  #condições para redirecionar cada caso para as funções
  if menu == '1':
    id_global += 1
    cadastrar_paciente(id_global)
  elif menu == '2':
    id_consulta +=1
    marcar_consulta(id_consulta)
  elif menu =='3':
    remover_consulta() #chama a função de remover
  elif menu == '4':
    print('Programa encerrado.')
    break #encerra o programa
  else:
    print('Opção inválida.')
    continue #volta para o início do laço