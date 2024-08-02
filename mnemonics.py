from re import compile
from os import scandir


regex = compile(r'[a-zA-Z]+')

wordlist = set()

for file in scandir('wordlists/'):
    if file.is_file():
        with open(file.path, 'r', encoding='utf8') as f:
            wordlist.update(f.read().split('\n'))


def find_mnemonics(text: str):
    words = regex.finditer(text)
    mnemonics = set()
    mnemonic_buffer = []
    for word in words:
        word = word[0].lower()
        if word in wordlist:
            mnemonic_buffer.append(word)
            
            if len(mnemonic_buffer) % 12 == 0:
                mnemonics.add(' '.join(mnemonic_buffer))
                mnemonic_buffer = []
        else:
            mnemonic_buffer = []

    return mnemonics