class KotoIgrashka:
    def __init__(self, name, size, material, months_old):
        self.name = name
        self.size = size
        self.material = material
        self.months_old = months_old

    def Sleep(self, name):
        print(f"{name} is *Zzz*")

    def TalkBehindMyBack(self, name):
        print(f"{name}: *dlsajfweofw*")

    def BeingSquished(self, name):
        print(f"{name}: *AAAAAAAAAAAAAAAAAAAAA*")

    def DoingHwForMe(self, name, months_old):
        print(f"{name}: I've been working non stop for {months_old} months, someone free me...")

dakimakura = KotoIgrashka('Dakimakura', 'large', 'cotton', 24)
Igrashka = KotoIgrashka('Igrashka', 'small', 'cotton', 24)
Squish = KotoIgrashka('Squish', 'extra small', 'squish', 1)

dakimakura.DoingHwForMe(dakimakura.name ,dakimakura.months_old)
Igrashka.BeingSquished(Igrashka.name)
Squish.Sleep(Squish.name)
Squish.TalkBehindMyBack(Squish.name)