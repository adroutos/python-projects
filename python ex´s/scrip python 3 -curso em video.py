
def bemvindo():
    print(" Bem vindo! espero que se divirta!!")

def jogo(soma):
    usuario = input("Deseja encerrar a calculadora?(s/n")
    if(usuario == 's'):
        return
    usuario = int(input("Deseja digitar numeros ou calculalos?(1/2)"))
    if(usuario == 1):
        val = int(input("digite seu numero : "))
        soma = soma + val
        jogo(soma)
    else:
        print("A soma eh: {}".format(soma))

bemvindo()
soma = 0
jogo(soma)

        
