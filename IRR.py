def calculadora_ir(salario_bruto):
    #tabela de aliquotas e faixas do imposto de renda
    tabela_ir = [
        {"faixa":(0,1903.98),"aliquota":0,"deducao":0},

        {"faixa":(1903.99,2826.65),"aliquota":7.5,"deducao":142},

        {"faixa":(2826.66,2751.05),"aliquota":15,"deducao":354},

        {"faixa":(751.06,4664.68),"aliquota":22.5,"deducao":636},

        {"faixa":(4664.69,float("inf")),"aliquota":27.5,"deducao":869}

    ]
    #CALCULAR O IMPORTO DE RENDA
    resultado = 0 
    valorDeducao = 0
    valorAliquota = 0
    for faixa in tabela_ir:
        if salario_bruto > faixa["faixa"][0] and salario_bruto <= faixa["faixa"][1]: 
                resultado = (salario_bruto * faixa["aliquota"]) / 100 - faixa["deducao"]
                valorAliquota =faixa["aliquota"]
                valoDeducao = faixa["deducao"]
                break
    return resultado, valorAliquota, valoDeducao


#testando nossa função de calculo do imposto de renda
salario_bruto = float(input("Informe o seu salario bruto: "))
resultado_final, valorAliquota, valoDeducao = calculadora_ir(salario_bruto)
salario_liquido = salario_bruto - resultado_final

print(f'O Imposto de renda devido é de R$ {resultado_final:.2f}')
print(f'A Aliquota aplicada foi de: R$ {valorAliquota}%')
print(f'A dedução foi de: R$ {valoDeducao}')
print(f'O Salario liquido será de: R$ {salario_liquido:.2f}')
print(f'Salário bruto de: R$ {salario_bruto:.2f}')
    
