import config
import sqlalchemy
from sqlalchemy import create_engine
import mysql.connector

config.schema = 'arrests'
config.port = 3306

sql_alchemy_connection = (
                                f'mysql+mysqlconnector://'
                                f'{config.user}:{config.password}'
                                f'@{config.host}:{config.port}'
                                f'/{config.schema}'
                           )
db = create_engine(sql_alchemy_connection)

db.connect()