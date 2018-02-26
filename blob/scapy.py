import spacy
nlp = spacy.load('en')

def similarity(base, ref):
    doc1 = nlp(base)
    doc2 = nlp(ref)
    return doc1.similarity(doc2)
