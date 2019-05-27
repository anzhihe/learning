from mrjob.job import MRJob


class MRWordCounter(MRJob):

    def mapper(self, key, line):
        timestamp, user_id = line.split()
        yield user_id, timestamp

    def reducer(self, uid, timestamps):
	print sorted(timestamps)
        yield uid, sorted(timestamps)


if __name__ == '__main__':
    MRWordCounter.run()
