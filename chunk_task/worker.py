import os
import redis
from rq import Worker, Queue, Connection

# Lista de colas a escuchar
listen = ['default']

# URL de conexión a Redis
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

# Conexión a Redis
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
