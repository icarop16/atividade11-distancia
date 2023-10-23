# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input("Adicione a distância que é sua viagem: "))
print(f"A sua distância é de {distancia}Km.")
cobrador1 = distancia * 0.50
cobrador2 = distancia * 0.45
if 200 < distancia:
    print(f"Sua viagem teve uma distância de {distancia}Km, sendo maior que 200Km, então o valor da passagem é {cobrador2}R$.")
elif 200 == distancia:
    print(f"Sua viagem teve uma distância e {distancia}km, sendo igual a 200Km, então o valor da passagem é {cobrador1}R$.")    
else:
    print(f"Sua viagem teve uma distância de {distancia}Km, sendo menor que 200Km, então o valor da passagem é {cobrador1}R$.")

