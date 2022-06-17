import os
from dataclasses import dataclass
from os.path import join, dirname, abspath


basedir = abspath(dirname(__file__))
testDB = join(basedir, "database_shopping.db")

db_url = os.environ.get("SQL_DB")


@dataclass
class BaseConfig:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{testDB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@dataclass
class LocalConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    if db_url:
        SQLALCHEMY_DATABASE_URI = db_url


@dataclass
class TestingServerConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQL_DB_TEST")


config = {"local": LocalConfig, "test": TestingServerConfig}
