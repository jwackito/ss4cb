class NewsAgency:
    def __init__(self):
        self._subscribers = []

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def notify(self, message):
        for sub in self._subscribers:
            sub.update(message)

class NewsSubscriber:
    def update(self, message):
        print(f"Subscriber received news: {message}")
