from src.infra.consumer import Consumer
import pytest


@pytest.mark.parametrize("coin", [
    ('BTC'),
    ('ETH'),
    ('AMP')
])
def test_consumer_validate_url(coin):
    consumer = Consumer()
    url = consumer.url.replace('VALUE_OF_COIN', coin)
    response = consumer.validate_url(url)
    assert response is True
