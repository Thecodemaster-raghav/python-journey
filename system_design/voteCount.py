# vote count 

class VotingBooth:
    def __init__(self):
        self.data = {}
        self.votebank = set() # empty set as a container 

    def vote(self, votername, options):
        votername = votername.lower() # same guard at the door — routes, voting booth." used in Fastapi routes
        options = options.lower()
        if votername not in self.votebank:
            self.votebank.add(votername)
            if options not in self.data: # set the options count to 1 if party not present
                self.data[options] = 1
            else:
                self.data[options] += 1 # else increment the options count
            return "Voted"
        else:
            return "Already Voted"

    def results(self):
        return self.data

voted = VotingBooth()
print(voted.vote("raghav", "party B"))
print(voted.vote("Veena", "party D"))
print(voted.vote("Manoj", "PARTY A"))
print(voted.vote("Keshav", "party D"))
print(voted.vote("Raghav", "party C"))
print(voted.results())