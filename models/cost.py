from pydantic import BaseModel, Field


class Cost(BaseModel):
    cost_id: int = Field(gt=0)
    description: str = Field(min_length=2, max_length=100)
    amount: float = Field(gt=0)



