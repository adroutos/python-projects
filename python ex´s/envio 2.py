ordem = ["primeira","segunda","terceira","quarta"]
valores = []
i = 0
media = 0
while(i < 4):
    valores.append(int(input("Digite a " + ordem[i] + " nota:")))
    media = media + valores[i]
    i = i + 1
    
media = media/4

print("A média aritmética é",media)

