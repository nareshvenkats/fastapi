import sys
from typing import Optional, Union

import pytest
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.testclient import TestClient

skip_py36 = pytest.mark.skipif(sys.version_info < (3, 7), reason="skip python3.6")

app = FastAPI()


class Item(BaseModel):
    name: Optional[str] = None


class ExtendedItem(Item):
    age: int


@app.post("/items/")
def save_union_different_body(item: Union[ExtendedItem, Item]):
    return {"item": item}


client = TestClient(app)


inherited_item_openapi_schema = {
    "openapi": "3.0.2",
    "info": {"title": "Fast API", "version": "0.1.0"},
    "paths": {
        "/items/": {
            "post": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {"application/json": {"schema": {}}},
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        },
                    },
                },
                "summary": "Save Union Different Body",
                "operationId": "save_union_different_body_items__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "title": "Item",
                                "anyOf": [
                                    {"$ref": "#/components/schemas/ExtendedItem"},
                                    {"$ref": "#/components/schemas/Item"},
                                ],
                            }
                        }
                    },
                    "required": True,
                },
            }
        }
    },
    "components": {
        "schemas": {
            "Item": {
                "title": "Item",
                "type": "object",
                "properties": {"name": {"title": "Name", "type": "string"}},
            },
            "ExtendedItem": {
                "title": "ExtendedItem",
                "required": ["age"],
                "type": "object",
                "properties": {
                    "name": {"title": "Name", "type": "string"},
                    "age": {"title": "Age", "type": "integer"},
                },
            },
            "ValidationError": {
                "title": "ValidationError",
                "required": ["loc", "msg", "type"],
                "type": "object",
                "properties": {
                    "loc": {
                        "title": "Location",
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "msg": {"title": "Message", "type": "string"},
                    "type": {"title": "Error Type", "type": "string"},
                },
            },
            "HTTPValidationError": {
                "title": "HTTPValidationError",
                "type": "object",
                "properties": {
                    "detail": {
                        "title": "Detail",
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/ValidationError"},
                    }
                },
            },
        }
    },
}


@skip_py36
def test_inherited_item_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json() == inherited_item_openapi_schema


@skip_py36
def test_put_extended_item():
    response = client.post("/items/", json={"name": "Foo", "age": 5})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Foo", "age": 5}}


@skip_py36
def test_put_item():
    response = client.post("/items/", json={"name": "Foo"})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Foo"}}
