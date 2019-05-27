from mrjob.job import MRJob
import re

class MRWordCounter(MRJob):

    def mapper(self, key, line):
	i=0
        for flow in line.split():
	    if i==3:
		timerow=flow.split(":")
		hm=timerow[1]+":"+timerow[2]
	    if i==9 and re.match(r"\d{1,}",flow):
            	yield hm, int(flow) 
	    i+=1

    def reducer(self, key, occurrences):
        yield key, sum(occurrences)


if __name__ == '__main__':
    MRWordCounter.run()
