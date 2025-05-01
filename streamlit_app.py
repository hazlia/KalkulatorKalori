def calculate_daily_calories(gender, berat_badan_kg, tinggi_badan_cm, usia, tingkat_aktivitas):
    """Menghitung kebutuhan kalori harian berdasarkan persamaan Mifflin-St Jeor."""
    tinggi_badan_m = tinggi_badan_cm / 100

    # BMR (Basal Metabolic Rate)
    if gender == 'male':
        BMR = 88.362 + (13.397 * berat_badan_kg) + (4.799 * tinggi_badan_m * 100) - (5.677 * usia)
    elif gender == 'female':
        BMR = 447.593 + (9.247 * berat_badan_kg) + (3.098 * tinggi_badan_m * 100) - (4.33 * usia)
    else:
        return "Jenis kelamin tidak valid"

    # Tingkat Aktivitas
    if tingkat_aktivitas == 'sedentary':
        faktor_aktivitas = 1.2
    elif tingkat_aktivitas == 'lightly_active':
        faktor_aktivitas = 1.375
    elif tingkat_aktivitas == 'moderately_active':
        faktor_aktivitas = 1.55
    elif tingkat_aktivitas == 'very_active':
        faktor_aktivitas = 1.725
    elif tingkat_aktivitas == 'extra_active':
        faktor_aktivitas = 1.9
    else:
        return "Tingkat aktivitas tidak valid"

    # Kalori Harian
    kalori_harian = BMR * faktor_aktivitas
    return kalori_harian

# Input data
gender = input("Jenis kelamin (male/female): ")
berat_badan_kg = float(input("Berat badan (kg): "))
tinggi_badan_cm = float(input("Tinggi badan (cm): "))
usia = int(input("Usia: "))
tingkat_aktivitas = input("Tingkat aktivitas (sedentary, lightly_active, moderately_active, very_active, extra_active): ")

# Menghitung dan menampilkan hasil
kalori_harian = calculate_daily_calories(gender, berat_badan_kg, tinggi_badan_cm, usia, tingkat_aktivitas)

if isinstance(kalori_harian, str):
    print(kalori_harian)
else:
    print("Kebutuhan kalori harian Anda:", kalori_harian)
