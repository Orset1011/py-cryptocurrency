import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mock_prediction(monkeypatch):
    def _mock_prediction(prediction_rate):
        monkeypatch.setattr(
            "app.main.get_exchange_rate_prediction",
            lambda current_rate: prediction_rate,
        )

    return _mock_prediction


def test_buy_more_cryptocurrency(mock_prediction):
    mock_prediction(106)

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(mock_prediction):
    mock_prediction(94)

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing(mock_prediction):
    mock_prediction(100)

    assert cryptocurrency_action(100) == "Do nothing"


def test_exactly_5_percent_higher(mock_prediction):
    mock_prediction(105)

    assert cryptocurrency_action(100) == "Do nothing"


def test_exactly_5_percent_lower(mock_prediction):
    mock_prediction(95)

    assert cryptocurrency_action(100) == "Do nothing"
