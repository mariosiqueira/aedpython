from aula05082019.ListaDuplamenteLigada import ListaDuplamenteLigada

listaDuplamenteLigada = ListaDuplamenteLigada()
listaDuplamenteLigada.inserirInicio(2)
listaDuplamenteLigada.inserirInicio(1)
listaDuplamenteLigada.inserirFim(3)
listaDuplamenteLigada.inserir(100, 3)

print('---Imprimir Diretamente:')
listaDuplamenteLigada.imprimirLista()
print('---Remoções:')
listaDuplamenteLigada.remover(1)

print('---Imprimir Lista Após Remoções:')
listaDuplamenteLigada.imprimirLista()
print('Impressão do inicio:')
print(listaDuplamenteLigada.inicio.chave)
 
print('Impressão do fim:')
print(listaDuplamenteLigada.fim.chave)
print('---Imprimir Reversamente:')
listaDuplamenteLigada.imprimirListaReversa()
print('---Tamanho:')
print(listaDuplamenteLigada.imprimirTamanho())