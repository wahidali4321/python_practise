city1 = "PESHAWAR"
city2 = "ISLAMABAD"

print(city1, "City1 length :", len(city1))
print(city2, "City2 length :", len(city2))

if len(city1) > len(city2):
    print(f"{city1} is longer")
elif len(city1) < len(city2):
    print(f"{city2} is longer")
else:
    print("Both cities have the same length.")