# 3. Estatísticas de Texto com collections.Counter
# Enunciado: Funções para limpar texto (minúsculas, remover pontuação), 
# contar palavras e retornar as 10 mais frequentes com suas contagens.
# Entrada (exemplo): "Bom dia, bom humor, bom trabalho!"
# Saída (exemplo): [('bom',3), ('dia',1), ('humor',1), ('trabalho',1)].
import string
from collections import Counter

def estatisticaTexto(string):
    textoTratado = "".join([letra for letra in string if letra not in ['!', '@', '#', '.', ',']]).lower()
    textoCounter = Counter(textoTratado.split())
    print(textoCounter)
    
    
    pass

estatisticaTexto("Bom dia, bom humor, bom trabalho!")