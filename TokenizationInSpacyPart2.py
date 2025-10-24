import spacy
from spacy.symbols import ORTH
nlp = spacy.blank("en")
doc = nlp("gimme this object. I required this.")    
nlp.tokenizer.add_special_case("gimme",[
    {ORTH:"gim"},
    {ORTH:"me"}
])
tokens = [token.text for token in doc]
print(tokens)
print(nlp.pipe_names)
nlp.add_pipe('sentencizer')
print(nlp.pipe_names)