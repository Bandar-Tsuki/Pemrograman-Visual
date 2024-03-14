# Clear the console
print("\033c")

# PART 1
# Constructing a Set (there are two methods)
fruits = {"apel", "jeruk", "mangga"}
food = {"nasi", "ayam", "sate"}
groceries = {"gula", "tepung", "minyak"}

print("WARUNG SETIA SEJAHTERA")
print("Buah yang dijual ada : ", fruits)
print("Makanan yang terdisplay ada : ", food)
print("Disini jual sembako : ", groceries)
print("----------------------------------------------------------------")

# Print every item
print("Buah: ")
for x in fruits:
    print(x)
print("----------------------------------------------------------------")

# Check the length of the set
print("Banyaknya jenis buah yang dijual : ", len(fruits))

# Check if an item exists
if "apel" in fruits:
    print("Iya, apel merupakan salah satu buah yang dijual")

# Add an item
fruits.add("pisang")
print(fruits)

# Add multiple items
fruits.update(["pear", "avocado", "kiwi"])
print(fruits)

# PART 2
# Remove an item (method 1)
fruits.remove("mangga")
print(fruits)

# Remove an item (method 2)
fruits.discard("pear")
print(fruits)

# Delete (pop) the last inserted key
fruits.pop()
print(fruits)

# Clear the set
fruits.clear()
print(fruits)

# Delete the set
del fruits
print("----------------------------------------------------------------")

# Union of two