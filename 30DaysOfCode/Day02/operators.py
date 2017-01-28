# Given the meal price (base cost of a meal), tip percent (the percentage of
# the meal price being added as tip), and tax percent (the percentage of the
# meal price being added as tax) for a meal,
# find and print the meal's total cost.

mealCost = raw_input()
tipPercent = raw_input()
taxPercent = raw_input()

floatCost = float(mealCost)

tip = int(tipPercent)  # / 100
tax = int(taxPercent)  # // 100

totalTip = floatCost / 100 * tip
totalTax = floatCost / 100 * tax

totalCost = float(mealCost) + totalTip + totalTax

print "The total meal cost is", int(round(totalCost)), "dollars."
