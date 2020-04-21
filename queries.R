

q_teams <- "SELECT yearID, lgID, teamID, name, divID, teamRank, WSWin, attendance FROM teams WHERE yearID >= 1985;"


q_salaries <- "SELECT * FROM salaries;"


q_postseason <- "SELECT * FROM seriespost WHERE round = 'WS' AND yearID >= 1985;"

