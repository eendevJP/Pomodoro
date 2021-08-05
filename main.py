import time

print("O pomodoro começou!")
for i in range(4):
    tempo = 25 * 60
    while tempo:
        minutos = tempo // 60
        segundos = tempo % 60
        temporizador = '{:02d}:{:02d}'.format(minutos, segundos)
        print("" + temporizador, end="\r")
        time.sleep(1)
        tempo -= 1
    print('Descanso!!')
    tempo = 5 * 60
    while tempo:
        minutos = tempo // 60
        segundos = tempo % 60
        temporizador = '{:02d}:{:02d}'.format(minutos, segundos)
        print("" + temporizador, end="\r")
        time.sleep(1)
        tempo -= 1
    print("Hora de Trabalhar!!")
