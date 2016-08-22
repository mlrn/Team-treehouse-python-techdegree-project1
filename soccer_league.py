import csv
def read_data():
    with open("soccer_players.csv", newline="") as soccer:
        soccerReader = csv.DictReader(soccer, delimiter=",")
        playersDict = list(soccerReader)
    return playersDict    
 
def create_teams(players):
    experienced_players = []
    non_experienced_players = []
    for player in players:
        if player["Soccer Experience"] == "YES":
            experienced_players.append(player)
        else:
            non_experienced_players.append(player)
    
    total_experienced = len(experienced_players)
    total_non_experienced = len(non_experienced_players)
    teams = [[],[], []]
    while len(experienced_players) > 0:
        for team in teams:
            for i in range(int(total_experienced / 3)):
                team.append(experienced_players.pop())
                   
    while len(non_experienced_players) > 0:
        for team in teams:
            for j in range(int(total_non_experienced / 3)):
                team.append(non_experienced_players.pop())
    
    Dragons = teams[0]
    Sharks = teams[1]
    Raptors = teams[2]            
                
    return teams, Dragons, Sharks, Raptors
    
def write_letter(teams):    
    for player in teams[0]:
        with open("_".join(player["Name"].split( )) + ".txt", "w") as file:
            file.write("Dear Reader,\n")            
            file.write("On behalf of this year childrens soccer league association, we inform you that ")
            file.write("{Name} player, whose guardians are {Guardian Name(s)}, has been assigned to team Dragons.\n".format(**player))
            file.write("The team practice date is March 17 at 1 pm.\n")
            file.write("See you then!")
    
    for player in teams[1]:    
        with open("_".join(player["Name"].split( )) + ".txt", "w") as file:
            file.write("Dear Reader,\n") 
            file.write("On behalf of this year childrens soccer league association, we inform you that ")
            file.write("{Name}, whose guardians are {Guardian Name(s)}, has been assigned to team Sharks.\n".format(**player))
            file.write("The team practice date is March 17 at 3 pm.\n")
            file.write("See you then!")
        
    for player in teams[2]:         
        with open("_".join(player["Name"].split( )) + ".txt", "w") as file:
            file.write("Dear Reader,\n") 
            file.write("On behalf of this year childrens soccer league association, we inform you that ")
            file.write("{Name}, whose guardians are {Guardian Name(s)}, has been assigned to team Raptors.\n".format(**player))
            file.write("The team practice date is March 18 at 1 pm.\n")
            file.write("See you then!")

    return None    

if __name__=="__main__":
    teams=create_teams(read_data())    
    write_letter(teams[0])
        