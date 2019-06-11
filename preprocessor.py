from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from functools import reduce
import string

pipe = lambda *args: lambda x: reduce(lambda acc, f: f(acc), args, x)
remove_punctuation = lambda s: s.translate(str.maketrans('', '', string.punctuation))
clean_word = lambda w: remove_punctuation(w).lower() 

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

PERSONAL_PRONOUNS = ['saya', 'aku', 'dia', 'mereka', 'anda', 'kamu', 'beliau', 'ia']

def normalize_personal_pronoun(s):
    return ' '.join([token if token not in PERSONAL_PRONOUNS else 'somepersonalpronoun' for token in s.split()])

DEMONSTRATIVE_PRONOUNS = ['ini', 'itu', 'sini', 'situ']

def normalize_demonstrative_pronoun(s):
    return ' '.join([token if token not in DEMONSTRATIVE_PRONOUNS else 'somedemonstrativepronoun' for token in s.split()])

COORDINATING_CONJUNCTIONS = ['dan', 'tetapi', 'atau']

def normalize_coordinating_conjunction(s):
    return ' '.join([token if token not in COORDINATING_CONJUNCTIONS else 'somecoordinatingconjunction' for token in s.split()])

WEEKDAYS = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']

def normalize_weekday(s):
    return ' '.join([token if token not in WEEKDAYS else 'someweekday' for token in s.split()])

MONTHS = ['januari', 'februari', 'maret', 'april', 'mei', 'juni', 'juli', 'agustus', 'september', 'oktober', 'november', 'desember']

def normalize_month(s):
    return ' '.join([token if token not in MONTHS else 'somemonth' for token in s.split()])

DETERMINERS = ['semua', 'beberapa', 'si', 'para', 'sang']

def normalize_determiner(s):
    return ' '.join([token if token not in DETERMINERS else 'somedeterminer' for token in s.split()])

PREPOSITIONS = ['dengan', 'di', 'ke', 'oleh', 'pada', 'untuk']

def normalize_preposition(s):
    return ' '.join([token if token not in PREPOSITIONS else 'somepreposition' for token in s.split()])

def create_obvious_verb_normalizer(annotated_words, exception_words):
    return lambda s: ' '.join([
        'someverb' if (
            (stemmer.stem(clean_word(token)) not in {*annotated_words, *exception_words}) and
            (token not in {*annotated_words, *exception_words}) and
            len(token) > 5 and
            token[0] in string.ascii_lowercase and
            (token[:3] == 'ber' or token[:2] == 'di' or token[:2] == 'me')
            and stemmer.stem(token)[:2] != 'di'
            and stemmer.stem(token)[:2] != 'me'
            and stemmer.stem(token)[:3] != 'ber' 
        ) else token for token in s.split()
    ])

def remove_normalized(s):
    return ' '.join([token for token in s.split() if 'some' not in token])

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
