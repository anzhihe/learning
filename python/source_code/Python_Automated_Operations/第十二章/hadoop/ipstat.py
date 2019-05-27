from mrjob.job import MRJob
import re

IP_RE = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

class MRCounter(MRJob):

    def mapper(self, key, line):
        for ip in IP_RE.findall(line):
            yield ip, 1 

    def reducer(self, ip, occurrences):
        yield ip, sum(occurrences)


if __name__ == '__main__':
    MRCounter.run()
