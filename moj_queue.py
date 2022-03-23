class Moj_queue(object):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise QueueException("Queue is Empty")
        return self._data[0]

    def dequeue(self):
        if self.is_empty():
            raise QueueException("Queue is Empty")

        element = self._data[0]
        del self._data[0]
        return element

    def enqueue(self, element):
        self._data.append(element)


class QueueException(Exception):
    pass