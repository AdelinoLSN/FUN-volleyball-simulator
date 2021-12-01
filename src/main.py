import random

def getTeamNames():
    team_1 = str(input('Nome do time 1: '))
    team_2 = str(input('Nome do time 2: '))
    return [team_1, team_2]

def fillList(poss, perc):
    lista = []
    for i in range(len(poss)):
        for j in range(perc[i]):
            lista.append(i)
    return lista

def getServeResult():
    possibilities = ['ace', 'out', 'deviation_out', 'receive']
    possibilities_percentual = [10, 5, 15, 60]
    lista = fillList(possibilities, possibilities_percentual)
    r = random.choice(lista)
    return r

def changeBallPossession(ball_possession):
    if (ball_possession == 1):
        return 2
    if (ball_possession == 2):
        return 1

def playCommon(ball_possession):
    possibilities = ['turnover', 'point', 'net', 'out', 'deviation_out', 'block']
    possibilities_percentual = [2, 40, 3, 15, 15, 25]
    lista = fillList(possibilities, possibilities_percentual)
    r = random.choice(lista)
    return r

def doPlayBlock(ball_possession):
    possibilities = ['rebound', 'out', 'point']
    possibilities_percentual = [30, 30, 40]
    lista = fillList(possibilities, possibilities_percentual)
    r = random.choice(lista)
    return r

def playBlock(ball_possession):
    result = doPlayBlock(ball_possession)
    if (result == 1):
        return play(ball_possession)
    if (result == 2):
        return ball_possession
    if (result == 3):
        ball_possession = changeBallPossession(ball_possession)
        return ball_possession

def play(ball_possession):
    result = playCommon(ball_possession)
    if (result == 1 or result == 2 or result == 3):
        ball_possession = changeBallPossession(ball_possession)
        return ball_possession
    if (result == 2 or result == 4):
        return ball_possession
    if (result == 5):
        return playBlock(ball_possession)

def doServe(ball_possession):
    print ("Time "+str(ball_possession)+" saca!")
    serve_result = getServeResult()
    if (serve_result == 0 or serve_result == 2):
        return ball_possession
    if (serve_result == 1):
        ball_possession = changeBallPossession(ball_possession)
        return ball_possession
    if (serve_result == 2):
        return play(ball_possession)


def doPlay(ball_possession):
    result = doServe(ball_possession)
    return result

def playMatch(team_1, team_2):
    team_1_score = 0
    team_2_score = 0
    ball_possession = 1
    while (team_1_score < 25 or team_2_score < 25 or abs(team_1_score - team_2_score) < 2):
        playResult = doPlay(ball_possession)
        if (playResult == 1):
            team_1_score+=1
            ball_possession = 1
        if (playResult == 2):
            team_2_score+=1
            ball_possession = 2
    return (team_1+" "+str(team_1_score)+"x"+str(team_2_score)+" "+team_2)

def main():
    [team_1, team_2] = getTeamNames()
    match_result = playMatch(team_1, team_2)
    print (match_result)

main()