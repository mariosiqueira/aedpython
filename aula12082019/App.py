from aula12082019.Queue import Queue

fila = Queue()
fila.inserir(1)
fila.inserir(2)
fila.inserir(3)
print('---Lista Após Inserções:')
fila.imprimirQueue()
print('---Inicio:', fila.inicio.elemento)
print('---Fim:', fila.fim.elemento)
print('---Lista Após Remoções:')

fila.remover()
fila.remover()
fila.remover()
# fila.remover()
fila.imprimirQueue()
print('---Inicio:', fila.inicio)
print('---Fim:', fila.fim)
