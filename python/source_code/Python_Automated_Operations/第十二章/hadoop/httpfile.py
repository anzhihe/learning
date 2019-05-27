from mrjob.job import MRJob
import re
class MRCounter(MRJob):
    def mapper(self, key, line):
	i=0
        for url in line.split():
	    if i==6:
            	yield url, 1 
	    i+=1

    def reducer(self, url, occurrences):
        yield url, sum(occurrences)


if __name__ == '__main__':
    MRCounter.run()
