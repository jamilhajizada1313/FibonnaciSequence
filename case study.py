# Case Study 1: The Automated Smart Greenhouse 🌿
# The Logic Focus: Nested conditionals (if/elif/else) and boolean logic (and/or).
# The Scenario: Students are writing the control software for a smart greenhouse. The system needs to automatically manage the environment based on two sensor inputs: temperature (in Celsius) and soil_moisture (as a percentage from 0 to 100).
# The Rules:
# If the soil moisture falls below 30%, the system must print "Action: Turn on water pump".
# If the temperature rises above 30°C, it must print "Action: Open ventilation fans".
# If the temperature drops below 10°C, it must print "Action: Turn on heater".
# If the temperature is optimal (between 18°C and 25°C) and the moisture is healthy (above 50%), it must print "Status: Greenhouse environment is perfect"



# STEP 1: Take Temprature From User In Variable Temp
# STEP 2: Take Soil Moisture From User In Variable Soil
# STEP 3: Check Soil Percentage and Temprature... 
    
# Take temperature from the user
temperature = float(input("Enter the temperature: "))

# Take soil moisture percentage from the user
soil_moisture = float(input("Enter the soil moisture: "))


# Check if temperature is greater than 30°C
if temperature > 30:
    print("Open ventilation fans")


# Check if temperature is below 10°C
if temperature < 10:
    print("Turn on heater!")


# Check if temperature is between 18°C and 25°C
# AND soil moisture is greater than or equal to 50%
if temperature >= 18 and temperature <= 25 and soil_moisture >= 50:
    print("Greenhouse environment is perfect")


# Check if soil moisture is greater than or equal to 30%
if soil_moisture >= 30:
    print("Turn on water pump")

# If soil moisture is below 30%
else:
    print("Environment needs adjustment!")

