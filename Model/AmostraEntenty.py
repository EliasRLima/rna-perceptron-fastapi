from pydantic import BaseModel


class Amostra(BaseModel):
    x1: float
    x2: float
    x3: float
    d: int
