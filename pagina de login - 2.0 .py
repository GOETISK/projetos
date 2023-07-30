#faça um programa que crie um usuario e faça login com o usuario e senha dele

                         #faça o painel inicial
print('seja bem vindo!')

print ('para prosseguir escolha as opções - \n 1- login \n 2- faça um novo usuario.\n 3- sair do programa ')
opões = 0

                #crie funcionalidades para as funções
while opões == 1 or 2 :
    opões = int (input('para onde iremos?: '))
    if opões == 1 or opões == 2 or opões == 3:
        if opões == 1:
            usuario = str (input('Digite o nome do usuario:'))
            senha = int (input('Digite sua senha:'))
           
        
        elif opões == 2:
          novo_usuario = str (input('Crie um novo usuario:'))
          crie_uma_senha = int (input('Crie uma senha:'))
          
        elif opões == 3:
            print ('saindo do programa...')
            break
          
          #falta coloca uma condição valida para ativa o if e o elif 
          #para validar a condição eles devem verificar se 'novo usuario' e 'crie uma senha' tem algo digitado
          #só assim eles poderão seguir em frente e armazena esses dados em uma nova variavel 
          #até o momento não sei qual condição usa para fazer essa parte funcionar
          
        if novo_usuario.isalpha() :
         usuarios_cadrastados = [novo_usuario] 
         
        if crie_uma_senha != '' :
           senhas_cadrastadas = [crie_uma_senha]
           print ('novo usuario cadrastado com sucesso!')
                  
    else:
        print('comando invalido, por favor digite novamente!')    
    break

#segundo estagio do codigo

while opões == 1 or 2 and opões != 3  :
    opões = int (input('para onde iremos?: '))
    if opões == 1 or opões == 2 or opões == 3:
        if opões == 1:
            usuario = str (input('Digite o nome do usuario:'))
            senha = int (input('Digite sua senha:'))
            if usuario == novo_usuario and senha == crie_uma_senha:
                print('login com sucesso!')
            else:
                print ('opção invalida, usuario não existe')
        elif opões == 2:
          novo_usuario = str (input('Crie um novo usuario:'))
          crie_uma_senha = int (input('Crie uma senha:'))
          if opões == 3:
            print( 'saindo do programa!')
            break
    else:
        print('comando invalido, o programa esta se encerrando....!')    
    break

#estagio 3 do codigo
while opões == 1 or 2 and opões != 3  :
    opões = int (input('para onde iremos?: '))
    if opões == 1 or opões == 2 or opões == 3:
        if opões == 1:
            usuario = str (input('Digite o nome do usuario:'))
            senha = int (input('Digite sua senha:'))
            if usuario == novo_usuario and senha == crie_uma_senha:
                print('login com sucesso!')
            else:
                print ('opção invalida, usuario não existe')
        
        elif opões == 2:
          novo_usuario = str (input('Crie um novo usuario:'))
          crie_uma_senha = int (input('Crie uma senha:'))
          if opões == 3:
            print( 'saindo do programa!')
            break
    else:
        print('comando invalido, o programa esta se encerrando....!')    
    break


                 
