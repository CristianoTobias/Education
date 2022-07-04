weight = 4.8
cost_ground_premium = 125.00
#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
  # more calculation
  cost_ground = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  # more calculation
  cost_ground = weight * 4.00 + 20
else:
  # last calculation
  cost_ground = weight * 4.75 + 20
print("Ground Shipping $ %.2f" % cost_ground)
print("Ground Shipping Premium $ %.2f" % cost_ground_premium)
#Drone Shipping
if weight <= 2:
  cost_ground = weight * 4.50
elif weight > 2 and weight <= 6:
  # more calculation
  cost_ground = weight * 9.00
elif weight > 6 and weight <= 10:
  # more calculation
  cost_ground = weight * 12.00
else:
  # last calculation
  cost_ground = weight * 14.25
print("Drone Shipping $ %.2f" % cost_ground)
