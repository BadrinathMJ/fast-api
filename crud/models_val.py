from pydantic import BaseModel, Field
from typing import Optional
class Employee(BaseModel):
    id: int = Field(...,gt=0)
    name: str = Field(...,min_length=3, max_length=30)
    department: str = Field(...,min_length=3, max_length=30)
    age: Optional[int] = Field(default=None)