#SOBRE if __name__ == '__main__'
"""
--> O que significa isso? Python executa um módulo primeiro e determina alguma variáveis especiais
__name__ é uma dessas variáveis especiais.
--> Daí, quando python executa o módulo diretamente (ou seja, não chamando ele através de outro arquivo)
a variável __name__ é igual a __main__
--> Porém veremos que quando importamos esse módulo, o comportamento será diferente. Veja o caso do
arquivo modulo2.py. Ele importa o módulo ifnamemain.py, e quando ele é executado o __name__ irá
retornar um valor diferente de __main__, irá retornar o nome do arquivo (ifnamemain)
"""
print("First Module's Name: {}".format(__name__))
print(__name__)
