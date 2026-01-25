
# Prompt user for input
kw_hours = int(input("Enter the KW hours used: "))

# Rates in cents
rate_first = 7.633
rate_over = 9.259

# Calculate amount owed
if kw_hours <= 1000:
    amount_cents = kw_hours * rate_first
else:
    amount_cents = (1000 * rate_first) + ((kw_hours - 1000) * rate_over)

# Convert cents to dollars
amount_dollars = amount_cents / 100

# Output result
print("Amount owed is $", amount_dollars)
