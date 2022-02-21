# Databricks notebook source
import json
import datetime


def save_share(list_share: str, country: str, path: str):
    data = {}
    for share in list_share:
        data.update({"share": share, "country": country, "date": datetime.date.today().isoformat()})

    with open(f"{path}/share_{country}.json", mode="w") as f:
        f.write(json.dumps(data))
# COMMAND ---------- 
