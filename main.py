# 26. Oziq-ovqat tayyorlash

class Recipe:
    def __init__(self, name, prep_time_minutes):
        self.name = name                    # ovqat nomi
        self.prep_time = prep_time_minutes  # tayyorlash vaqti (daqiqa)

    def total_time(self):
        """Ovqatni tayyorlash uchun ketgan vaqt (daqiqa)"""
        return self.prep_time

    def __str__(self):
        return f"{self.name:14} | {self.prep_time:4} daqiqa"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class MainCourse(Recipe):
    def __str__(self):
        return f"🍲 {self.name:12} → {self.prep_time:3} daqiqa"


class SideDish(Recipe):
    def __str__(self):
        return f"🥗 {self.name:12} → {self.prep_time:3} daqiqa"


# Qo‘shimcha misollar uchun (foydali bo‘lishi mumkin)
class Soup(Recipe):
    def __str__(self):
        return f"🥣 {self.name:12} → {self.prep_time:3} daqiqa"


class Dessert(Recipe):
    def __str__(self):
        return f"🍰 {self.name:12} → {self.prep_time:3} daqiqa"


# --------------------------------------------------
# Umumiy tayyorlash vaqtini chiqarish
# --------------------------------------------------

def show_cooking_time_summary(dishes):
    print("\n" + "═" * 60)
    print("     OVQAT TAYYORLASH VAQTI — UMUMIY HISOB     ".center(60))
    print("═" * 60)
    print("Ovqat nomi             Tayyorlash vaqti")
    print("─" * 60)

    total_minutes = 0

    for dish in dishes:
        print(dish)
        total_minutes += dish.total_time()

    hours = total_minutes // 60
    minutes_left = total_minutes % 60

    print("─" * 60)
    print(f"Jami tayyorlash vaqti:   {total_minutes:4} daqiqa "
          f"({hours} soat {minutes_left:02d} daqiqa)")
    print("═" * 60 + "\n")


# Test ma'lumotlari (bir kechki ovqat misoli)
ovqatlar = [
    MainCourse("Osh palov", 70),
    SideDish("Achchiq-chuchuk salat", 12),
    Soup("Sho‘rva", 45),
    MainCourse("Qovurilgan go‘sht", 35),
    SideDish("Sabzavotli garnir", 20),
    Dessert("Shirin non", 25),
]

show_cooking_time_summary(ovqatlar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol ovqatlaringiz:\n")
misol_ovqatlar = [
    MainCourse("Osh", 60),
    SideDish("Salat", 15),
]

show_cooking_time_summary(misol_ovqatlar)
