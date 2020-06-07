#programa de teste da função while com loop

print("Qual é o seu nome?")
Nome = input()
print("Seja bem vindo à Matrix " + Nome)
print("Por gentileza nos forneça a senha para acesso ao código fonte")
Pass = input()
while Pass != "bolodecenoura":
    print("Acesso negado")
    Pass = input()
print("Parabéns " + Nome + " você tem acesso total à Matrix agora")
ImpDesn = input()
