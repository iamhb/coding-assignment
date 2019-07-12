import data2
outputTeam=[] #declaration of return value

def get_members(team):

    memberAccess(team)
    return outputTeam # return after all recursion

def memberAccess(peopleTeam):  

        for person in peopleTeam.members:

            if(person.is_team):
                memberAccess(person)

            else:
                outputTeam.append(person)

print sorted(p.displayname for p in get_members(data2.c_team))