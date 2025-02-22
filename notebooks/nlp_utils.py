from pydantic import BaseModel
from gliner import GLiNER

model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1", max_length=768)


class Entity(BaseModel):
    start: int
    end: int
    text: str
    label: str
    score: float


def nlp_tokens(text):
    token_generator = model.data_processor.words_splitter(text)
    tokens = [t for t in token_generator]
    return len(tokens)
