from mrjob.job import MRJob
import re
class MRCounter(MRJob):
    def mapper(self, key, line):
	i=0
        for httpcode in line.split():
	    if i==8 and re.match(r"\d{1,3}",httpcode):
            	yield httpcode, 1 
	    i+=1

    def reducer(self, httpcode, occurrences):
        yield httpcode, sum(occurrences)

    def reducer_sorted(self, httpcode, occurrences):
	yield httpcode, sorted(occurrences)

    def steps(self):
        return [self.mr(mapper=self.mapper),
                self.mr(reducer=self.reducer)]

if __name__ == '__main__':
    MRCounter.run()
