import redis
from modules.config import FileManager, Config

config = Config(2)
rdispool = redis.ConnectionPool(host=config.db.redis['db_host'], port=config.db.redis['db_port'], db=15)

def rdis():
    return redis.Redis(connection_pool=rdispool)
