


import pandas as pd
import sqlite3



conn = sqlite3.connect('lahman2016.sqlite')



# Querying Database for all seasons where a team played 150 or more games and is still active today.

query = '''select * from Teams 
inner join TeamsFranchises
on Teams.franchID == TeamsFranchises.franchID
where Teams.G >= 150 and TeamsFranchises.active == 'Y';
'''

# Creating dataframe from query.

Teams = conn.execute(query).fetchall()


teams_df = pd.DataFrame(Teams)

print(teams_df.head())



# adding column names to dataframe

cols = ['yearID','lgID','teamID','franchID','divID','Rank','G','Ghome','W','L','DivWin','WCWin','LgWin','WSWin','R','AB','H','2B','3B','HR','BB','SO','SB','CS','HBP','SF','RA','ER','ERA','CG','SHO','SV','IPouts','HA','HRA','BBA','SOA','E','DP','FP','name','park','attendance','BPF','PPF','teamIDBR','teamIDlahman45','teamIDretro','franchID','franchName','active','NAassoc']

teams_df.columns = cols

print(teams_df.head())

print(len(teams_df))



