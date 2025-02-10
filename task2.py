from collections import deque


def is_palindrom(text: str) -> bool:
    data = text.lower().replace(" ", "")
    queue = deque(data)
    while len(queue) > 1:
        if queue.pop() != queue.popleft():
            return False
    return True


print(is_palindrom(input("Enter text: ")))