# login gaurd systemdesign rep
import time

class LoginGaurd:
    def __init__(self, attempt, window):
        self.store = {}
        self.attempt = attempt
        self.window = window

    def logedUser(self, username, success):
        usertime = time.time()
        counter = 0
        if username not in self.store:
            self.store[username] = {"count": counter, "logintime": None}
        if self.store[username]["logintime"] is not None and usertime - self.store[username]["logintime"] < self.window:
            return "locked"
        elif success:
            self.store[username] = {"count": counter, "logintime": None}
            return "Ok"
        else:
            self.store[username]["count"] += 1
            if self.store[username]["count"] >= self.attempt:
                self.store[username] = {"count": counter, "logintime": usertime}
        return "failed"

guard = LoginGaurd(3, 30)

for g in range(4):
    print(guard.logedUser("a", False))
            

            
