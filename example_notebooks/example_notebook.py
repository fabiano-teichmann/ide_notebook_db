# Databricks notebook source
from pyspark.sql.types import *


# COMMAND ----------

class GenerateSchema:
    def __init__(self, fields: list):
        self.fields = fields
        self.schema = []

    @property
    def correlation_schema(self) -> dict:
        return {
            "string": StringType(),
            "email": StringType(),
            "phone": StringType(),
            "varchar": StringType(),
            "int": IntegerType(),
            "bigint": LongType(),
            "bit": ByteType(),
            "tinyint": ShortType(),
            "smallint": ShortType(),
            "uniqueidentifier": StringType(),
            "datetime2": TimestampType(),
            "datetime": TimestampType(),
            "id": StringType(),
            "picklist": StringType(),
            "boleam": BooleanType(),
            "address": StringType(),
            "char": StringType(),
            "varbinary": StringType(),
            "date": DateType(),
            "double": DoubleType(),
            "bigint": LongType(),
            "textarea": StringType(),
            "list_double": ArrayType(DoubleType()),
            "list_string": ArrayType(StringType()),
            "decimal": DecimalType(),
            "list_bigint": ArrayType(StringType()),
            "smalldatetime": TimestampType(),
        }

    def generate_schema(self) -> StructType:

        for field in self.fields:
            try:
                self.schema.append(StructField(field["name"], self.correlation_schema[field["col_type"]], False))
            except KeyError:
                self.schema.append(StructField(field["name"], StringType(), False))

        return StructType(self.schema)
