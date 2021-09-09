class MyBitmap:
    def __init__(self, size):
        self.words = [0] * (self.get_word_index(size-1) + 1)
        self.size = size

    def get_bit(self, bit_index):
        if bit_index < 0 or bit_index > self.size-1:
            raise Exception("超过bitmap有效范围 !")
        word_index = self.get_word_index(bit_index)
        return (self.words[word_index] & (1 << bit_index)) != 0

    def set_bit(self, bit_index):
        if bit_index < 0 or bit_index > self.size-1:
            raise Exception("超过bitmap有效范围 !")
        word_index = self.get_word_index(bit_index)
        self.words[word_index] |= (1 << bit_index)

    def get_word_index(self, bit_index):
        # 右移6位，相当于除以64
        return bit_index >> 6


bitMap = MyBitmap(21474836470)
bitMap.set_bit(78)
bitMap.set_bit(50)
print(bitMap.get_bit(126))
print(bitMap.get_bit(78))


