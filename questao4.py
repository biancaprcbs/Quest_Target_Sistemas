def percentual_por_estado(vetor_faturamento):
	valor_total = sum(vetor_faturamento)
	perc_SP = (vetor_faturamento[0] * 100) / valor_total
	perc_RJ = (vetor_faturamento[1] * 100) / valor_total
	perc_MG = (vetor_faturamento[2] * 100) / valor_total
	perc_ES = (vetor_faturamento[3] * 100) / valor_total
	perc_outros = (vetor_faturamento[4] * 100) / valor_total
	
	return perc_SP, perc_RJ, perc_MG, perc_ES, perc_outros

# Valores de faturamento mensal

faturamento_mensal = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

sp, rj, mg, es, out = percentual_por_estado(faturamento_mensal)

print("Percentual do estado SP:", sp)
print("Percentual do estado RJ:", rj)
print("Percentual do estado MG:", mg)
print("Percentual do estado ES:", es)
print("Percentual de outros estados:", out)

