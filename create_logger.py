import datetime


class Logger:
    filename = 'log.txt'

    def write(self, message):
        line = str(datetime.datetime.now()) + " " + message + "\n"
        file = open(self.filename, 'a')
        file.write(line)


logger = Logger()