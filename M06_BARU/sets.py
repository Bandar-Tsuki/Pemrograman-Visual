print("Case 5")

# PART_1
# Constructing a Set (there are two methods)
set_1 = {"Toyota", "Daihatsu", "Honda"}
set_2 = {"Toyota", "Daihatsu", "Honda"}

print("Tipe data Set_1 adalah", type(set_1))
print("Tipe data Set_2 adalah", type(set_2))
print("Data Set_1:", set_1)
print("Data Set_2:", set_2)

# Print every item of set_2
for x in set_2:
    print(x)

print("--------------------------------------")

# Check the length of the set
print(len(set_1))

# Check if key exist
if "Daihatsu" in set_1:
    print("Yes, 'Daihatsu' is an item in set_1.")

# Add an item
set_1.add("Mitsubishi")
print(set_1)

# Add multiple items
set_1.update(["Suzuki", "Mazda", "Nissan"])
print(set_1)


# PART_2
# Remove an item (method 1)
set_1.remove("Honda")
print(set_1)

# Remove an item (method 2)
set_1.discard("Mazda")
print(set_1)

# Remove (pop the last inserted key)
set_1.pop()
print(set_1)

# Clear the set
set_1.clear()
print(set_1)

# Delete the set
del set_1

print("--------------------------------------")

# Union (or "gabung")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Make true copies of all items of set 2
set4 = set2.copy()
print("Set 4:", set4)
