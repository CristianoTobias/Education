Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Cristiano Tobias
// Data atual  : 18/06/2022
Var
// Se��o de Declara��es das vari�veis 
a: inteiro
angulo,s: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
a <- abs(-50)
escreval(a)
escreval(exp(2,3))
escreval(raizq(81))
escreval(int(raizq(90)))
escreval(sen(grauprad(90)))
escreval("Informe um angulo")
leia(angulo)
s <- sen(grauprad(angulo))
escreval("O seno de", angulo, " �",s)

Fimalgoritmo