import spacy
from duckling import DucklingWrapper, Dim

class NERExtractorClass():
    def __init__(self , model='en'):
        self.nlp = spacy.load(model)
        self.duckling_wrapper = DucklingWrapper(parse_datetime=True)
    
    
    def spacy_parse(self ,text):
        # https://spacy.io/api/annotation#named-entities
        
        doc = self.nlp(text)
        ner = []
        for e in doc.ents:
            tmp = {"text":e.text,"label":e.label_}
            ner.append(tmp)
        return ner

    def duckling_parse(self, text):
        weekend = 'by the end of the weekend'
        asap = 'the end of the day'

        text = text.lower()

        text += " "

        text = text.replace("the end of the week ",weekend).replace("the end of week ",weekend).replace("end of week ",weekend).replace("end of the week ",weekend)
        text = text.replace("asap",asap).replace("as soon as possible",asap)

        result = self.duckling_wrapper.parse_time(text)
        return result

        
    
    def parse(self, text ,method='spacy'):
        if method == 'spacy':
            return self.spacy_parse(text)
        if method == 'dickling':
            return self.duckling_parse(text)
        
        return {}