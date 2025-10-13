def month_to_season(month):
        
        if month in [12, 1, 2]:
            return "Зима"
        elif month in [3, 4, 5]:
            return "Весна"
        elif month in [6, 7, 8]:
            return "Лето"
        elif month in [9, 10, 11]:
            return "Осень"

month_number = 2
season = month_to_season(month_number)
print(f"Месяц {month_number} — это сезон: {season}")

month_number = 4
season = month_to_season(month_number)
print(f"Месяц {month_number} — это сезон: {season}")

month_number = 7
season = month_to_season(month_number)
print(f"Месяц {month_number} — это сезон: {season}")

month_number = 10
season = month_to_season(month_number)
print(f"Месяц {month_number} — это сезон: {season}")
