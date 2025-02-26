from typing import List

from pydantic import BaseModel


STOP_WORDS = [
    "friday",
    "he",
    "her",
    "i",
    "it",
    "miss",
    "monday",
    "one",
    "saturday",
    "she",
    "sunday",
    "they",
    "thursday",
    "today",
    "tomorrow",
    "tuesday",
    "we",
    "wednesday",
    "what",
    "which",
    "who",
    "you",
]
LABELS = [
    "Date",
    "Demographic Group",
    "Event",
    "Geo-Political Entity",
    "Location",
    "Musical Group",
    "Nationality, Religious, or Political Group",
    "Organization",
    "Person",
    "Product",
    "Time",
    "Work of Art",
]


class Entity(BaseModel):
    start: int
    end: int
    text: str
    label: str
    score: float


def nlp_tokens(text, model):
    token_generator = model.data_processor.words_splitter(text)
    tokens = [t for t in token_generator]
    return len(tokens)


def get_dialogue(text: str):
    lines = [
        line.split(": ")[1]
        for line in text.strip().splitlines()
        if len(line.split(": ")) > 1
    ]

    return "\n".join(lines)


def get_entities(chunks: List[str], model):
    results = {}
    for i, chunk in enumerate(chunks):
        dialogue_only = get_dialogue(chunk)
        entities = model.predict_entities(dialogue_only, LABELS, threshold=0.5)
        for entity in entities:
            ner_entity = entity["text"]
            ner_label = entity["label"]
            if ner_entity.lower() not in STOP_WORDS:
                if ner_entity.lower() in results:
                    results[ner_entity.lower()]["keys"].add(ner_entity)
                    results[ner_entity.lower()]["labels"].add(ner_label)
                    results[ner_entity.lower()]["indexes"].update([i - 1, i, i + 1])
                else:
                    results[ner_entity.lower()] = {
                        "keys": set([ner_entity]),
                        "labels": set([ner_label]),
                        "indexes": set([i - 1, i, i + 1]),
                    }
    entities = {
        sorted(list(values["keys"]))[0]: {
            "labels": sorted(list(values["labels"])),
            "indexes": sorted([i for i in values["indexes"] if 0 <= i < len(chunks)]),
        }
        for key, values in sorted(results.items())
    }
    return entities


def get_tags(text: str, model, stopwords=[]):
    tags = set()
    entities = model.predict_entities(text, LABELS, threshold=0.5)
    for entity in entities:
        ner_entity = entity["text"]
        if ner_entity.lower() not in STOP_WORDS and ner_entity.lower() not in stopwords:
            tags.add(ner_entity)
    return sorted(list(tags))


def get_relevant_chunks(chunks, indexes):
    relevant_chunks = []
    for i in indexes:
        relevant_chunks.append(chunks[i])
    return relevant_chunks
