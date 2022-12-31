class Flower:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.quantity})"

class Bouquet:
    def __init__(self, name, flowers):
        self.name = name
        self.flowers = flowers

    def __str__(self):
        return self.name

# Create some flower objects
roses = Flower("Roses", 10, 50)
lilies = Flower("Lilies", 5, 40)
tulips = Flower("Tulips", 7, 30)

# Create a bouquet object with the flowers
bouquet = Bouquet("Spring Bouquet", [roses, lilies, tulips])

# Print the bouquet
print(bouquet)

# Print the flowers in the bouquet
for flower in bouquet.flowers:
    print(flower)

# Check if we need to order more of a particular flower
if roses.quantity < 20:
    print("We need to order more roses!")
