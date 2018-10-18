## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234@1, umF1#, 2w3E*, 2We3345
# Então, a saída do programa deve ser:
# ABd1234@1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
MIN_SENHA = 6
MAX_SENHA = 12
MAX_N_DIGIT = 9

senha = input("Digite aqui a sua senha: ")

if(len(senha) < MIN_SENHA):
    print("Sua senha eh muito pequena")
elif(len(senha) > MAX_SENHA):
    print("Sua senha eh muito grande")

elif(not ('$' in senha or '#' in senha or '@' in senha)):
    print("Sua senha esta invalida, utilize pelo menos um: [$#@]")
else:
    temMaisc = False
    for caractere in senha:
        if(ord(caractere) in range(ord('A'), ord('Z')+1)):
            temMaisc = True

    if(temMaisc == False):
        print("Nao tem nenhuma letra MAIUSCULA")

    else:
        temNumero = False
        for caractere in senha:
            if(ord(caractere) in range(ord('0'), ord('9')+1)):
                temNumero = True
        if(temNumero == False):
            print("Sua senha nao tem nenhum digito")
        else:
            temMinusc = False
            for caractere in senha:
                if(ord(caractere) in range(ord('a'), ord('z')+1)):
                    temMinusc = True

            if(temMinusc == False):
                print("Nao tem nenhuma letra MINUSCULA")
            else:
                print("PARABENS SUA SENHA EH MUITO BOA")
    


if __name__ == '__main__':
    main()
