class Student(object):
    # ScoreA, ScoreC, ScoreD, ScoreE
    def __init__(self, name):
        self.Name = name
        self.ScoreList = []
        self.ScoreA = []
        self.ScoreC = []
        self.ScoreD = []
        self.ScoreE = []
    
    def AddScore2List(self, score):
        self.ScoreList.append(score)
    
    def AddScoreSum2List(self, score_a, score_c, score_d, score_e):
        self.ScoreA.append(score_a)
        self.ScoreC.append(score_c)
        self.ScoreD.append(score_d)
        self.ScoreE.append(score_e)
    
    def GetFinalScore(self):
        FinalScoreA = 0.0
        FinalScoreC = 0.0       
        FinalScoreE = 0.0
        FinalScoreD = 0.0
        self.ScoreA = sorted(self.ScoreA)
        self.ScoreC = sorted(self.ScoreC)
        self.ScoreD = sorted(self.ScoreD)
        self.ScoreE = sorted(self.ScoreE)
        FinalScoreA = sum(self.ScoreA[1:-1])/(len(self.ScoreA) - 2)
        FinalScoreC = sum(self.ScoreC[1:-1])/(len(self.ScoreC) - 2)
        FinalScoreD = sum(self.ScoreD[1:-1])/(len(self.ScoreD) - 2)
        FinalScoreE = sum(self.ScoreE[1:-1])/(len(self.ScoreE) - 2)
        return [FinalScoreA, FinalScoreC, FinalScoreD, FinalScoreE]

    def __str__(self):
       return "Name: {}  ScoreList: {}".format(self.Name, str(self.GetFinalScore()))
