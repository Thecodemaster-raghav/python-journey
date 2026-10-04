import time

fake_db = {"user1": "Raghav",
           "user2": "Manoj",
           }

def fetch_from_db(key):
    time.sleep(1)
    if key in fake_db:
        return fake_db[key]
    else:
        return None

class Cache:
    def __init__(self, ttl):
        self.cache = {}
        self.ttl = ttl
        self.hits = 0
        self.misses = 0

    def get(self, key):
        now = time.time()
        # remove the key if in cache but expired
        if key in self.cache and now > self.cache[key]["expiry"]:
            del self.cache[key]
        # if key in cache return the cache value
        if key in self.cache:
            self.hits += 1
            return self.cache[key]["value"]
        self.misses += 1 # the values if not in cache returned from db itself
        value = fetch_from_db(key)
        # values if not None stores the expiry and return the value for the key
        if value is not None:
            expires_at = now + self.ttl
            self.cache[key] = {"value": value, "expiry": expires_at}
        return value
    

cache = Cache(ttl=2)
cache.get("user1")
time.sleep(3)
cache.get("user1")
print(cache.hits)
print(cache.misses)