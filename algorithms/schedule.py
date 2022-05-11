class Schedule_ob:
    day = ""
    activities = []
    def __init__(self, day, activities):
        self.day = day
        self.activities = activities
    def print_day(self):
        print(self.day)
    def return_activ(self):
        return self.activities

def return_schedule():
    file = open("schedule.txt", 'rb')
    line = file.readline().decode('utf-8')
    result = []
    activities = []
    while (line):
        day = line
        length = int(file.readline().decode('utf-8'))
        if (length):
            for i in range(length):
                line = file.readline().decode('utf-8')
                activities.append(line)
            result.append(Schedule_ob(day, activities))
        activities = []
        line = file.readline().decode('utf-8')
    return result