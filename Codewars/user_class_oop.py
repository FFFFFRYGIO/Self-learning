# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
    def rank(current_rank):
        return self.rank
    def progress(self):
        return self.progress
    def inc_progress(self, rank):
        if rank > 8 or rank < -8 or rank == 0:
            raise ValueError()
        if self.rank == 8:
            return 0
        #activity-value - difference between ranks
        if self.rank * rank > 0:
            activity_value = rank - self.rank
        else:
            if self.rank > 0:
                activity_value = rank - self.rank + 1
            else:
                activity_value = rank - self.rank - 1
        #score - points that user earned
        if activity_value > 0:
            score = 10 * activity_value * activity_value
        elif activity_value == 0:
            score = 3
        elif activity_value == -1:
            score = 1
        else:
            score = 0
        print(self.rank, rank, activity_value, self.progress, score)
        #updating progress and rank
        self.progress += score
        while self.progress >= 100:
            if self.rank == 7:
                self.rank += 1
                self.progress = 0
            else:
                if self.rank == 8:
                    self.progress = 0
                else:
                    if self.rank == -1:
                        self.rank = 1
                    else:
                        self.rank += 1
                    self.progress -= 100
