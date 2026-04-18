import datetime

def analisar_imc(p, a):
    imc = p / (a ** 2)
    
    if imc < 18.5: classif = "Abaixo do peso (Risco de baixa imunidade)"
    
    elif imc < 25: classif = "Peso ideal (Saudável)"
    
    elif imc < 30: classif = "Sobrepeso (Alerta metabólico)"
    
    else: classif = "Obesidade (Risco cardiovascular elevado)"
    
    return f"{round(imc, 2)} - {classif}"

def analisar_mental_avancado(sono, rotina, humor):
   
    if sono < 7:
        status_sono = "DESREGULAR (Privação)"
        melhoria = " Aumentar as horas de repouso para estabilizar o humor e o foco."
        
    elif sono > 9:
        status_sono = "DESREGULAR (Excesso)"
        melhoria = " Investigar se o sono é de baixa qualidade ou se há desmotivação."
        
    else:
        status_sono = "REGULAR"
        melhoria = " Manter a rotina atual, o corpo está descansando bem."

   
    relatorio = (f"Sono {status_sono} ({sono}h). Humor: {humor}. "
                 f"Rotina: {rotina}. >> O QUE MELHORAR: {melhoria}")
    
    return relatorio

def analisar_ciclo(data_u, duracao, total, anomalia):
    
    data_dt = datetime.datetime.strptime(data_u, "%d/%m/%Y")
    proxima = data_dt + datetime.timedelta(days=total)
    
    return f"Fluxo: {duracao} dias | Próxima prevista: {proxima.strftime('%d/%m/%Y')} | Obs: {anomalia}"


biblioteca = []

while True:
    
    print("\n" + "="*60)
    print("           SISTEMA MÉDICO DE ALTA PRECISÃO")
    print("="*60)
    print("1 - Cadastrar Nova Ficha")
    print("2 - Acessar Biblioteca Detalhada")
    print("3 - Sair")
    
    menu_principal = input("\nEscolha uma opção: ")

    if menu_principal == "1":
        
        print("\n -PASSO 1: DADOS PESSOAIS-")
        nome = input("Nome Completo: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ").upper()

        ficha = {
            "Nome": nome, "Idade": idade, "Sexo": sexo,
            "IMC": "Não avaliado", "Saúde Mental": "Não avaliado", "Ciclo": "Não avaliado"
        }

        print(f"\n -PASSO 2: EXAMES PARA {nome.upper()} -")
        print("1 - Calcular IMC")
        print("2 - Avaliação de Saúde Mental")
        
        
        if sexo == 'F':
            print("3 - Registro de Ciclo Menstrual")
            print("4 - Realizar Todas as Avaliações")
            
        else:
            print("3 - Realizar Ambas as Avaliações (IMC + Mental)")

        escolha = input("\nO que deseja fazer? ")

   
        if (sexo == 'F' and escolha in ['1', '4']) or (sexo == 'M' and escolha in ['1', '3']):
            
            print("\n>> COLETA IMC")
            
            p = float(input("   Peso (kg): "))
            a = float(input("   Altura (m): "))
            ficha["IMC"] = analisar_imc(p, a)

        
        if (sexo == 'F' and escolha in ['2', '4']) or (sexo == 'M' and escolha in ['2', '3']):
            
            print("\n>> COLETA SAÚDE MENTAL")
            
            h_sono = float(input("   Média de horas de sono: "))
            rot = input("   Descreva sua rotina (Estressante, cansativa, parada, tranquila...): ")
            hum = input("   Como você se sente hoje? ")
            ficha["Saúde Mental"] = analisar_mental_avancado(h_sono, rot, hum)

   
        if sexo == 'F' and escolha in ['3', '4']:
            
            print("\n>> COLETA CICLO MENSTRUAL")
            
            d_m = input("   Data da última menstruação (DD/MM/AAAA): ")
            dur = int(input("   Duração do fluxo (dias): "))
            tot = int(input("   Duração média do ciclo (ex: 28): "))
            ano = input("   Houve anomalias ou dores intensas? ")
            ficha["Ciclo"] = analisar_ciclo(d_m, dur, tot, ano)

        biblioteca.append(ficha)
        print(f"\n✓ Prontuário de {nome} finalizado e salvo!")

    elif menu_principal == "2":
        print("\n" + "█"*60)
        print("                 RELATÓRIO GERAL DA BIBLIOTECA")
        print("█"*60)
        
        if not biblioteca:
            print("\nNenhum registro encontrado na biblioteca.")
            
        else:
            for i, f in enumerate(biblioteca):
                
                print(f"\n--- FICHA #{i+1} ---")
                print(f"IDENTIFICAÇÃO: {f['Nome']} | {f['Idade']} anos | Sexo: {f['Sexo']}")
                print(f"ESTADO IMC: {f['IMC']}")
                print(f"SAÚDE MENTAL: {f['Saúde Mental']}") 
                
                if f['Sexo'] == 'F':
                    
                    print(f"CICLO MENSTRUAL: {f['Ciclo']}")
                print("-" * 60)
        
        input("\nPressione ENTER para retornar ao menu...")

    elif menu_principal == "3":
        
        print("Saindo do sistema...")
        
        break
