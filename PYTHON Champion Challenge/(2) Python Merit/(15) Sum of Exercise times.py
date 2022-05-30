weeks = 2

# Lady Crow
Lady_crow_mins = 20
Lady_crow_days = 3
Lady_crow_per_week = Lady_crow_days * Lady_crow_mins
Lady_crow_two_weeks = weeks * Lady_crow_per_week

# Lord Crow
Lord_crow_mins = 25
Lord_crow_days = 4
Lord_crow_per_week = Lord_crow_days * Lord_crow_mins
Lord_crow_two_weeks = weeks * Lord_crow_per_week

# Daughter Crow
Daughter_crow_mins = 15
Daughter_crow_days = 5
Daughter_crow_per_week = Daughter_crow_days * Daughter_crow_mins
Daughter_crow_two_weeks = weeks * Daughter_crow_per_week

# Master Crow
Master_crow_mins = 30
Master_crow_days = 6
Master_crow_per_week = Master_crow_days * Master_crow_mins
Master_crow_two_weeks = weeks * Master_crow_per_week

Total_time = Lady_crow_two_weeks + Lord_crow_two_weeks + Daughter_crow_two_weeks + Master_crow_two_weeks

print("They all do exercises", Total_time, "minutes")
