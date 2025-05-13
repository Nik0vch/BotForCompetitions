import spacy
import random
from spacy.util import minibatch, compounding
from spacy.language import Language
from spacy.training import Example
from .interface import *
import logging

nlp: Language
modelName = "personal_data_parser_model_ru"

def Init():
    global nlp
    logging.info("Идёт подключение модели spacy...")
    try:
        nlp = spacy.load(f"NeuralModels/{modelName}")
    except:
        nlp = spacy.blank("ru")

def ParseToNlpFormat(training_values: list[TrainingDataType]):
    result = []
    for data in training_values:
        text = data[0]
        entities = []
        for key, value in data[1].items():
            startIndex = text.rfind(value)
            if startIndex != -1:
                end_index = startIndex + len(value)
                entities.append((startIndex, end_index, key))
        result.append((text, {"entities":entities}))
            
    return result

def GetAttributes(text: str) -> dict[LABELS_NLP, str]:
    doc = nlp(text)
    desired_labels = {label.value for label in LABELS_NLP}
    extracted_entities = {ent.label_: ent.text for ent in doc.ents if ent.label_ in desired_labels}
    return extracted_entities

def TrainNerModel(train_data: list):
    ner = nlp.add_pipe("ner") if "ner" not in nlp.pipe_names else nlp.get_pipe("ner")
    # ner = nlp.get_pipe("ner")
    labels = [label.value for label in LABELS_NLP]

    for label in labels:
        ner.add_label(label)

    optimizer = nlp.begin_training()
    for itn in range(15):
        random.shuffle(train_data)
        losses = {}
        batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.5))
        for batch in batches:
            examples = []
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                examples.append(example)
            nlp.update(examples, drop=0.3, losses=losses, sgd=optimizer)
        print(f"Iteration {itn+1}, Losses: {losses}")
    # Сохраняем модель в папку
    nlp.to_disk(modelName)

