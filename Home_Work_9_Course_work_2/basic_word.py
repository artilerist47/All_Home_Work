class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

        self.user_answer = None

    def word_in_subwords(self):
        return self.user_answer in self.subwords

    def len_words(self):
        return len(self.subwords)
