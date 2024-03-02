# Declaração das listas a serem utilizadas(Cadastros):
candidatos = []
eleitores = []
prefeitos = []
governadores = []
presidentes = []
jaVotou = []
jaVotouArrumado = []
votoNulo = []
votoBranco = []
ordemPref = []
ordemGov = []
ordemPres = []
brancoPref = []
brancoGov = []
brancoPres = []
nuloPref = []
nuloGov = []
nuloPres = []
  
# Criando a função que trará o Menu:

def menu():
    print("=-=" * 5, "MENU - SIMULADOR DE URNA" , "=-=" * 5) 
    print("\n - > O que deseja fazer?") # Apresentação das opções 
    print("\n • [1] - Cadastrar Candidatos") 
    print(" • [2] - Cadastrar Eleitores") 
    print(" • [3] - Votar")
    print(" • [4] - Apurar Resultados")
    print(" • [5] - Relatório e Estatísticas")
    print(" • [6] - Encerrar")
    

    opcao = str(input("\nEscolha uma opção: "))

    while opcao not in ("1", "2", "3", "4", "5", "6"): # Correção dos dados inseridos
        opcao = str(input("Valor inválido, digite novamente: "))
    return int(opcao)

def verificarResposta(resposta):
  if resposta == 1:
    return addCandidato()
  elif resposta == 2:
    return addEleitor()
  elif resposta == 3:
    return login()
  elif resposta == 4:
    return verificarResultados()
  elif resposta == 5:
    return showEstatisticas()
  elif resposta == 6:
    return acabar()
  else:
    return None

def addCandidato():
  nome = input("\nDigite o nome do candidato: ")
  while not nome.isalpha():
    nome = input("\nNome inválido. Digite o nome do candidato: ")
  partido = input("Digite o partido do candidato: ")
  while not partido.isalpha():
    partido = input("\nPartido inválido. Digite o partido do candidato: ")
  numero = input("Digite o número do candidato: ")
  while not numero.isnumeric(): 
    numero = input("\nNúmero inválido. Digite o número do candidato: ")
  cargo = input("Digite o cargo do candidato: ")
  while cargo.upper() not in ("PREFEITO", "GOVERNADOR", "PRESIDENTE"):
    cargo = str(input('Cargo inválido. Digite novamente [PRESIDENTE, PREFEITO ou GOVERNADOR]: '))
  candidato = {
    "partido": partido.upper(),
    "cargo": cargo.upper(),
    "nome": nome.upper(),
    "numero": numero.upper(),
    "votos": 0,
  }
  candidatos.append(candidato)
  if cargo.upper().strip() == "PREFEITO": # Separa os candidatos em cargos políticos
    prefeitos.append(candidato)
  elif cargo.upper().strip() == "GOVERNADOR":
    governadores.append(candidato)
  else:
    presidentes.append(candidato)
  
  print(f"\nCandidato {nome} adicionado!\n")
  respostaUser = str(input("Deseja continuar? [SIM ou NÃO]: "))
  while respostaUser.upper() not in ("SIM", "NÃO"):
    respostaUser = str(input("Valor inválido. Deseja continuar? [SIM ou NÃO]: "))
  if respostaUser.upper() == "SIM":
    return addCandidato()
  else:
    print("")
    return main()

def addEleitor():
  nome = input("\nDigite seu nome: ")
  while not nome.isalpha():
    nome = input("Nome inválido. Digite novamente: " )

  CPF = str(input("Digite seu CPF: ")).replace(".", "").replace("-", "")
  while not CPF.isnumeric():
    CPF = str(input("CPF inválido. Digite novamente: ")).replace(".", "").replace("-", "")

  for eleitor in eleitores:
    if eleitor["CPF"] == CPF:
      print("CPF já cadastrado. Digite novamente.")
      return main()

  eleitor = {
    "nome": nome,
    "CPF": CPF,
  }
  eleitores.append(eleitor)

  print(f"\nEleitor {nome} adicionado!")

  respostaUser = str(input("Deseja continuar? [SIM ou NÃO]: "))
  while respostaUser.upper() not in ("SIM", "NÃO"):
    respostaUser = str(input("Valor inválido. Deseja continuar? [SIM ou NÃO]: "))
  if respostaUser.upper() == "SIM":
    return addEleitor()
  elif respostaUser.upper() == "NÃO":
    return main()

