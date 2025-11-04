# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.
starting_fuel_level = 0
astronauts_abroard = 0
altitude_shuttle_reaches = 0

# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 
while starting_fuel_level > 30000 or starting_fuel_level <= 5000:
    starting_fuel_level = int(input("Enter starting fuel level: "))  

# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
while astronauts_abroard > 7 or astronauts_abroard <= 0:
  astronauts_abroard = int(input("Enter # of astronaunts aboard: "))
  if astronauts_abroard > 7 or astronauts_abroard <= 0:
     print("Choose a number between 1 - 7")
  
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.
while starting_fuel_level-100*astronauts_abroard >=0 :
   altitude_shuttle_reaches += 50
   starting_fuel_level -= 100*astronauts_abroard
   


# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”
if altitude_shuttle_reaches >= 2000:
   ending = "Orbit achieved"
else:
   ending = "Failted to Orbit"
print("The shuttle gained an altitude of ", altitude_shuttle_reaches," km and has ", starting_fuel_level," kg of fuel left.", ending)
