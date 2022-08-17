
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

import io
import os
text="এটাই আমাদের প্রিয় খাবার"

new_text=word_tokenize(text)

with open("F:/pre-rocessing/bn.txt",encoding='utf-8-sig') as f:
        lst = [x for x in f.read().split()]
        stop_words = lst

filtered_text=[w for w in new_text if not w in stop_words]
clean_text=TreebankWordDetokenizer().detokenize(filtered_text)

print(clean_text)

