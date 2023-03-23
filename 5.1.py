import random

class T2Cup:
    allTeams = []
    def entry_team(self, teamObj):
        self.allTeams.append(teamObj)

class Team(T2Cup):
    def __init__(self, name):
        self.teamName = name
        self.playersListOfObj = []
        super().entry_team(self)
    def entry_player(self, player):
        self.playersListOfObj.append(player)
    def __repr__(self):
        return f"Team name: {self.teamName}"

class Player:
    def __init__(self, name, teamObj):
        self.playerName = name
        self.strikeRate = 0.0
        self.runBat = 0
        self.ballUsed = 0
        self.fours = 0
        self.sixes = 0
        self.runBowl = 0
        self.wicketTaken = 0
        self.ballsBowled = 0
        teamObj.playersListOfObj.append(self)
    def __repr__(self):
        return f"Name: {self.playerName}"

class Innings:
    def __init__(self, team1, team2, battingTeam, bowlingTeam):
        self.teamOneObj = team1
        self.teamTwoObj = team2
        self.battingTeam = battingTeam
        self.bowlingTeam = bowlingTeam
        self.totalRun = 0
        self.totalWickets = 0
        self.totalOver = 0
        self.currentBall = 0
        self.currentBatsmanOrder = 2
        self.currentBattingList = [battingTeam.playersListOfObj[0], battingTeam.playersListOfObj[1]]
        self.striker = battingTeam.playersListOfObj[0]
        self.currentBowler = None
        self.currentOverStatus = []
        self.allOverStatus = []
        self.target = None
    def show_score_board(self):
        print(f"*{self.currentBattingList[0].playerName} - {self.currentBattingList[0].runBat}({self.currentBattingList[0].ballUsed})", end="\t")
        print(f"{self.currentBattingList[1].playerName} - {self.currentBattingList[1].runBat}({self.currentBattingList[1].ballUsed})")
        print(f"{battingTeamObj.teamName[:3].upper()} | {self.totalRun}-{self.totalWickets}")
        print(f"Overs: {self.totalOver}.{self.currentBall}")
        if self.currentBowler is not None:
            print(f"{self.currentBowler.playerName} - {self.currentBowler.runBowl}/{self.currentBowler.wicketTaken}")
        if self.currentBall>0:
            print("Current over- ", end="")
            for i in self.currentOverStatus:
                print(i, end=" ")
            print()
        if self.currentBall==0 and self.totalOver > 0:
            print("Last over- ", end="")
            for i in self.allOverStatus[-1]:
                print(i, end=" ")
            print()
        if self.target is not None:
            print(f"Target - {self.target}")
            print(f"Need {self.target - self.totalRun} runs in {12 - (self.totalOver*6 + self.currentBall)}")
    def set_bowler(self, bowlerObj):
        self.currentBowler = bowlerObj
    def bowl(self, status):
        run = 0
        extraRun = 0
        isNoBall = False
        isWide = False
        willStrikeChange = False
        isWicketDown = False
        if status[0] > '0' and status[0] < '9':
            run = int(status)
            if run % 2 == 1:
                willStrikeChange = True
        else:
            if status[0] == 'W' and len(status) == 1:
                isWicketDown = True
            elif status[0] == 'N':
                isNoBall = True
                extraRun = 1
                run = int(status[1])
                if run % 2 == 1:
                    willStrikeChange = True
            elif status[0] == 'W':
                isWide = True
                extraRun = 1 + int(status[1])
                if int(status[1]) % 2 == 1:
                    willStrikeChange = True

        self.totalRun += run + extraRun
        if self.target is not None:
            if self.totalRun >= self.target:
                return "end"
        self.striker.runBat += run
        if run == 4:
            self.striker.fours += 1
        if run == 6:
            self.striker.sixes +=1
        if isWide == False:
            self.striker.ballUsed += 1
        self.currentBowler.runBowl += run+extraRun

        self.currentOverStatus.append(status)
        if isNoBall == False and isWide == False:
            self.currentBowler.ballsBowled += 1
            self.currentBall += 1
            if self.currentBall == 6:
                self.currentBall = 0
                self.totalOver += 1
                willStrikeChange = True
                self.allOverStatus.append(self.currentOverStatus)
                self.currentOverStatus = []

        if isWicketDown == True:
            if self.totalWickets == 1:
                return "end"
            print()
            print(f"{self.striker.playerName}\t{self.striker.runBat}/{self.striker.ballUsed}")
            print(f"Strike rate - {self.striker.runBat*100/self.striker.ballUsed}")
            print(f"4's-{self.striker.fours}\t6's-{self.striker.sixes}")
            self.currentBattingList[0] = self.battingTeam.playersListOfObj[self.currentBatsmanOrder]
            print()
            self.currentBatsmanOrder += 1
            self.striker = self.currentBattingList[0]
            self.totalWickets+=1
            self.currentBowler.wicketTaken += 1
        if willStrikeChange == True:
            self.currentBattingList[0], self.currentBattingList[1] = self.currentBattingList[1], self.currentBattingList[0]
            self.striker = self.currentBattingList[0]
        return ""
        

