def clock_angle(time):
    hours = int(time[:2]) % 12
    mins = int(time[-2:])

    degHours = 0.5 * (60 * hours + mins)
    degMins = mins * 6

    return min((360 - abs(degHours - degMins)), abs(degHours - degMins))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
