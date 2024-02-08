def calcular_faturamento(vetor_faturamento):
    menor_valor = min(vetor_faturamento)
    maior_valor = max(vetor_faturamento)
    media_mensal = sum(vetor_faturamento) / len(vetor_faturamento)
    dias_acima_da_media = sum(1 for valor in vetor_faturamento if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_da_media

# Valores de faturamento diário retirado do arquivo json

faturamento_diario = [22174.1664, 24537.6698, 26139.6134, 26742.6612, 42889.2258, 46251.174, 11191.4722, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 25681.8318, 1718.1221, 13220.495, 8414.61]

menor, maior, acima_media = calcular_faturamento(faturamento_diario)

print("Menor valor de faturamento em um dia:", menor)
print("Maior valor de faturamento em um dia:", maior)
print("Número de dias com faturamento acima da média mensal:", acima_media)

