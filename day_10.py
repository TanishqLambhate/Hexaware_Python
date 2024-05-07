#working across sets
# 1.union
#2. intersection
# 3.Difference(except)

outdoor_activities={"Hiking","Cycling"}
indoor_activities={"Gaming","Reading","Cycling"}

print(outdoor_activities.union(indoor_activities))
print(outdoor_activities.intersection(indoor_activities))
print(outdoor_activities.difference(indoor_activities))
print(outdoor_activities.symmetric_difference(indoor_activities))