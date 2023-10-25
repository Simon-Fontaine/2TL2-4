import time
import random


class Nourriture:
    def __init__(self, quantite_initiale):
        self.quantite = quantite_initiale

    def retirer_quantite(self, quantite):
        if self.quantite >= quantite:
            self.quantite -= quantite  # pour éviter d'avoir une quantité négative
        else:
            self.quantite = 0


class Fourmi:
    def __init__(self):
        self.est_vivante = True
        self.age = 0
        self.age_max = 14

    def grandir(self):
        if self.est_vivante:
            self.age += 1
            if self.age >= self.age_max:
                self.mourir()

    def manger(self, nourriture):
        if self.est_vivante:
            if nourriture.quantite > 0:
                nourriture.retirer_quantite(1)
            else:
                self.mourir()

    def mourir(self):
        self.est_vivante = False


class Oeuf:
    def __init__(self):
        self.age = 0
        self.est_eclos = False

    def grandir(self):
        self.age += 1
        if self.age >= 3 and random.random() < 0.8:  # 80% de chance d'éclore
            self.est_eclos = True
            return Fourmi()
        return None


class Reine(Fourmi):
    def __init__(self):
        super().__init__()
        self.age_max = 56
        self.taux_oeufs = 10

    def pondre_oeufs(self):
        if self.est_vivante:
            return [Oeuf() for _ in range(self.taux_oeufs)]
        return []


class Colonie:
    def __init__(self, quantite_fourmis_initiale, quantite_nourriture):
        self.fourmis = [Fourmi() for _ in range(quantite_fourmis_initiale)]
        self.oeufs = []
        self.reine = Reine()
        self.nourriture = Nourriture(quantite_nourriture)
        self.jour = 0
        self.quantite_fourmis_initiale = (
            quantite_fourmis_initiale + 1
        )  # on ajoute la reine

    @property
    def quantite_fourmis(self):
        return len(self.fourmis) + self.reine.est_vivante

    @property
    def quantite_fourmis_mortes(self):
        total_fourmis = (
            self.quantite_fourmis_initiale + self.jour * self.reine.taux_oeufs
        )
        return total_fourmis - self.quantite_fourmis

    def _mettre_a_jour_fourmis(self):
        self.reine.grandir()
        self.reine.manger(self.nourriture)

        for fourmi in self.fourmis:
            fourmi.grandir()
            fourmi.manger(self.nourriture)

        self.fourmis = [fourmi for fourmi in self.fourmis if fourmi.est_vivante]

    def _mettre_a_jour_oeufs(self):
        nouvelles_fourmis = []
        for oeuf in self.oeufs:
            fourmi = oeuf.grandir()
            if fourmi:
                nouvelles_fourmis.append(fourmi)

        self.fourmis.extend(nouvelles_fourmis)
        self.oeufs = [oeuf for oeuf in self.oeufs if not oeuf.est_eclos]

    def _pondre_oeufs(self):
        self.oeufs.extend(self.reine.pondre_oeufs())

    def mettre_a_jour(self):
        self._mettre_a_jour_fourmis()
        self._mettre_a_jour_oeufs()
        self._pondre_oeufs()
        self.jour += 1


def obtenir_entrees():
    try:
        quantite_fourmis_initiale = int(
            input("Entrez la quantité initiale de fourmis: ")
        )
        quantite_nourriture = int(input("Entrez la quantité initiale de nourriture: "))
        vitesse_simulation = float(
            input(
                "Entrez la vitesse de simulation (en secondes par jour, par exemple, 2.0): "
            )
        )
        return quantite_fourmis_initiale, quantite_nourriture, vitesse_simulation
    except ValueError:
        print("Valeur invalide. Veuillez réessayer.")
        return obtenir_entrees()


def demarrer_simulation():
    (
        quantite_fourmis_initiale,
        quantite_nourriture,
        vitesse_simulation,
    ) = obtenir_entrees()

    colonie = Colonie(quantite_fourmis_initiale, quantite_nourriture)

    while colonie.fourmis or colonie.reine.est_vivante or len(colonie.oeufs) > 0:
        colonie.mettre_a_jour()
        print(f"Jour: {colonie.jour}")
        print(f"Fourmis: {colonie.quantite_fourmis}")
        print(f"Oeufs: {len(colonie.oeufs)}")
        print(f"Nourriture: {colonie.nourriture.quantite}")
        print(f"Fourmis mortes: {colonie.quantite_fourmis_mortes}\n")
        time.sleep(vitesse_simulation)


demarrer_simulation()
