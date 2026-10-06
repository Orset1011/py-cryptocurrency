import pytest
from typing import Generator
from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@pytest.fixture
def exchange_mock() -> Generator[MagicMock, None, None]:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_func:
        yield mock_func


def test_cryptocurrency_action_increase(exchange_mock: MagicMock) -> None:
    exchange_mock.return_value = 110
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_decrease(exchange_mock: MagicMock) -> None:
    exchange_mock.return_value = 90
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_no_change(exchange_mock: MagicMock) -> None:
    exchange_mock.return_value = 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
