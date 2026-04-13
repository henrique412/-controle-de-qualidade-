import os

# Configurações do Sistema
LIMITE_CAIXA = 10
REQUISITOS = {
    "peso_min": 95,
    "peso_max": 105,
    "cores_validas": ["azul", "verde"],
    "comprimento_min": 10,
    "comprimento_max": 20
}

# Banco de Dados em Memória
peças_aprovadas = []
peças_reprovadas = []
caixas_fechadas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    0
    
#avaliar peça 

def avaliar_peça(peça):
    motivos = []
    
    if not (REQUISITOS["peso_min"] <= peça['peso'] <= REQUISITOS["peso_max"]):
        motivos.append(f"Peso fora da faixa ({peça['peso']}g)")
    
    if peça['cor'].lower() not in REQUISITOS["cores_validas"]:
        motivos.append(f"Cor inválida ({peça['cor']})")
        
    if not (REQUISITOS["comprimento_min"] <= peça['comprimento'] <= REQUISITOS["comprimento_max"]):
        motivos.append(f"Comprimento fora da faixa ({peça['comprimento']}cm)")
    
    return motivos

#cadastrar peças 

def cadastrar_peça():
    print("--- Cadastro de Peça ---")
    try:
        id_peça = input("ID da Peça: ")
        peso = float(input("Peso (g): "))
        cor = input("Cor: ").strip().lower()
        comprimento = float(input("Comprimento (cm): "))
        
        peça = {"id": id_peça, "peso": peso, "cor": cor, "comprimento": comprimento}
        erros = avaliar_peça(peça)
        
        if not erros:
            peças_aprovadas.append(peça)
            print(f"\n✅ Peça {id_peça} APROVADA!")
            
            # Lógica de empacotamento
            if len(peças_aprovadas) % LIMITE_CAIXA == 0:
                inicio = len(peças_aprovadas) - LIMITE_CAIXA
                caixa = peças_aprovadas[inicio:]
                caixas_fechadas.append(caixa)
                print(f"📦 CAIXA FECHADA! (Total de caixas: {len(caixas_fechadas)})")
        else:
            peça['motivo'] = ", ".join(erros)
            peças_reprovadas.append(peça)
            print(f"\n❌ Peça {id_peça} REPROVADA. Motivos: {peça['motivo']}")
            
    except ValueError:
        print("\n⚠️ Erro: Insira valores numéricos válidos para peso e comprimento.")

#listar peças

def listar_peças():
    print("\n--- Peças Aprovadas ---")
    for p in peças_aprovadas:
        print(f"ID: {p['id']} | {p['peso']}g | {p['cor']} | {p['comprimento']}cm")
    
    print("\n--- Peças Reprovadas ---")
    for p in peças_reprovadas:
        print(f"ID: {p['id']} | Motivo: {p['motivo']}")

def remover_peça():
    id_busca = input("Digite o ID da peça que deseja remover: ")
    removida = False
    
    # Busca em ambas as listas
    for lista in [peças_aprovadas, peças_reprovadas]:
        for p in lista:
            if p['id'] == id_busca:
                lista.remove(p)
                print(f"Peça {id_busca} removida com sucesso.")
                removida = True
                break
    if not removida:
        print("ID não encontrado.")

#gerar relatorio

def gerar_relatorio():
    limpar_tela()
    total_aprovadas = len(peças_aprovadas)
    total_reprovadas = len(peças_reprovadas)
    caixas_em_andamento = 1 if total_aprovadas % LIMITE_CAIXA != 0 else 0
    total_caixas = len(caixas_fechadas) + caixas_em_andamento

    print("========================================")
    print("       RELATÓRIO FINAL DE PRODUÇÃO      ")
    print("========================================")
    print(f"Total de Peças Aprovadas: {total_aprovadas}")
    print(f"Total de Peças Reprovadas: {total_reprovadas}")
    print(f"Total de Caixas Utilizadas: {total_caixas}")
    print("----------------------------------------")
    if peças_reprovadas:
        print("Motivos de Reprovação detectados:")
        for p in peças_reprovadas:
            print(f"- Peça {p['id']}: {p['motivo']}")
    print("========================================\n")

# Menu principal

while True:
    print("\nSISTEMA DE CONTROLE DE QUALIDADE INDUSTRIAL")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        cadastrar_peça()
    elif opcao == '2':
        listar_peças()
    elif opcao == '3':
        remover_peça()
    elif opcao == '4':
        print(f"\nTotal de caixas fechadas: {len(caixas_fechadas)}")
        for i, caixa in enumerate(caixas_fechadas, 1):
            ids = [p['id'] for p in caixa]
            print(f"Caixa {i}: {ids}")
    elif opcao == '5':
        gerar_relatorio()
    elif opcao == '0':
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida.")