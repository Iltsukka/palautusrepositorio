class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""

        if self.game_is_tied():
            score = self.return_tied_score(self.m_score1)

        elif self.someone_wins_or_has_advantage():
            score = self.return_advantage_or_winning_score()
        else:
            score = self.return_score()

        return score
    
    def game_is_tied(self):
        return self.m_score1 == self.m_score2
    
    def return_tied_score(self, score):
        match score:
            case 0:
                return "Love-All"
            case 1:
                return "Fifteen-All"
            case 2:
                return "Thirty-All"
            case _:
                return "Deuce"
        
    def someone_wins_or_has_advantage(self):
        return self.m_score1 >= 4 or self.m_score2 >= 4
    
    def return_advantage_or_winning_score(self):
        minus_result = self.m_score1 - self.m_score2

        match minus_result:
            
            case 1:
                return 'Advantage player1'
            
            case -1:
                return 'Advantage player2'
            
            case _ if minus_result >= 2:
                return 'Win for player1'
            
            case _:
                return 'Win for player2'
    
    def return_score(self):
        score = ''
        for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"
        
        return score