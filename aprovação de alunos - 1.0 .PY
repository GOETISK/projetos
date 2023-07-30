#leia a nota de todos os alunos 

#primeiro aluno
primeiro_aluno = str (input('nome do primeiro aluno: '))
primeira_nota = int (input('digite a primeira nota: '))
segunda_nota = int (input('digite a segunda nota: '))
terceira_nota = int (input('digite a terceira nota: '))
quarta_nota = int (input('digite a quarta nota: ')) 

#segundo aluno
segundo_aluno = str (input('nome do segundo aluno: '))
primeira_nota_do_segundo_aluno = int (input('digite a primeira nota: '))
segunda_nota_do_segundo_aluno = int (input('digite a segunda nota: '))
terceira_nota_do_segundo_aluno = int (input('digite a terceira nota: '))
quarta_nota_do_segundo_aluno = int (input('digite a quarta nota: '))

#terceiro aluno
terceiro_aluno = str (input('nome do terceiro aluno: '))
primeira_nota_do_terceiro_aluno = int (input('primeira nota: '))
segunda_nota_do_terceiro_aluno = int (input('segunda nota: '))
terceira_nota_do_terceiro_aluno = int (input('terceira nota: '))
quarta_nota_do_terceiro_aluno = int (input('digite a quarta nota: '))

#quarto aluno
quarto_aluno = str (input('nome do quarto aluno: '))
primeira_nota_do_quarto_aluno = int (input('digite a primeira nota: '))
segunda_nota_do_quarto_aluno = int (input('digite a segunda nota: '))
terceira_nota_do_quarto_aluno = int (input('digite a terceira nota: '))
quarta_nota_do_quarto_aluno = int (input('digite a quarta nota: '))

#quinto aluno
quinto_aluno = str (input('nome do quinto aluno: '))
primeira_nota_do_quinto_aluno = int (input('digite a primeira nota: '))
segunda_nota_do_quinto_aluno = int (input('digite a segunda nota: '))
terceira_nota_do_quinto_aluno = int (input('digite a terceira nota: '))
quarta_nota_do_quinto_aluno = int (input('digite a quarta nota: '))

#sexto aluno
sexto_aluno = str (input('nome do sexto aluno: '))
primreira_nota_do_sexto_aluno = int((input('digite a primeira nota: ')))
segunda_nota_do_sexto_aluno = int ((input('digite a segunda nota: ')))
terceira_nota_do_sexto_aluno = int ((input('digite a terceira nota: ')))
quarta_nota_do_sexto_aluno = int (input('digite a quarta nota: '))

#setimo aluno
setimo_aluno = str (input('nome do setimo aluno: '))
primeira_nota_do_setimo_aluno = int (input('digite a primeira nota: '))
segunda_nota_do_setimo_aluno = int (input('digite a segunga nota: '))
terceira_nota_do_setimo_aluno = int (input('digite a terceira nota: '))
quarta_nota_do_setimo_aluno = int (input('digite a quarta nota: '))

#oitavo aluno
oitavo_aluno = str (input('nome do oitavo aluno: '))
primeira_nota_do_oitavo_aluno = int (input('digite a primeira nota: '))
segunda_nota_do_oitavo_aluno = int (input('digite a segunda nota: '))
terceira_nota_do_oitavo_aluno = int (input('digite a terceira nota: '))
quarta_nota_do_oitavo_aluno = int (input('digite a quarta nota: '))

#nono aluno
nono_aluno = str (input('nome do nono aluno: '))
primeira_nota_do_nono_aluno = int (input('digite a primeira nota: '))
segunda_nota_do_nono_aluno = int (input('digite a segunda nota: '))
terceira_nota_do_nono_aluno = int (input('digite a terceira nota: '))
quarta_nota_do_nono_aluno = int (input('digite a quarta nota: '))

#decimo aluno
decimo_aluno = str (input('nome do decimo aluno: '))
primeira_nota_do_decimo_aluno = int (input('digite a primeira nota: '))
segunda_nota_do_decimo_aluno = int (input('digite a segunda nota: '))
terceira_nota_do_decimo_aluno = int (input('digite a terceira nota: '))
quarta_nota_do_decimo_aluno = int (input ('digite a quarta nota: '))



#calcule sua media e mostre na tela 
média_do_primeiro_aluno = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

média_do_segundo_aluno = (primeira_nota_do_segundo_aluno + segunda_nota_do_segundo_aluno + terceira_nota_do_segundo_aluno + quarta_nota_do_segundo_aluno) / 4

média_do_terceiro_aluno = (primeira_nota_do_terceiro_aluno + segunda_nota_do_terceiro_aluno + terceira_nota_do_terceiro_aluno + quarta_nota_do_terceiro_aluno) / 4

média_do_quarto_aluno = (primeira_nota_do_quarto_aluno + segunda_nota_do_quarto_aluno + terceira_nota_do_quarto_aluno + quarta_nota_do_quarto_aluno) / 4

