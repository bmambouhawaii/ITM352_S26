health = 100

while health > 0:
    print(f"Current health: {health}")
    damage = int(input("Enter damage taken: "))
    health -= damage

    print("I'm in the loop")

    if health <= 0:
        print("Game Over!")