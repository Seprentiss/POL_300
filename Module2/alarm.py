
"""
TODO
    Given a day of the week encoded as 1=Mon, 2=Tue, ...7=Sun, and a boolean indicating if we are on vacation,
    return a string of the form "7:00" indicating when the alarm clock should ring.
    Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
    Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

    You will be given two parameters day_of_week. This tells you what the day of the week is 1-7.
    on_Vaction is a boolean that tells you whether the person is on vacation or not (True or False).

"""
def alarm(day_of_week, on_Vaction):
    if (on_Vaction):
        if(day_of_week > 5):
            return "off"
        else:
            return "10:00"
    else:
        if(day_of_week > 5):
            return "10:00"
        else:
            return "7:00"

print (alarm(6,True))


