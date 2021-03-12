from bot import bot

'''
Autor:
* Matheus Richter

Descrição:
Esse trabalho consiste na implementação de um chatbot
simples, que responde de acordo com a proximidade do
vetor tf-idf gerado pelo input do usuário com um dos
vetores disponíveis no corpus. O corpus é constituido
arquivo "Computer.txt", que contem o conteúdo disponével
na página da wikipédia "https://en.wikipedia.org/wiki/Computer".
As stopwords foram geradas utilizando o contúdo composto
pelo livro "Frankenstein; Or, The Modern Prometheus",
disponível em: "https://www.gutenberg.org/files/84/84-0.txt";
e pelo livro "The Adventures of Tom Sawyer", disponível
em: "https://www.gutenberg.org/files/74/74-0.txt".

Para testar basta executar este arquivo python e digitar algo,
com relação a computadores, em inglês no terminal, o retorno será 
um documento do corpus, o mais similar, com relação ao input, 
encontrado pelos algoritmos.

Algumas interações possíveis são:
* when were computers invented?
* what is computer i/o and networking?
* tell about bugs
* tell about early cpus
* are bugs computer fault?
* can computer do more than one thing at a time?
* are computers calculating machines?
'''

if __name__ == "__main__":
    bot()
