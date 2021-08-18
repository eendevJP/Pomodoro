import time

print("O pomodoro começou!")
for i in range(4):
    userTimeWork = str(input('Quanto tempo você quer ficar focado? \n'))
    tempoTrabalho = int(userTimeWork) * 60
    userTimeBreak = str(input('Quanto tempo você quer descansar?\n'))
    tempoDescanso = int(userTimeBreak) * 60
    while tempoTrabalho:
        minutos = tempoTrabalho // 60
        segundos = tempoTrabalho % 60
        temporizador = '{:02d}:{:02d}'.format(minutos, segundos)
        print("" + temporizador, end="\r")
        time.sleep(1)
        tempoTrabalho -= 1
    print('Descanso!')
    while tempoDescanso:
        minutos = tempoDescanso // 60
        segundos = tempoDescanso % 60
        temporizador = '{:02d}:{:02d}'.format(minutos, segundos)
        print("" + temporizador, end="\r")
        time.sleep(1)
        tempoDescanso -= 1
    print('Hora de trabalhar!!')
