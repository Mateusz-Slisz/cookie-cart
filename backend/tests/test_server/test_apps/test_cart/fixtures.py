import uuid

import pytest


@pytest.fixture
def random_id() -> str:
    return str(uuid.uuid4())
