recent_purchase = [36.13, 23.87, 183.35, 22.93, 11.62]

budget = 150
total_spent = 0

for purchase in recent_purchase:
    total_spent += purchase
    if total_spent > budget:
        print("This purchase is over budget: ", purchase)
    else:
        print("This purchase is within budget: ", purchase)

def check_budget(recent_purchased, budget):
    for purchase in recent_purchased:
        if purchase > budget:
            print(f"{purchase}: This purchase is over budget.")
        else:
            print(f"{purchase}: This purchase is within budget.")
 #---- Test cases
check_budget ([36.12,23.87,183.35,22.93, 11.62], 150)   
check_budget ([10, 20,  30],25)
check_budget ([100, 200, 300], 250)