import os

import investpy

# MAGIC %run example_notebooks.save_share
# MAGIC %run example_notebooks.utils.logger


def get_list_share(country: str):
    list_share = investpy.get_stocks_list(country=country)
    save_share(list_share=list_share, country=country, path=os.environ["PATH_LIST_SHARE"])


if __name__ == "__main__":
    logger.info("Start get list share")
    get_list_share("brazil")
    logger.info("Finished")
