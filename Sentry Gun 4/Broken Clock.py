import re

def broken_clock(starting_time, wrong_time, error_description):
    r = re.match(R'([+-]\d+) (second|minute|hour)s? at (\d+) (second|minute|hour)s?', error_description)
    how = int(r.group(1))
    if r.group(2) == "minute": how *= 60
    elif r.group(2) == "hour": how *= 60*60
    at = int(r.group(3))
    if r.group(4) == "minute": at *= 60
    elif r.group(4) == "hour": at *= 60*60
    speed = (how + at)/at

    def to_seconds(t):
        h,m,s = t.split(":")
        return int(h)*60*60+int(m)*60+int(s)

    incorrect = to_seconds(wrong_time)
    start = to_seconds(starting_time)
    correct = (incorrect-start)/speed+start
    return "{:02g}:{:02g}:{:02g}".format(correct//3600, correct//60%60, int(correct%60))


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