def login():
  if len(eleitores) == 0:
    print("Desculpe, mas não há eleitores disponíveis.\n")
    return main()
  elif len(eleitores) == len(jaVotou):
    print("Todos os eleitores disponíveis já votaram.\n")
    return main()
  
  global CPF
  
  CPF = input('Digite seu CPF:').strip().replace(".", "").replace("-", "")  # Login do Eleitor
  for i in range (0, len(eleitores)):
    if eleitores[i]['CPF'] == CPF:
      print('Certo, CPF encontrado!')
      return votarPrefeito()
    elif CPF in jaVotou:
      print('O CPF cadastrado já votou.')
      return main()
  print('CPF não encontrado.')
  return login()


def votarPrefeito():
  voto = input("\nEm quem você irá votar para prefeito? [-1 para branco e -2 para nulo]: ").strip() # Voto para prefeito
  if voto == "-1":
    confirmacao = input("Você tem certeza de que quer votar branco? [SIM ou NÃO]: ").upper().strip()
    while confirmacao not in ("SIM","NÃO"):
      confirmacao = input("Resposta inválida. Você tem certeza de que quer votar branco? [SIM ou NÃO]: ").upper().strip()
    match confirmacao:
      case "SIM":
        for eleitor in eleitores:
          brancoPref.append(0)
          votoBranco.append(eleitor)
        return votarGovernador()
      case "NÃO":
        return votarPrefeito()
  elif voto == "-2":
    confirmacao1 = input("Você tem certeza de que quer votar nulo? [SIM ou NÃO]: ").upper().strip()
    while confirmacao1 not in ("SIM","NÃO"):
      confirmacao1 = input("Resposta inválida. Você tem certeza de que quer votar nulo? [SIM ou NÃO]: ").upper().strip()
    match confirmacao1:
      case "SIM":
        for eleitor in eleitores:
          nuloPref.append(0)
          votoNulo.append(eleitor)
        votarGovernador()
      case "NÃO":
        return votarPrefeito()
  for candidato in prefeitos:
    if voto == candidato["numero"]: # Mostra o candidato
      print("Nome:" , candidato["nome"])
      print("Partido:", candidato["partido"])
      opcao = str(input(f"Você tem certeza que quer votar em {candidato['nome']} para {candidato['cargo']}? [SIM ou NÃO]: ")).upper().strip() # Confirmação do voto
      while opcao not in ("SIM", "NÃO"):
        opcao = str(input('Resposta inválida. Digite novamente [SIM ou NÃO]: ')).upper()
      match opcao:
        case "NÃO":
          return votarPrefeito()  
        case "SIM": # Contagem dos Votos
          print("Certo! Contando voto...")
          candidato["votos"] += 1
          return votarGovernador()
        case _:
          return None