cup = T2Cup()
bangladesh = Team("Bangladesh")
india = Team("India")
tamim = Player("Tamim Iqbal", bangladesh)
sakib = Player("Shakib Al Hasan", bangladesh)
mustafiz = Player("Mustafizur Rahman", bangladesh)
kohli = Player("Virat Kohli", india)
rohit = Player("Rohit Sharma", india)
bumra = Player("Bumra", india)

while True:
    print("Select teams to be played")
    for i, val in enumerate(cup.allTeams):
        print(f"{i+1}. {val.teamName}")
    teamOneIndex, teamTwoIndex = map(int, input("Enter tow team index: ").split(" "))
    teamOneIndex -= 1
    teamTwoIndex -= 1
    teamOneObj = cup.allTeams[teamOneIndex]
    teamTwoObj = cup.allTeams[teamTwoIndex]
    tossWin = random.choice([teamOneIndex, teamTwoIndex])
    print(f"{cup.allTeams[tossWin].teamName} team wins the toss")
    if tossWin==teamOneIndex:
        tossLose = teamTwoIndex
    else:
        tossLose = teamTwoIndex
    rand = random.choice([0,1])
    if rand == 0:
        print(f"{cup.allTeams[tossWin].teamName} choose bowling" )
        battingTeamObj = cup.allTeams[tossLose]
        bowlingTeamObj = cup.allTeams[tossWin]
    else:
        print(f"{cup.allTeams[tossWin].teamName} choose batting" )
        battingTeamObj = cup.allTeams[tossWin]
        bowlingTeamObj = cup.allTeams[tossLose]
    firstInnings = Innings(teamOneObj, teamTwoIndex, battingTeamObj, bowlingTeamObj)
    firstInnings.show_score_board()

    over = 0
    while over<2:
        off =False
        print("Choose bowler: ")
        for i, val in enumerate(bowlingTeamObj.playersListOfObj):
            print(f"{i+1}. {val.playerName}")
        bowlerIndex = int(input("Enter bowler index: "))
        bowlerIndex -= 1
        bowlerObj = bowlingTeamObj.playersListOfObj[bowlerIndex]
        firstInnings.set_bowler(bowlerObj)


        while True:
            status = input("Enter Status: ")
            rcv = firstInnings.bowl(status)
            if rcv == "end":
                off = True
                break
            firstInnings.show_score_board()
            if (firstInnings.totalOver * 6 + firstInnings.currentBall) % 6 == 0:
                break
        over+=1
        if off == True:
            break
    print(f"Target is {firstInnings.totalRun+1}")
    
    battingTeamObj, bowlingTeamObj = bowlingTeamObj, battingTeamObj
    secondInnings = Innings(teamOneObj, teamTwoIndex, battingTeamObj, bowlingTeamObj)
    secondInnings.target = firstInnings.totalRun + 1

    over = 0
    while over<2:
        off =False
        print("Choose bowler: ")
        for i, val in enumerate(bowlingTeamObj.playersListOfObj):
            print(f"{i+1}. {val.playerName}")
        bowlerIndex = int(input("Enter bowler index: "))
        bowlerIndex -= 1
        bowlerObj = bowlingTeamObj.playersListOfObj[bowlerIndex]
        secondInnings.set_bowler(bowlerObj)


        while True:
            status = input("Enter Status: ")
            rcv = secondInnings.bowl(status)
            if rcv == "end":
                off = True
                break
            secondInnings.show_score_board()
            if (secondInnings.totalOver * 6 + secondInnings.currentBall) % 6 == 0:
                break
        over+=1
        if off == True:
            break
    if secondInnings.totalRun == secondInnings.target:
        print(f"{secondInnings.battingTeam.teamName} wins")
    else:
        print(f"{secondInnings.bowlingTeam.teamName} wins")

    break
# print(bangladesh.playersListOfObj)
# for obj in bangladesh.playersListOfObj:
#     print(obj.playerName)
