# ratelimiter
import time

class RateLimiter:
    def __init__(self, limit, window):
        self.store = {}
        self.limit = limit # save limit in self
        self.window = window # save window window in self

    def allow(self, user_id):
        now = time.time()
        counter = 1
        if user_id not in self.store:
            self.store[user_id] = {"count": counter, "start": now}
            return True
        elif (now - self.store[user_id]["start"]) >= self.window: # window expired; reset entry
            self.store[user_id] = {"count": counter, "start": now}
            return True
        else:
            self.store[user_id]["count"] += 1
            compare = self.store[user_id]["count"] <= self.limit
            return compare

limiter = RateLimiter(5, 10)
for i in range(7):
    time.sleep(11)
    print(limiter.allow("user_4"))

            




