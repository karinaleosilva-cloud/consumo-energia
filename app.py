#calculadora de consumo elétrico inteligente
#atividade curso DS ag.05 

#entrada 
nome_do_aparelho = input("Digite o nome do aparelho: ")
potencia_do_aparelho = float(input("digite a potência do aparelho em watts (W): "))
tempo_medio_de_uso_por_dia = float(input("Digite o tempo médio de uso por dia em horas (h): "))


#processamento 
consumo_mensal = (potencia_do_aparelho * tempo_medio_de_uso_por_dia * 30) / 1000

#Saída
print(f"aparelho {nome_do_aparelho}")
print(f"consumo mensal estimado: {consumo_mensal:.2f} kWh")  