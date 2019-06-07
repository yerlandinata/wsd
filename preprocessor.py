from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from functools import reduce
import string

pipe = lambda *args: lambda x: reduce(lambda acc, f: f(acc), args, x)
clean_word = lambda w: w.translate(str.maketrans('', '', string.punctuation)).lower() 

def normalize_money(s):
    s = s.replace('Rp ', 'Rp')
    tokens = []
    for t in s.split():
        if t[:2] == 'Rp':
            tokens.append('somemoney')
        else:
            tokens.append(t)
    return ' '.join(tokens)

TERBILANG = [
    'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'nol',
    'sepuluh', 'sebelas', 'belas', 'puluh', 'seratus', 'ratus', 'seribu', 'ribu'
]

def normalize_number(s):
    tokens = []
    for t in s.split():
        try:
            int(clean_word(t))
            tokens.append('somenumber')
        except:
            if t in TERBILANG:
                tokens.append('somenumber')
            else:
                tokens.append(t)
    result = ' '.join(tokens)
    while 'somenumber somenumber' in result:
        result = result.replace('somenumber somenumber', 'somenumber')
    return result

stemmer = StemmerFactory().create_stemmer()

def create_stemmer(annotated_words, exception_words):
    def stem(s):
        tokens = []
        for t in s.split():
            allow_stem = reduce(lambda acc, w: acc and w not in clean_word(t), {*annotated_words, *exception_words}, True)
            if allow_stem:
                tokens.append(stemmer.stem(t))
            else:
                tokens.append(clean_word(t))
        return ' '.join(tokens)
    return stem

def create_stop_words_remover(annotated_words, exception_words):
    with open('../stop_words_tala.txt', 'r') as f:
        stop_words = f.readlines()
    stop_words = list(map(str.strip, stop_words))
    stop_words = list(filter(lambda w: w not in {*annotated_words, *exception_words}, stop_words))

    return lambda s: ' '.join(word for word in s.split() if word not in stop_words)
