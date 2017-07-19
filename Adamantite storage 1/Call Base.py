import re

def total_cost(calls):
    total = 0
    daytotal = 0
    day = ""
    def switchday():
        nonlocal daytotal,total
        total += min(daytotal, 100) + max(daytotal-100, 0)*2
        daytotal = 0
        
    for line in calls:
        r = re.match(R"(\d\d\d\d-\d\d-\d\d) \d\d:\d\d:\d\d (\d+)", line)
        if day != r.group(1):
            switchday()
            day = r.group(1)
        daytotal += (int(r.group(2))+59)//60

    switchday()
    return total


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"

    print("All set? Click 'Check' to review your code and earn rewards!")
