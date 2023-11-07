import time
import random

FOURMIS_AGE_MAX = 14

REINE_AGE_MAX = 56
REINE_NOMBRES_OEUFS = 40


class Nourriture:
    def __init__(self, quantite_initiale):
        self.quantite = quantite_initiale

    def __str__(self):
        return f"Nourriture: {self.quantite}\n"

    def retirer_quantite(self, quantite):
        if self.quantite >= quantite:
            # Pour éviter d'avoir une quantité négative
            self.quantite -= quantite
        else:
            self.quantite = 0


class Fourmi:
    def __init__(self):
        self.est_vivante = True
        self.age = 0
        self.age_max = FOURMIS_AGE_MAX

    def __str__(self):
        return f"Fourmi: {self.est_vivante}\nAge: {self.age}\n"

    def grandir(self):
        if self.est_vivante:
            self.age += 1
            if self.age >= self.age_max:
                self.mourir()

    def manger(self, nourriture, faim=1):
        if self.est_vivante:
            if nourriture.quantite > 0 and nourriture.quantite >= faim:
                nourriture.retirer_quantite(faim)
            else:
                self.mourir()

    def mourir(self):
        self.est_vivante = False


class Oeuf:
    def __init__(self):
        self.age = 0
        self.est_eclos = False
        self.est_mort = False

    def __str__(self):
        return f"Oeuf: {self.est_eclos}\nAge: {self.age}\n"

    def grandir(self):
        self.age += 1
        if self.age >= 3:
            # 80% de chance d'éclore
            if random.random() < 0.8:
                self.est_eclos = True
                return Fourmi()
            else:
                # Marquer l'œuf comme mort s'il n'éclos pas
                self.est_mort = True
        return None


class Reine(Fourmi):
    def __init__(self):
        super().__init__()
        self.age_max = REINE_AGE_MAX
        self.nombres_oeufs = REINE_NOMBRES_OEUFS

    def __str__(self):
        return f"Reine: {self.est_vivante}\nAge: {self.age}\nOeufs: {self.nombres_oeufs}\n"

    def pondre_oeufs(self):
        if self.est_vivante:
            return [Oeuf() for _ in range(self.nombres_oeufs)]
        return []


class Colonie:
    def __init__(self, quantite_fourmis_initiale, quantite_nourriture):
        self.fourmis = [Fourmi() for _ in range(quantite_fourmis_initiale)]
        self.oeufs = []
        self.reine = Reine()
        self.nourriture = Nourriture(quantite_nourriture)
        self.jour = 0
        # Pour compter le nombre de fourmis nées + la reine
        self.fourmis_nees = quantite_fourmis_initiale + 1

    def __str__(self):
        return f"""Jour: {self.jour}
Oeufs: {len(self.oeufs)}
Fourmis: {self.quantite_fourmis}
Nourriture: {self.nourriture.quantite}
Reine vivante: {self.reine.est_vivante}
Fourmis mortes: {self.quantite_fourmis_mortes}\n"""

    @property
    def quantite_fourmis(self):
        return len(self.fourmis) + self.reine.est_vivante

    @property
    def quantite_fourmis_mortes(self):
        return self.fourmis_nees - self.quantite_fourmis

    def _mettre_a_jour_fourmis(self):
        self.reine.grandir()
        self.reine.manger(self.nourriture, faim=self.reine.nombres_oeufs)

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
                self.fourmis_nees += 1

        self.fourmis.extend(nouvelles_fourmis)
        # Retirer les œufs qui sont éclos ou morts
        self.oeufs = [oeuf for oeuf in self.oeufs if not oeuf.est_eclos and not oeuf.est_mort]

    def _pondre_oeufs(self):
        self.oeufs.extend(self.reine.pondre_oeufs())

    def mettre_a_jour(self):
        self._mettre_a_jour_fourmis()
        self._mettre_a_jour_oeufs()
        self._pondre_oeufs()
        self.jour += 1


def obtenir_entrees():
    try:
        quantite_fourmis_initiale = int(input("Entrez la quantité initiale de fourmis: "))
        quantite_nourriture = int(input("Entrez la quantité initiale de nourriture: "))
        vitesse_simulation = float(input("Entrez la vitesse de simulation (en secondes par jour, par exemple, 2.0): "))
        return (
            quantite_fourmis_initiale,
            quantite_nourriture,
            vitesse_simulation,
        )
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
        print(colonie)
        time.sleep(vitesse_simulation)


demarrer_simulation()

input("Appuyez sur une ENTER pour quitter...")
