import os

import investpy

from example_notebooks.utils.logger import logger
from save_share import save_share


def get_list_share(country: str):
    list_share = investpy.get_stocks_list(country=country)
    save_share(list_share=list_share, country=country, path=os.environ["PATH_LIST_SHARE"])


if __name__ == "__main__":
    logger.info("Start get list share")
    get_list_share("brazil")
    logger.info("Finished")
