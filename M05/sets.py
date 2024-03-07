print("\033c")
# To close all

# PART 1
# Constructing a Set (there are two methods)
set_1 = {"Toyota", "Daihatsu", "Honda"}
set_2 = {"Toyota", "Daihatsu", "Honda"}

print("Tipe data Set 1 adalah ", type(set_1))
print("Tipe data Set 2 adalah ", type(set_2))
print("Data Set 1: ", set_1)
print("Data Set 2: ", set_2)
print("----------------------------------------------------------------")

# Print every item of set_1
for x in set_1:
    print(x)
print("----------------------------------------------------------------")

# Check the length of the set
print("Length of set_1: ", len(set_1))

# Check if a key exists
if "Daihatsu" in set_1:
    print("Yes, 'Daihatsu' is an item in set_1.")

# Add an item
set_1.add("Mitsubishi")
print(set_1)

# Add multiple items
set_1.update(["Suzuki", "Mazda", "Nissan"])
print(set_1)

# PART 2
# Remove an item (method 1)
set_1.remove("Honda")
print(set_1)

# Remove an item (method 2)
set_1.discard("Mazda")
print(set_1)

#Delet (pop) the last inserted key
set_1.pop()
print(set_1)

#clear the set
set_1.clear()
print(set_1)

#delete the set
del set_1
print("----------------------------------------------------------------")

# Union of two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print("----------------------------------------------------------------")

# Set 1 takes copies of all items of set 2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)