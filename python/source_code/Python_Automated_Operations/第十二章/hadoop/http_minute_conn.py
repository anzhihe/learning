from mrjob.job import MRJob
import re

class MRCounter(MRJob):

    def mapper(self, key, line):
	i=0
        for dt in line.split():
	    if i==3:
		timerow=dt.split(":")
		hm=timerow[1]+":"+timerow[2]
            	yield hm, 1 
	    i+=1

    def reducer(self, key, occurrences):
        yield key, sum(occurrences)


if __name__ == '__main__':
    MRCounter.run()
