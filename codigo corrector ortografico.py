import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

subtitle = "Se realizaron 72.297 exámenes PCR en las últimas 24 horas, y la posatividad llego a 10,6%."
subtitle_2 = subtitle.replace(",","")
print(subtitle_2)
subtitle_corregido = correction(subtitle_2)
subtitle_split = subtitle_2.split()
i=0
while i<len(subtitle_split):
    subtitle_split[i] = subtitle_split[i].lower()
    i=i+1

if subtitle == subtitle_corregido:
    faltas_ortograficas = 0
else:
    faltas_ortograficas = 1

i=0
contador_faltas_ortograficas = 0
faltas_ortograficas_lista = []
while i<len(subtitle_split):
    palabra_correccion = correction(subtitle_split[i])
    if subtitle_split[i] == palabra_correccion:
        i=i+1
    else:
        contador_faltas_ortograficas = contador_faltas_ortograficas + 1
        faltas_ortograficas_lista.append(subtitle_split[i])
        i=i+1
        
print(faltas_ortograficas)
print(contador_faltas_ortograficas)
i=0
while i<len(faltas_ortograficas_lista):
    print(faltas_ortograficas_lista[i])
    i=i+1
