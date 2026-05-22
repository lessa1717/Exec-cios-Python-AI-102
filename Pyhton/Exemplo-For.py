print("---Detector de Multas---")
multados = 0

for i in range(1,4):
    velocidade = int(input(f"Velocidade do carro {i} (km/h)"))

    if velocidade > 80:
        print("Multado!")
        multados= multados + 1
    else:
        print("tudo OK!")
    print(f"Total de carros multados hoje: {multados}")