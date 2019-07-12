import data2
outputTeam=[]

def exercise1(givenName, people):

    for peopleTeam in people:

        if(peopleTeam.is_team): # only teams
            memberAccess(peopleTeam,givenName) 

    return list(set(outputTeam))   

def memberAccess(peopleTeam,givenName):

        for person in peopleTeam.members:

            if(person.is_team): # if team, calling memberAccess recursively
                if memberAccess(person,givenName):
                    outputTeam.append(peopleTeam)
                    
            else: #if not a team
                if person.displayname == givenName.displayname:
                    outputTeam.append(peopleTeam)
                    return 1

print [t.displayname for t in exercise1(data2.alice, data2.people)]