def votarGovernador():
  voto = input("\nEm quem você irá votar para governador?: ").strip() # Voto para governador
  if voto == "-1":
    confirmacao = input("Você tem certeza de que quer votar branco? [SIM ou NÃO]: ").upper().strip() # Voto branco
    while confirmacao not in ("SIM","NÃO"):
      confirmacao = input("Resposta inválida. Você tem certeza de que quer votar branco? [SIM ou NÃO]: ").upper().strip()
    match confirmacao:
      case "SIM":
        for eleitor in eleitores:
          brancoGov.append(0)
          votoBranco.append(eleitor)
        return votarPresidente()
      case "NÃO":
        return votarGovernador()
  elif voto == "-2":
    confirmacao1 = input("Você tem certeza de que quer votar nulo? [SIM ou NÃO]: ").upper().strip() # Voto nulo
    while confirmacao1 not in ("SIM","NÃO"):
      confirmacao1 = input("Resposta inválida. Você tem certeza de que quer votar nulo? [SIM ou NÃO]: ").upper().strip()
    match confirmacao1:
      case "SIM":
        for eleitor in eleitores:
          nuloGov.append(0)
          votoNulo.append(eleitor)
        return votarPresidente()
      case "NÃO":
        return votarGovernador()
  for candidato in governadores:
    if voto == candidato["numero"]: # Mostra o candidato
      print("Nome:" , candidato["nome"])
      print("Partido:", candidato["partido"])
      opcao = str(input(f"Você tem certeza que quer votar em {candidato['nome']} para {candidato['cargo']}? [SIM ou NÃO]: ")).upper().strip() # Confirmação do voto
      while opcao not in ("SIM", "NÃO"):
        opcao = str(input('Resposta inválida. Digite novamente [SIM ou NÃO]: ')).upper().strip()
      match opcao:
        case "NÃO":
          return votarGovernador()  
        case "SIM": # Contagem do Voto
          print("Certo! Contando voto...")
          candidato["votos"] += 1
          return votarPresidente()
        case _:
          return None
          
def votarPresidente():
  voto = input("\nEm quem você irá votar para presidente?: ").strip() # Voto para presidente

  if voto == "-1":
    confirmacao = input("Você tem certeza de que quer votar branco? [SIM ou NÃO]: ").upper().strip() # Voto branco
    while confirmacao not in ("SIM","NÃO"):
      confirmacao = input("Resposta inválida. Você tem certeza de que quer votar branco? [SIM ou NÃO]: ").upper().strip()
    match confirmacao:
      case "SIM":
        for eleitor in eleitores:
            if CPF == eleitor["CPF"]:
              brancoPres.append(0)
              votoBranco.append(eleitor)
              jaVotou.append(eleitor)
        return main()
      case "NÃO":
        return votarPresidente()
  elif voto == "-2":
    confirmacao1 = input("Você tem certeza de que quer votar nulo? [SIM ou NÃO]: ").upper().strip() # Voto nulo
    while confirmacao1 not in ("SIM","NÃO"):
      confirmacao1 = input("Resposta inválida. Você tem certeza de que quer votar nulo? [SIM ou NÃO]: ").upper().strip()
    match confirmacao1:
      case "SIM":
        for eleitor in eleitores:
            if CPF == eleitor["CPF"]:
              nuloPres.append(0)
              votoNulo.append(eleitor)
              jaVotou.append(eleitor)
        return main()
      case "NÃO":
        return votarPresidente()
  for candidato in presidentes:
    if voto == candidato["numero"]: # Mostra o candidato
      print("Nome:" , candidato["nome"])
      print("Partido:", candidato["partido"])
      opcao = str(input(f"Você tem certeza que quer votar em {candidato['nome']} para {candidato['cargo']}? [SIM ou NÃO]")).upper().strip() # Confirmação do voto
      while opcao not in ("SIM", "NÃO"):
        opcao = str(input('Resposta inválida. Digite novamente [SIM ou NÃO]: '))
      match opcao:
        case "NÃO":
          return votarPresidente()  
        case "SIM": # Contagem do Voto
          print("Certo! Contando voto...")
          for eleitor in eleitores:
            if CPF == eleitor["CPF"]:
              jaVotou.append(eleitor)
          candidato["votos"] += 1
          return main()
        case _:
          return None
          
