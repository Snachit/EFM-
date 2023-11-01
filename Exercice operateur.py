def calculate_cost(duration):
    offers = [
        {"abonnement": 200, "minutes_gratuites": float('inf'), "cost_per_minute": 0},
        {"abonnement": 100, "minutes_gratuites": 120, "cost_per_minute": 0.5},
        {"abonnement": 50, "minutes_gratuites": 60, "cost_per_minute": 1},
        {"abonnement": 20, "minutes_gratuites": 30, "cost_per_minute": 1.5},
        {"abonnement": 0, "minutes_gratuites": 0, "cost_per_minute": 2}
    ]

    costs = []
    for offer in offers:
        total_cost = offer["abonnement"]
        if duration > offer["minutes_gratuites"]:
            total_cost += (duration - offer["minutes_gratuites"]) * offer["cost_per_minute"]
        costs.append(total_cost)

    return costs
def display_menu():
    print("1- Saisir la durée de communication")
    print("2- Afficher la liste du coût mensuel par offre")
    print("3- Afficher l’offre la plus intéressante (moindre coût)")
    print("4- Quitter le programme")
communication_duration = 0
while True:
    display_menu()
    choice = int(input("Entrez votre choix : "))

    if choice == 1:
        communication_duration = int(input("Entrez la durée de communication du mois en minutes : "))
    elif choice == 2:
        if communication_duration != 0:
            monthly_costs = calculate_cost(communication_duration)
            print("Coût mensuel par offre:", monthly_costs)
        else:
            print("Veuillez d'abord saisir la durée de communication.")
    elif choice == 3:
        if communication_duration != 0:
            monthly_costs = calculate_cost(communication_duration)
            min_cost = min(monthly_costs)
            index = monthly_costs.index(min_cost)
            print(f"L'offre la plus intéressante est l'offre {index + 1} avec un coût de {min_cost} DH")
        else:
            print("Veuillez d'abord saisir la durée de communication.")
    elif choice == 4:
        print("Programme quitté.")
        break
    else:
        print("Choix invalide. Veuillez entrer un choix valide.")