média_do_quinto_aluno = (primeira_nota_do_quinto_aluno + segunda_nota_do_quinto_aluno + terceira_nota_do_quinto_aluno + quarta_nota_do_quinto_aluno) / 4

média_do_sexto_aluno = (primreira_nota_do_sexto_aluno + segunda_nota_do_sexto_aluno + terceira_nota_do_sexto_aluno + quarta_nota_do_sexto_aluno) / 4

média_do_setimo_aluno = (primeira_nota_do_setimo_aluno + segunda_nota_do_setimo_aluno + terceira_nota_do_setimo_aluno + quarta_nota_do_setimo_aluno) / 4

média_do_oitavo_aluno = (primeira_nota_do_oitavo_aluno + segunda_nota_do_oitavo_aluno + terceira_nota_do_oitavo_aluno + quarta_nota_do_oitavo_aluno) / 4

média_do_nono_aluno = (primeira_nota_do_nono_aluno + segunda_nota_do_nono_aluno + terceira_nota_do_nono_aluno + quarta_nota_do_nono_aluno) / 4

média_do_decimo_aluno = (primeira_nota_do_decimo_aluno + segunda_nota_do_decimo_aluno + terceira_nota_do_decimo_aluno + quarta_nota_do_decimo_aluno) / 4


print ('{}, o primeiro  aluno ficou com uma média de {}'.format(primeiro_aluno,média_do_primeiro_aluno ))
print ('{}, o segundo  aluno ficou com uma média de {}'.format(segundo_aluno,média_do_segundo_aluno))
print ('{}, o terceiro  aluno ficou com uma média de {}'.format(terceiro_aluno,média_do_terceiro_aluno))
print ('{}, o quarto  aluno ficou com uma média de {}'.format(quarto_aluno,média_do_quarto_aluno))
print ('{}, o quinto  aluno ficou com uma média de {}'.format(quinto_aluno,média_do_quinto_aluno))
print ('{}, o sexto aluno ficou com uma média de {}'.format(sexto_aluno,média_do_sexto_aluno))
print ('{}, o setimo aluno ficou com uma média de {}'.format(setimo_aluno,média_do_setimo_aluno))
print ('{}, o oitavo aluno ficou com uma média de {}'.format(oitavo_aluno,média_do_oitavo_aluno))
print ('{}, o nono aluno ficou com uma média de {}'.format(nono_aluno,média_do_nono_aluno))
print ('{}, o decimo aluno ficou com uma média de {}'.format(decimo_aluno,média_do_decimo_aluno))



#mostre quais alunos foram aprovados e reprovados na tela

aprovados = 0
reprovados = 0

if média_do_primeiro_aluno >= 5:
  print ('{},aprovado!'.format(primeiro_aluno))
  aprovados += + 1
else:
  print ('{},reprovado!'.format(primeiro_aluno))
  reprovados += +1
  
if média_do_segundo_aluno >= 5:
  print ('{},aprovado!'.format(segundo_aluno))
  aprovados += + 1
else:
  print ('{},reprovado!'.format(segundo_aluno))
  reprovados += +1
  
if média_do_terceiro_aluno >= 5:
  print ('{},aprovado!'.format(terceiro_aluno))
  aprovados += + 1
else:
  print ('{},reprovado!'.format(terceiro_aluno))
  reprovados += +1

if média_do_quarto_aluno >= 5:
  print ('{},aprovado!'.format(quarto_aluno))
  aprovados += + 1
else:
  print ('{},reprovado!'.format(quarto_aluno))
  reprovados += +1
  
if média_do_quinto_aluno >= 5:
  print ('{},aprovado!'.format(quinto_aluno))
  aprovados += + 1
else:
  print ('{},reprovado!'.format(quinto_aluno))
  reprovados += +1  
    
if média_do_sexto_aluno >= 5:
  print ('{},aprovado!'.format(sexto_aluno))
  aprovados += + 1
else:
  print ('{},reprovado!'.format(sexto_aluno))
  reprovados += +1
  
if média_do_setimo_aluno >= 5:
  print ('{},aprovado!'.format(setimo_aluno))
  aprovados += + 1
else:
  print ('{},reprovado!'.format(setimo_aluno))
  reprovados += +1
  
if média_do_oitavo_aluno >= 5:
  print ('{},aprovado!'.format(oitavo_aluno))
  aprovados += + 1
else:
  print ('{},reprovado!'.format(oitavo_aluno))
  reprovados += +1
  
if média_do_nono_aluno >= 5:
  print ('{},aprovado!'.format(nono_aluno))
  aprovados += + 1
else:
  print ('{},reprovado!'.format(nono_aluno))
  reprovados += +1

if média_do_decimo_aluno >= 5:
  print ('{},aprovado!'.format(decimo_aluno))
  aprovados += + 1
else:
  print ('{},reprovado!'.format(decimo_aluno))
  reprovados += +1
  
#mostre quantos passaram e quantos reprovaram na tela
print ('o numero de alunos aprovados foi de {}'.format(aprovados))
print ('o numero de alunos reprovados foi de {}'.format(reprovados))
