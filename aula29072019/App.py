from aula29072019.ListaLigada import ListaLigada
listaLigada = ListaLigada()
listaLigada.inserirInicio(2, 'Mario', '222222222-22')
listaLigada.inserirInicio(1, 'Vandre', '111111111-11')
listaLigada.inserirFim(3, 'José', '333333333-33')
listaLigada.inserir('500', 'Boby', '999999999-99', 3)
print('---Inserções:')
listaLigada.imprimirLista()
print('---Tamanho:')
print(listaLigada.imprimirTamanho())
print('---Remoções:')
listaLigada.remover(3)
listaLigada.remover(1)
listaLigada.remover(0)

listaLigada.imprimirLista()
print('---Tamanho:')
print(listaLigada.imprimirTamanho())
# print('Buscar Elemento:')
# print(listaLigada.buscarElemento(2).toString())