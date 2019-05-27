from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

class MRWordCounter(MRJob):

    def mapper(self, key, line):
	user_id  = line.split()[0]
	timestamp =line.split()[1].split(',')
	yield user_id, timestamp

    def reducer(self, uid, timestamps):
	for b in timestamps:	
		yield uid, max(b)

if __name__ == '__main__':
    MRWordCounter.run()
