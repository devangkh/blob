from rake_nltk import Rake


def get_ranked_phrases(text, score=False):
    r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
#     r = Rake(<language>) # To use it in a specific language supported by nltk.

    # If you want to provide your own set of stop words and punctuations to
    # r = Rake(<list of stopwords>, <string of puntuations to ignore>)
    
    r.extract_keywords_from_text(text)
    if score:
        return r.get_ranked_phrases_with_scores()
    else:
        return r.get_ranked_phrases()


def get_word_frequency_distribution(text):
    r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
    r.extract_keywords_from_text(text)
    return r.get_word_frequency_distribution()

def get_word_degrees(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    return r.get_word_degrees()

