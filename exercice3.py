
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = int(secondes / 31540000)
    secondes = secondes - (annees * 31540000)

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = int(secondes / 604800)
    secondes = secondes - (semaines * 604800)

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = int(secondes / 86400)
    secondes = secondes - (jours * 86400)

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = int(secondes / 3600)
    secondes = secondes - (heures * 3600)

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = int(secondes / 60)

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = secondes - (minutes * 60)

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
