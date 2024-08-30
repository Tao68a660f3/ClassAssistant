from datetime import datetime

def next_gaokao():
    year = datetime.now().year
    thisGaokao = datetime(year,6,7,9,0)
    timeDelta = thisGaokao - datetime.now()
    if timeDelta.days < 0:
        thisGaokao = datetime(year+1,6,7,9,0)
    timeDelta = thisGaokao - datetime.now()
    return timeDelta

if __name__ == "__main__":
    print(next_gaokao())