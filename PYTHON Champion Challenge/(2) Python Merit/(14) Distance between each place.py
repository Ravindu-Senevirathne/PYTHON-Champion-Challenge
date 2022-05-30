Distance_to_well = 100
Distance_to_lake = 300
Distance_to_river = 1200

# Add because distance is from lake
River_distance = Distance_to_river + Distance_to_lake

# Multiply by 2 because they've to go and come
Distance_to_well = 2 * Distance_to_well
Distance_to_lake = 2 * Distance_to_lake
River_distance = 2 * River_distance

Total_distance = (Distance_to_well + Distance_to_lake + River_distance) / 1000

print("Total distance they've to travel is : ", Total_distance * 3, "km")
