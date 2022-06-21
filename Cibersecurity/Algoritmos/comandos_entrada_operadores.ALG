Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Cristiano Tobias
// Data atual  : 18/06/2022
Var
// Seção de Declarações das variáveis 
a: inteiro
angulo,s: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
a <- abs(-50)
escreval(a)
escreval(exp(2,3))
escreval(raizq(81))
escreval(int(raizq(90)))
escreval(sen(grauprad(90)))
escreval("Informe um angulo")
leia(angulo)
s <- sen(grauprad(angulo))
escreval("O seno de", angulo, " é",s)

Fimalgoritmo