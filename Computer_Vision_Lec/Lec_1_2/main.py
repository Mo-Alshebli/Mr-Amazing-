import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the input variables
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')

# Define the output variable
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Define the membership functions for each input and output variable
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['hot'] = fuzz.trimf(temperature.universe, [0, 50, 100])

humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['high'] = fuzz.trimf(humidity.universe, [0, 50, 100])

fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [0, 50, 100])

# Define the rules for the fuzzy system
rule1 = ctrl.Rule(temperature['cold'] & humidity['low'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['cold'] & humidity['high'], fan_speed['high'])
rule3 = ctrl.Rule(temperature['hot'] & humidity['low'], fan_speed['high'])
rule4 = ctrl.Rule(temperature['hot'] & humidity['high'], fan_speed['high'])

# Create the control system
fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

# Define the simulation inputs
temp_input = 20
humid_input = 70

# Create the simulation
fan_sim = ctrl.ControlSystemSimulation(fan_ctrl)

# Set the inputs for the simulation
fan_sim.input['temperature'] = temp_input
fan_sim.input['humidity'] = humid_input

# Run the simulation
fan_sim.compute()

# Print the output
print(fan_sim.output['fan_speed'])