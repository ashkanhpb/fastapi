from pydantic import BaseModel, Field, field_validator
import  re


class Cost(BaseModel):
    cost_id: int = Field(gt=0)
    description: str = Field(min_length=2, max_length=100)
    amount: float = Field(gt=0)


@field_validator('cost_id')
def validate_cost_id(v):
    if v < 0:
        raise ValueError('cost id must be greater than 0')
    return v


@field_validator('amount')
def validate_description(v):
    pattern = r'^\d+(\.\d+)?$'
    match = re.match(pattern, v)
    if not match:
        raise ValueError('cost amount is wrong')
    return v

