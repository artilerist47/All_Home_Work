class Player:
    def __init__(self, user_name):
        self.user_name = user_name

        self.used_words = []
        self.help_words = []
        self.user_answer = None


class OneUsers(Player):
    def len_player_words(self):
        return len(self.used_words)

    def len_help_words_one_players(self):
        return len(self.help_words)

    def append_user_words(self):
        return self.used_words.append(self.user_answer)


class AllUsers(Player):
    def len_all_players_words(self):
        return len(self.used_words)

    def len_help_words_all_players(self):
        return len(self.help_words)

    def append_words_all_users(self):
        return self.used_words.append(self.user_answer)

    def check_all_used_words(self):
        return self.user_answer in self.used_words

    def check_all_words_help(self):
        return self.user_answer in self.help_words