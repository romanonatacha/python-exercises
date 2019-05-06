segundos = input ('Por favor, entre com o número de segundos que deseja converter: ')
totSegundos = int(segundos)

dias = totSegundos // 86400
segundosRest = totSegundos % 86400
horas = segundosRest // 3600
segundosRest2 = totSegundos % 3600
minutos = segundosRest2 // 60
segundosRestFinal = segundosRest2 % 60

print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundosRestFinal, 'segundos.')
