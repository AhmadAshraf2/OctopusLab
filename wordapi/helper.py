import re
from parsel import Selector
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract_page_source(response):
    """extracts text from page source and creates word and freq dict"""
    response_sel = Selector(text=str(response.body))
    page_text = clean(response_sel.css(' :not(script)::text').getall())
    page_text = ' '.join(page_text).lower()
    tokens = nltk.word_tokenize(page_text)
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word, pos in tagged if (pos == 'NN' or pos == 'VB')]
    downcased_words = [x.lower() for x in nouns if len(x) > 2]
    return downcased_words


def word_count(wordlist):
    """sorts dict of words and frequency"""
    words = {w: wordlist.count(w) for w in wordlist}
    sorted_words = dict(sorted(words.items(), key=lambda kv: kv[1], reverse=True)[:100])
    return sorted_words


def _sanitize(input_val):
    """ Shorthand for sanitizing results, removing unicode whitespace and normalizing end result"""
    return re.sub('\s+', ' ', input_val.replace('\xa0', ' ')).strip()


def clean(lst_or_str):
    """ Shorthand for sanitizing results in an iterable, dropping ones which would end empty """
    if not isinstance(lst_or_str, str) and getattr(lst_or_str, '__iter__', False):  # if iterable and not a string like
        return [x for x in (_sanitize(y) for y in lst_or_str if y is not None) if x]
    return _sanitize(lst_or_str)
