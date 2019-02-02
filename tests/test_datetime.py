import json
from datetime import datetime, timezone

import pytest
from starlette.testclient import TestClient

from fastapi import FastAPI
from pydantic import BaseModel


class ModelWithDatetimeField(BaseModel):
    dt_field: datetime
    class Config:
        json_encoders = {
            datetime: lambda dt: dt.replace(
                microsecond=0, tzinfo=timezone.utc
            ).isoformat()
        }


app = FastAPI()
model = ModelWithDatetimeField(dt_field=datetime.utcnow())


@app.get("/model", response_model=ModelWithDatetimeField)
def get_model():
    return model


@pytest.fixture
def client():
    yield TestClient(app)


def test_dt(client):
    with client:
        response = client.get("/model")
    assert json.loads(model.json()) == response.json()
