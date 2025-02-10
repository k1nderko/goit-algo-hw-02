from queue import Queue
import random
import time

request_queue = Queue()
request_id = 0


def generate_request(request_id):
    request_data = f"Заявка №{request_id}"
    request_queue.put(request_data)
    print(f"Заявку {request_data} додано до черги")


def process_request():
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f"Обробка заявки: {request_data}")
    else:
        print("немає заявок у черзі")


while True:
    time.sleep(1)

    try:
        if random.choice([True, False]):
            request_id += 1
            generate_request(request_id)

        if random.choice([True, False]):
            process_request()

    except KeyboardInterrupt:
        break
