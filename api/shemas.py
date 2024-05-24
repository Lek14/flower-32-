from pydantic import BaseModel


class BaseFlower(BaseModel):
    name: str
    type: str
    country: str
    blooming_season: str
    variant: str
    price: float


class CreateFlower(BaseFlower):
    pass

class ShowFlower(BaseFlower):
    id: int

# class ShowSuppliersWithFlowers(BaseModel):
