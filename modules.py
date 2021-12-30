# two ways to import modules
import converters
from converters import lbs_to_kg

# My weight in kilos
print(f"My weight in pounds is: {converters.kg_to_lbs(75)}")

# My weight in pounds
print(f"My weight in kilos is: {lbs_to_kg(165)}")
