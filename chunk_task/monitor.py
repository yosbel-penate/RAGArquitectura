import os
import time
import redis
from rq import Queue
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tasks import process_file

# URL de conexión a Redis
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)
q = Queue(connection=conn)

class Watcher:
    DIRECTORY_TO_WATCH = "./documents"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        if event.is_directory:
            return None
        elif event.src_path.endswith('.txt'):
            print(f"Nuevo archivo detectado: {event.src_path}")
            q.enqueue(process_file, event.src_path)

if __name__ == '__main__':
    w = Watcher()
    w.run()
