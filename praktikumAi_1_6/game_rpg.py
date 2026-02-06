from abc import ABC, abstractmethod

# ==========================================
# LATIHAN 5: ABSTRACTION (BLUEPRINT)
# ==========================================
class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass

# ==========================================
# CLASS UTAMA HERO (LATIHAN 1, 2, 4)
# ==========================================
class Hero(GameUnit):
    def __init__(self, name, hp_awal, attack_power):
        self.name = name
        self.__hp = hp_awal  
        self.attack_power = attack_power

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def info(self):
        print(f"Hero: {self.name:10} | HP: {self.get_hp():4} | Power: {self.attack_power}")

    def diserang(self, damage):
        self.set_hp(self.get_hp() - damage)
        print(f"{self.name} terkena {damage} damage. Sisa HP: {self.get_hp()}")

    # Hapus duplikasi! Gunakan satu method serang yang fleksibel
    def serang(self, lawan=None):
        if lawan:
            print(f"{self.name} menyerang {lawan.name}!")
            lawan.diserang(self.attack_power)
        else:
            print(f"{self.name} menyerang dengan tangan kosong.")

# ==========================================
# CLASS TURUNAN (LATIHAN 3 & 6 - POLYMORPHISM)
# ==========================================
class Mage(Hero):
    def __init__(self, name, hp=80, attack=30, mana=100):
        super().__init__(name, hp, attack)
        self.mana = mana

    def info(self):
        print(f"Mage: {self.name:10} | HP: {self.get_hp():4} | Mana: {self.mana}")
    
    def serang(self, lawan=None):
        if lawan:
            super().serang(lawan)
        else:
            print(f"{self.name} (Mage) menembakkan Bola Api! Boom! 🔥")

class Archer(Hero):
    def __init__(self, name, hp=90, attack=25):
        super().__init__(name, hp, attack)

    def serang(self, lawan=None):
        if lawan:
            super().serang(lawan)
        else:
            print(f"{self.name} (Archer) memanah dari jauh! Jleb! 🏹")

class Fighter(Hero):
    def __init__(self, name, hp=150, attack=20):
        super().__init__(name, hp, attack)

    def serang(self, lawan=None):
        if lawan:
            super().serang(lawan)
        else:
            print(f"{self.name} (Fighter) memukul dengan pedang! Slash! ⚔️")

class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis
        self.name = jenis # Agar konsisten dengan Hero saat diserang

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target.name}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")

# ==========================================
# OUTPUT JAWABAN LATIHAN 1 - 6
# ==========================================

# --- JAWABAN LATIHAN 1 & 2 ---
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)
hero1.set_hp(500)

print("--- JAWABAN LATIHAN 1 & 2 ---")
hero1.info()
hero2.info()
hero1.serang(hero2)

# --- JAWABAN LATIHAN 3 ---
print("\n--- JAWABAN LATIHAN 3 ---")
eudora = Mage("Eudora", 80, 30, 100)
eudora.info()

# --- JAWABAN LATIHAN 4 ---
print("\n--- JAWABAN LATIHAN 4 ---")
hero1.set_hp(-50)
print(f"Hasil HP hero1: {hero1.get_hp()}")
print(f"Akses paksa Name Mangling: {hero1._Hero__hp}")

# --- JAWABAN LATIHAN 5 ---
print("\n--- JAWABAN LATIHAN 5 ---")
h_5 = Hero("Alucard", 200, 25)
m_5 = Monster("Serigala")
h_5.info()
m_5.info()

# --- JAWABAN LATIHAN 6 ---
print("\n--- PERANG DIMULAI (POLYMORPHISM) ---")
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord")
]

for pahlawan in pasukan:
    pahlawan.serang()