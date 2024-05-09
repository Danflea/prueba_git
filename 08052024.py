x= "Hola git"
print(x)

def pesoPromedio(P):
  return sum(P['peso']) / len(P['peso'])

def IMC(P):
  imc = []
  for i in range(len(P['talla'])):
    imc.append(P['peso'][i] / (P['talla'][i] ** 2))
  return imc

def sobrepeso(P):
  sobrepeso = 0
  for i in range(len(P['talla'])):
    if (P['peso'][i] / (P['talla'][i] ** 2)) > 25:
      sobrepeso += 1
  return sobrepeso / len(P['talla']) * 100

def reporte(P):
  with open('reporte.txt', 'w') as f:
    f.write(f'Peso promedio: {pesoPromedio(P)}\n')
    f.write('IMC:\n')
    for i in range(len(P['talla'])):
      f.write(f'Paciente {i+1}: {IMC(P)[i]}\n')
    f.write(f'Porcentaje de pacientes con sobrepeso: {sobrepeso(P)}\n')


P = {'talla':[1.56,1.70,1.63,1.58], 'peso':[68,52,69,52], 'presión':[118,120,120,119]}
print(pesoPromedio(P)) # imprime 59.5
print(IMC(P)) # imprime [27.480106100795757, 21.595782073813708, 26.865323741007195, 27.480106100795757]
print(sobrepeso(P)) # imprime 50.0
reporte(P) # crea un archivo reporte.txt con la información del peso promedio, el IMC de cada paciente y el porcentaje de pacientes con sobrepeso
