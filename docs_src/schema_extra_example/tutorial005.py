from typing import Union

from fastapi import Body, FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


item_examples = {
    "Example Item": {
        "value": {
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        }
    },
    "Example Item; coerce string to float": {
        "value": {
            "name": "Bar",
            "price": "35.4",
        }
    },
    "Raise validation error for 'price'": {
        "value": {
            "name": "Baz",
            "price": "thirty five point four",
        }
    },
}

item_examples_list = [dct["value"] for dct in item_examples.values() if "value" in dct]


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Bar",
                "price": "35.4",
            },
            "examples": item_examples_list,
        }
    }


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(
        ...,
        examples={
            "id as int": {"value": 5},
            "id as string": {"value": "5"},
            "invalid id": {"value": "anything else"},
        },
    ),
    item: Item = Body(examples=item_examples),
):
    results = {"item_id": item_id, "item": item}
    return results