def LoadTrainData():
    training_values = [
        (
            "Я Иванов Иван Иванович, 20 лет, из Оренбургской области, город Оренбург, учусь в МФТИ, участвую в номинации \"Программирование\"",
            {
                "NAME": "Иванов Иван Иванович", 
                "AGE": "20",
                "REGION": "Оренбургской области",
                "CITY": "Оренбург",
                "UNIVERSITY": "МФТИ",
                "NOMINATION": "Программирование"
            }
        ),
        (
            "Меня зовут Петрова Анна Сергеевна, 22 года, из Московской области, город Москва, учусь в МГУ, номинация \"Филология\"",
            {
                "NAME": "Петрова Анна Сергеевна",
                "AGE": "22",
                "REGION": "Московской области",
                "CITY": "Москва",
                "UNIVERSITY": "МГУ",
                "NOMINATION": "Филология"
            }
        ),
        (
            "Здравствуйте, я Смирнов Алексей Владимирович, 25 лет, из Ленинградской области, город Санкт-Петербург, учусь в СПбГУ, номинация \"История\"",
            {
                "NAME": "Смирнов Алексей Владимирович",
                "AGE": "25",
                "REGION": "Ленинградской области",
                "CITY": "Санкт-Петербург",
                "UNIVERSITY": "СПбГУ",
                "NOMINATION": "История"
            }
        ),
        (
            "Я Кузнецова Ольга Петрова, 19 лет, из Челябинской области, город Челябинск, учусь в ЧелГУ, номинация \"Математика\"",
            {
                "NAME": "Кузнецова Ольга Петрова",
                "AGE": "19",
                "REGION": "Челябинской области",
                "CITY": "Челябинск",
                "UNIVERSITY": "ЧелГУ",
                "NOMINATION": "Математика"
            }
        ),
        (
            "Меня зовут Григорьев Илья Валерьевич, 28 лет, из Ростовской области, город Ростов-на-Дону, учусь в РГЭУ, номинация \"Экономика\"",
            {
                "NAME": "Григорьев Илья Валерьевич",
                "AGE": "28",
                "REGION": "Ростовской области",
                "CITY": "Ростов-на-Дону",
                "UNIVERSITY": "РГЭУ",
                "NOMINATION": "Экономика"
            }
        ),
        (
            "Я Лебедев Артем Евгеньевич, 21 год, из Республики Татарстан, город Казань, учусь в КГУ, номинация \"Физика\"",
            {
                "NAME": "Лебедев Артем Евгеньевич",
                "AGE": "21",
                "REGION": "Республики Татарстан",
                "CITY": "Казань",
                "UNIVERSITY": "КГУ",
                "NOMINATION": "Физика"
            }
        ),
        (
            "Меня зовут Сидоров Дмитрий Максимович, 30 лет, из Нижегородской области, город Нижний Новгород, учусь в ННГУ, номинация \"Информатика\"",
            {
                "NAME": "Сидоров Дмитрий Максимович",
                "AGE": "30",
                "REGION": "Нижегородской области",
                "CITY": "Нижний Новгород",
                "UNIVERSITY": "ННГУ",
                "NOMINATION": "Информатика"
            }
        ),
        (
            "Я Федорова Мария Владислововна, 24 года, из Самарской области, город Самара, учусь в СГЭУ, номинация \"Экология\"",
            {
                "NAME": "Федорова Мария Владислововна",
                "AGE": "24",
                "REGION": "Самарской области",
                "CITY": "Самара",
                "UNIVERSITY": "СГЭУ",
                "NOMINATION": "Экология"
            }
        ),
        (
            "Здравствуйте, я Ковалев Сергей, 27 лет, из Краснодарского края, город Краснодар, учусь в КубГУ, номинация \"Журналистика\"",
            {
                "NAME": "Ковалев Сергей",
                "AGE": "27",
                "REGION": "Краснодарского края",
                "CITY": "Краснодар",
                "UNIVERSITY": "КубГУ",
                "NOMINATION": "Журналистика"
            }
        ),
        (
            "Меня зовут Голубева Наталья, 23 года, из Амурской области, город Благовещенск, учусь в АмГУ, номинация \"Биология\"",
            {
                "NAME": "Голубева Наталья",
                "AGE": "23",
                "REGION": "Амурской области",
                "CITY": "Благовещенск",
                "UNIVERSITY": "АмГУ",
                "NOMINATION": "Биология"
            }
        ),
        (
            "Я Кузнецов Алексей, 26 лет, из Вологодской области, город Вологда, учусь в ВГСПУ, номинация \"Механика\"",
            {
                "NAME": "Кузнецов Алексей",
                "AGE": "26",
                "REGION": "Вологодской области",
                "CITY": "Вологда",
                "UNIVERSITY": "ВГСПУ",
                "NOMINATION": "Механика"
            }
        ),
        (
            "Здравствуйте, меня зовут Ермакова Елена, 28 лет, из Курской области, город Курск, учусь в Курский ГАУ, номинация \"Агробизнес\"",
            {
                "NAME": "Ермакова Елена",
                "AGE": "28",
                "REGION": "Курской области",
                "CITY": "Курск",
                "UNIVERSITY": "ГАУ",
                "NOMINATION": "Агробизнес"
            }
        ),
        (
            "Меня зовут Смирнов Олег Семёнович, 22 года, из Красноярского края, город Красноярск, учусь в СФУ, номинация \"Химия\"",
            {
                "NAME": "Смирнов Олег",
                "AGE": "22",
                "REGION": "Красноярского края",
                "CITY": "Красноярск",
                "UNIVERSITY": "СФУ",
                "NOMINATION": "Химия"
            }
        ),
        (
            "Я Васильева Ирина, 20 лет, из Архангельской области, город Архангельск, учусь в АГУ, номинация \"Физика\"",
            {
                "NAME": "Васильева Ирина",
                "AGE": "20",
                "REGION": "Архангельской области",
                "CITY": "Архангельск",
                "UNIVERSITY": "АГУ",
                "NOMINATION": "Физика"
            }
        ),
        (
            "Меня зовут Никитин Дмитрий Владимирович, 24 года, из Самарской области, город Тольятти, учусь в ТГУ, номинация \"Экология\"",
            {
                "NAME": "Никитин Дмитрий Владимирович",
                "AGE": "24",
                "REGION": "Самарской области",
                "CITY": "Тольятти",
                "UNIVERSITY": "ТГУ",
                "NOMINATION": "Экология"
            }
        ),
        (
            "Я Зайцева Ольга, 21 год, из Приморского края, город Владивосток, учусь в ДВФУ, номинация \"Информатика\"",
            {
                "NAME": "Зайцева Ольга",
                "AGE": "21",
                "REGION": "Приморского края",
                "CITY": "Владивосток",
                "UNIVERSITY": "ДВФУ",
                "NOMINATION": "Информатика"
            }
        ),
    ]

    TrainNerModel(ParseToNlpFormat(training_values))