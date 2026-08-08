a = 12345.678

print(f"2 digits after decimal: {a:.2f}") 
print(f"Giving 15 spaces {a} : {a:15}")
print(f"Giving 15 spaces but with 0 in empty spaces : {a:015}")
print(f"Everything to the left: {a:<10}")
print(f"Everything to the right: {a:>10}")
print(f"Everything to the centre: {a:^10}")
print(f"Gives '+' sign to each positive no. except negetive ones: {a:+}")
print(f"',' at thousand: {a:,}")
print(f"We can use multiple at ones: {a:+20.2f}")