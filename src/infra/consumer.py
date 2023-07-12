"""Consumer."""
from src.domain.interfaces import ConsumerInterface
import logging
import yaml
import requests


class Consumer(ConsumerInterface):
    """Consumer."""

    def __init__(self) -> None:
        """Construct."""
        ConsumerInterface.__init__(self)
        self.url = "https://www.mercadobitcoin.net/api/VALUE_OF_COIN/ticker/"
        with open("./src/infra/coins.yml", "r") as file:
            try:
                self.coins = yaml.load(file, Loader=yaml.loader.SafeLoader)
            except yaml.YAMLError as exc:
                print(exc)

    def get(self, coin: str):
        """Get info about the chosen coin.

        Parameters
        ----------
        coin: str
            Coin symbol. Must be present in infra/coins.yml
        """
        url = self.url.replace("VALUE_OF_COIN", coin)
        if self.validate_url(url):
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    return r.json()
            except Exception as e:
                logging.error(e)
        else:
            msg = f"URL error: {url} check this out."
            logging.error(msg)
            raise ValueError(msg)

    def validate_url(self, url: str) -> bool:
        """Validate the coin.

        Parameters
        ----------
        coin: str
            coin symbol. Must be present in infra/coins.yml
        coins: str
            Strings present in infra/coins.yml suported by the mercado
            bitcoin API
        """
        coin = url.split("/")[-3]
        coins = list(self.coins.keys())

        if coin in coins:
            return True
            # try:
            #     r = requests.get(url)
            #     if r.status_code == 200:
            #         return True
            # except Exception as e:
            #     logging.info(e)
            #     return False
        else:
            raise ValueError(
                f"'{coin}' must be present in coins supported by "
                f"Mercado bitcoin API. Check this on"
                f"infra/coins.yml"
            )
