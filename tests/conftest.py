import pytest

# works like a static variables


@pytest.fixture
def candidate():
    return("Luffy")


@pytest.fixture
def voter_id():
    return(7)
