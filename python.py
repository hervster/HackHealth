import datetime

class BottleStorage:

    def __init__(self):
        self.map = {}

    def addBaby(self, baby):
        self.map[baby] = baby.bottles

    def addBottle(self, bottle):
        self.map[bottle.baby].append(bottle)
        self.map[bottle.baby].sort().reverse()
                
                

class Baby:
    def __init__(self, name, crib, bottles=[], timeLastFed=None):
        self.name = name
        self.crib = crib
        self.bottles = bottles # sorted list by time (age) in descending order (oldest is first)
        # convert input list with year, month, day, hour, minute into a datetime
        self.timeLastFed = datetime.datetime(timeLastFed[0], timeLastFed[1], timeLastFed[2], timeLastFed[3], timeLastFed[4])

    def timeToEpoch(self, dateTime):
        return (dateTime - datetime.datetime(1970,1,1)).total_seconds()

    def timeBeforeNextBottle(self):
        """returns seconds left before next bottle must be given to baby"""
        now = datetime.datetime.now()
        timeElapsed = self.timeToEpoch(now) - self.timeToEpoch(self.timeLastFed)
        return 10800 - timeElapsed
         
    def getNextBottle(self):
        """returns oldest bottle in bottles list"""
        return self.bottles[0]

    def removeBottle(self, bottle):
        """called every time bottle expires or is used"""
        self.bottles.remove(bottle)

class Bottle:
    def __init__(self, timeProduced, storageMethod, thawed=None, timeThawed=None):
        self.timeProduced = datetime.datetime(timeProduced[0], timeProduced[1], timeProduced[2], timeProduced[3], timeProduced[4])
        self.storageMethod = storageMethod
        self.thawed = thawed
        self.timeThawed = datetime.datetime(timeThawed[0], timeThawed[1], timeThawed[2], timeThawed[3], timeThawed[4])

    def timeToEpoch(self, dateTime):
        return (dateTime - datetime.datetime(1970,1,1)).total_seconds()

    def setThawed(self, true):
        self.thawed = True

    def totalTime(self):
        """Returns total time a bottle can be stored based on storage method"""
        if self.storageMethod == "fresh":
            return 14400 # 4 hrs
        elif self.storageMethod == "refrigerated":
            return 43200 # 12 hrs
        elif self.storageMethod == "frozen":
            if self.thawed:
                # if thawed in fridge:
                return 86400 # 24 hrs
                # if thawed at room temp:
                # return 7200 # 2 hrs
            else:
                return 31536000 # 12 months
        else:
            return None # raise exception?

    def timeLeftBeforeExp(self): # displayed, needs to update every minute
        """Returns time in seconds left before expiration"""
        if self.thawed:
            expTime = self.timeToEpoch(self.timeThawed) + self.totalTime()
            return expTime - datetime.datetime.now()
        expTime = self.timeToEpoch(self.timeProduced) + self.totalTime()
        return expTime - datetime.datetime.now()

if __name__ == "__main__":
    bottleStorage = BottleStorage()

    while True:
        for baby in bottleStorage.map:
            timeLeft = baby.timeBeforeNextBottle()
            # display str(datetime.timedelta(seconds=timeBeforeNextBottle()))
            if timeLeft > 7200: #if more than 2 hrs left
                # green
                pass
            elif timeLeft <= 0: #if 3 hrs have passed
                #alert
                pass
            elif timeLeft <= 3600: #if 0-1 hr left
                #red
                pass
            else: #if btwn 1-2 hrs left
                #yellow
                pass
            for bottle in baby.bottles:
                # display str(datetime.timedelta(seconds=timeLeftBeforeExp()))
                # if expired, remove bottle from list
                if bottle.timeLeftBeforeExp() <= 0:
                    baby.removeBottle(bottle)