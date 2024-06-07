from typing import Literal

from pydantic import BaseModel, Field

class InputModel(BaseModel):
    ingredients: str = Field(
        description='사용할 식재료 목록',
        min_items=1,
        default='김치'
    )
    cuisine_type: Literal['한식', '중식', '일식', '양식', '기타'] = Field(
        description='원하는 요리 종류',
        default='한식',
    )

    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )

class OutputModel(BaseModel):
    output: str = Field(
        description='생성된 레시피',
    )
