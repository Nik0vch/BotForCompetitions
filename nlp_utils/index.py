import spacy
# Загрузка языковой модели
# nlp = spacy.load("ru_core_news_lg")

try:
    nlp = spacy.load("ner_model_ru")
except:
    nlp = spacy.blank("ru")
    # nlp = spacy.load("ru_core_news_lg")