def verificarResultados():
  
  rankingPref = sorted(prefeitos, key  = lambda x: x["votos"], reverse = True)
  totalVotosPref = sum(candidato["votos"] for candidato in prefeitos)
  
  print("\nRESULTADO PARA PREFEITO\n")
  for i in range (0, len(rankingPref)): # Ranking de Prefeito
    print(f"{i+1}º mais votado: \n")
    print("nome:", prefeitos[i]["nome"])
    print("Partido:", prefeitos[i]["partido"])
    print("Total de Votos Válidos:", prefeitos[i]["votos"], f"{(prefeitos[i]['votos']/totalVotosPref) * 100: .2f}%") 
    print()

  print(f"Total de votos: {totalVotosPref + len(brancoPref) + len(nuloPref)}") # Outras informações
  print(f"Total de votos brancos: {len(brancoPref)} ({len(brancoPref) / (totalVotosPref + len(brancoPref) + len(nuloPref)) * 100}", "%)")
  print(f"Total de votos nulos: {len(nuloPref)} ({len(nuloPref) / (totalVotosPref + len(brancoPref) + len(nuloPref)) * 100}", "%)")

  
  rankingGov = sorted(governadores, key = lambda x: x["votos"], reverse = True)
  totalVotosGov = sum(candidato["votos"] for candidato in governadores)

  print("\nRESULTADO PARA GOVERNADOR\n")
  for i in range (0, len(rankingGov)): # Ranking de Governador
    print(f"{i+1}º mais votado: ")
    print("nome:", governadores[i]["nome"])
    print("Partido:", governadores[i]["partido"])
    print("Votos:", governadores[i]["votos"])
    print(f"Votos válidos: {(governadores[i]['votos']/totalVotosGov) * 100: .2f}%")
    print()

  print(f"Total de votos: {totalVotosGov + len(brancoGov) + len(nuloGov)}") # Outras informações
  print(f"Total de votos brancos: {len(brancoGov)} ({len(brancoGov) / (totalVotosGov + len(brancoGov) + len(nuloGov)) * 100}", "%)")
  print(f"Total de votos nulos: {len(nuloGov)} ({len(nuloGov) / (totalVotosGov + len(brancoGov) + len(nuloGov)) * 100}", "%)")
  

  rankingPres = sorted(presidentes, key = lambda x: x["votos"], reverse = True)
  totalVotosPres = sum(candidato["votos"] for candidato in presidentes)
  print("\nRESULTADO PARA PRESIDENTE\n") 
  for i in range (0, len(rankingPres)): # Ranking de Presidente
    print(f"{i+1}º mais votado: \n")
    print("nome:", presidentes[i]["nome"])
    print("Partido:", presidentes[i]["partido"])
    print("Votos:", presidentes[i]["votos"])
    print(f"Votos válidos: {(presidentes[i]['votos']/totalVotosPres) * 100: .2f}%")
    print()

  print(f"Total de votos: {totalVotosPres + len(brancoPres) + len(nuloPres)}") # Outras informações
  print(f"Total de votos brancos: {len(brancoPres)} ({len(brancoPres) / (totalVotosPres + len(brancoPres) + len(nuloPres)) * 100}", "%)")
  print(f"Total de votos nulos: {len(nuloPres)} ({len(nuloPres) / (totalVotosPres + len(brancoPres) + len(nuloPres)) * 100}", "%)")
    
  return main()
  
def showEstatisticas():

  for elemento in jaVotou:
    if elemento not in jaVotouArrumado:
      jaVotouArrumado.append(elemento)
  print("Eleitores que votaram: ", end = ' ')
  for i in jaVotouArrumado:
    print(f"{i['nome']}", end = ' ')
  print(f"\nTotal de votos: {len(jaVotouArrumado)}")
  print(f"Quantidade de eleitores: {len(eleitores)}")

  contagemVotos = {} # Contagem de votos por partido
  partidoMaisVotos = None
  partidoMenosVotos = None
  maxVotos = 0
  minVotos = float('inf')
  
  for i in range (0, len(candidatos)):
    partido = candidatos[i]['partido']
    if partido in contagemVotos:
      contagemVotos[partido] += 1
    else:
      contagemVotos[partido] = 1
  for partido, votos in contagemVotos.items():
    if votos > maxVotos:
      maxVotos = votos
      partidoMaisVotos = partido
    if votos < minVotos:
      minVotos = votos
      partidoMenosVotos = partido

  print(f"O partido que mais elegeu políticos foi: {partidoMaisVotos}")
  print(f"O partido que menos elegeu políticos foi: {partidoMenosVotos}\n")
  return main()

def acabar():
  return "\nPrograma Encerrado."
  
def main():
  opcao = menu()
  verificarResposta(opcao)
  
main()