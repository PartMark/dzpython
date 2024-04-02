# Tingimuslik operaator IF
#1
# def osta_pilet(vanus):
#     if vanus < 0 or vanus > 100:
#         return "Vigased andmed"
#     elif vanus < 6:
#         return "Tasuta"
#     elif 6 <= vanus <= 14:
#         return "Lastepilet"
#     elif 15 <= vanus <= 65:
#         return "Täispilet"
#     else:
#         return "Sooduspilet"

# eesnimi = input("Sisesta Juku eesnimi: ")
# vanus = int(input("Sisesta Juku vanus: "))

# pilet = osta_pilet(vanus)
# print(f"{eesnimi} pilet: {pilet}")

#2
# nimi1 = input("Sisesta esimese inimese nimi: ")
# nimi2 = input("Sisesta teise inimese nimi: ")
# print(f"Täna on {nimi1} ja {nimi2} pinginaabrid!")

#3
# pikkus = float(input("Sisesta toa pikkus (meetrites): "))
# laius = float(input("Sisesta toa laius (meetrites): "))

# põranda_pindala = pikkus * laius
# print(f"Põranda pindala on {põranda_pindala} ruutmeetrit.")

# remondi_soov = input("Kas soovite teha remonti? (jah/ei): ")
# if remondi_soov.lower() == "jah":
#     ruutmeetri_hind = float(input("Sisesta ruutmeetri hind (EUR): "))
#     remondi_hind = põranda_pindala * ruutmeetri_hind
#     print(f"Põranda vahetamise hind on {remondi_hind} eurot.")
# else:
#     print("Remondi tegemine jäeti ära.")

#4
# def leia_allahindlus(alghind):
#     if alghind > 700:
#         soodustus = alghind * 0.3
#         uus_hind = alghind - soodustus
#         return uus_hind
#     else:
#         return alghind

# alghind = float(input("Sisesta toote alghind: "))

# uus_hind = leia_allahindlus(alghind)
# print(f"Soodustusega hind on {uus_hind} eurot.")

#5
# temperatuur = float(input("Sisesta temperatuur kraadides: "))

# if temperatuur > 18:
#     print("Temperatuur on üle 18 kraadi, mis on soovitav toasoojus talvel.")
# else:
#     print("Temperatuur on 18 kraadi või madalam.")

#6
# pikkus = float(input("Sisesta oma pikkus meetrites: "))

# if pikkus < 1.6:
#     print("Sa oled lühike.")
# elif 1.6 <= pikkus <= 1.8:
#     print("Sa oled keskmise pikkusega.")
# else:
#     print("Sa oled pikk.")

#7
# pikkus = float(input("Sisesta oma pikkus meetrites: "))
# sugu = input("Sisesta oma sugu (m/n): ")

# if sugu.lower() == "m":
#     if pikkus < 1.6:
#         print("Sa oled lühike mees.")
#     elif 1.6 <= pikkus <= 1.8:
#         print("Sa oled keskmise pikkusega mees.")
#     else:
#         print("Sa oled pikk mees.")
# elif sugu.lower() == "n":
#     if pikkus < 1.5:
#         print("Sa oled lühike naine.")
#     elif 1.5 <= pikkus <= 1.7:
#         print("Sa oled keskmise pikkusega naine.")
#     else:
#         print("Sa oled pikk naine.")
# else:
#     print("Vigane sugu! Palun sisestage 'm' või 'n'.")

#8
# import random

# def main():
#     tooted = {
#         "piim": random.uniform(0.5, 2),
#         "sai": random.uniform(0.2, 1),
#         "leib": random.uniform(0.3, 1.5),}

#     ostukorv = {}
#     for toode, hind in tooted.items():
#         kogus = int(input(f"Mitu tükki {toode} soovid osta: "))
#         ostukorv[toode] = (hind, kogus)

#     summa = 0
#     print("\nTšekk:")
#     for toode, (hind, kogus) in ostukorv.items():
#         toote_summa = hind * kogus
#         print(f"{toode}: {kogus} tk x {hind} EUR = {toote_summa} EUR")
#         summa += toote_summa

#     print(f"\nKokku: {summa} EUR")
# main()

#9
# def ruudu_kontroll(külg1, külg2):
#     if külg1 == külg2:
#         return "Tegemist on ruuduga."
#     else:
#         return "Tegemist ei ole ruuduga."

# def main():
#     külg1 = float(input("Sisesta esimese külje pikkus: "))
#     külg2 = float(input("Sisesta teise külje pikkus: "))

#     tulemus = ruudu_kontroll(külg1, külg2)
#     print(tulemus)

# main()

#10
# def liida(a, b):
#     return a + b

# def lahuta(a, b):
#     return a - b

# def korruta(a, b):
#     return a * b

# def jaga(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Viga: Nulliga jagamine"

# arv1 = float(input("Sisesta esimene arv: "))
# arv2 = float(input("Sisesta teine arv: "))
# tehe = input("Vali tehe (+, -, *, /): ")

# if tehe == '+':
#     tulemus = liida(arv1, arv2)
# elif tehe == '-':
#     tulemus = lahuta(arv1, arv2)
# elif tehe == '*':
#     tulemus = korruta(arv1, arv2)
# elif tehe == '/':
#     tulemus = jaga(arv1, arv2)
# else:
#     tulemus = "Vale tehe"

# print(f"Tulemus: {tulemus}")

#11
# def on_juubel(aasta):
#     if aasta % 5 == 0:
#         return True
#     else:
#         return False

# sünnipäev = int(input("Sisesta oma sünnipäeva aastaarv: "))

# if on_juubel(sünnipäev):
#     print("Palju õnne! See on juubeliaasta!")
# else:
#     print("Tavaline aasta.")

#12
# hind = float(input("Sisesta toote hind: "))

# if hind <= 10:
#     allahindlus = 0.1 * hind
# else:
#     allahindlus = 0.2 * hind

# lõplik_hind = hind - allahindlus
# print(f"Toote lõplik hind on {lõplik_hind} eurot.")

#13
# sugu = input("Kas oled mees või naine? (m/n): ")

# if sugu.lower() == 'm':
#     vanus = int(input("Sisesta oma vanus: "))

#     if 16 <= vanus <= 18:
#         print("Oled sobilik kandideerima jalgpallimeeskonda!")
#     else:
#         print("Kahjuks sa ei sobi antud meeskonda.")
# elif sugu.lower() == 'n':
#     print("Naised ei saa kandideerida antud meeskonda.")
# else:
#     print("Vigane sugu! Palun sisesta 'm' või 'n'.")

#14
# inimeste_arv = int(input("Sisesta inimeste arv: "))
# bussi_kohad = int(input("Sisesta ühe bussi kohtade arv: "))

# busside_arv = inimeste_arv // bussi_kohad
# viimases_bussis = inimeste_arv % bussi_kohad

# if viimases_bussis > 0:
#     busside_arv += 1

# print(f"Vaja on {busside_arv} bussi.")
# print(f"Viimases bussis on {viimases_bussis} inimest.")


#Matemaatika

# import random

# def genereeri_tehe(tase, operatsioonid, min_väärtus, max_väärtus):
#     tehe = []
#     for _ in range(tase):
#         arv = random.randint(min_väärtus, max_väärtus)
#         tehe.append(str(arv))
#         tehe.append(random.choice(operatsioonid))
#     arv = random.randint(min_väärtus, max_väärtus)
#     tehe.append(str(arv))
#     return " ".join(tehe)

# def arvuta_tehe(tehe):
#     return eval(tehe)

# def hinda_tulemus(protsent):
#     if protsent < 60:
#         return "Hinne 2"
#     elif 60 <= protsent < 75:
#         return "Hinne 3"
#     elif 75 <= protsent < 90:
#         return "Hinne 4"
#     else:
#         return "Hinne 5"

# print("Tere tulemast matemaatika testi!")
# tase = int(input("Vali testi tase (1, 2 või 3): "))
# operatsioonid = input("Vali tehted (+, -, *, /, **): ").split()
# min_väärtus = int(input("Sisesta väikseim väärtus: "))
# max_väärtus = int(input("Sisesta suurim väärtus: "))
# kogus = int(input("Sisesta tehtete arv: "))

# õiged_vastused = 0
# for _ in range(kogus):
#     tehe = genereeri_tehe(tase, operatsioonid, min_väärtus, max_väärtus)
#     vastus = arvuta_tehe(tehe)
#     print(f"Kui tehe on: {tehe}")
#     kasutaja_vastus = float(input("Sisesta oma vastus: "))
#     if kasutaja_vastus == vastus:
#         õiged_vastused += 1
#         print("Õige vastus!")
#     else:
#         print(f"Vale vastus! Õige vastus oli: {vastus}")

# protsent = õiged_vastused / kogus * 100
# print(f"\nTest lõppenud! Sinu tulemus: {õiged_vastused}/{kogus}, {protsent}%.")
# print(f"Hinne: {hinda_tulemus(protsent)}")

#Sõnastik

# import random

# rus_sõnad = ["яблоко", "стол", "машина", "дом"]
# est_sõnad = ["õun", "laud", "auto", "maja"]

# with open("rus.txt", "w", encoding="utf-8") as f:
#     for sõna in rus_sõnad:
#         f.write(sõna + "\n")

# with open("est.txt", "w", encoding="utf-8") as f:
#     for sõna in est_sõnad:
#         f.write(sõna + "\n")

# def loe_failist(f):  #Написание функций для чтения и записи в файлы
#     mas = []
#     with open(f, 'r', encoding="utf-8") as fail:
#         for rida in fail:
#             mas.append(rida.strip())
#     return mas

# def salvesta_failisse(sõnad, failinimi):
#     with open(failinimi, 'w', encoding="utf-8") as fail:
#         for sõna in sõnad:
#             fail.write(sõna + '\n')

# def tõlgi(sõnastik, sõna):
#     return sõnastik.get(sõna)

# def lisa_sõna(sõnastik, sõna, tõlge):
#     sõnastik[sõna] = tõlge

# def main():
#     # чтение слов из файлов
#     rus_sõnad = loe_failist("rus.txt")
#     est_sõnad = loe_failist("est.txt")
#     rus_sõnastik = {sõna: tõlge for sõna, tõlge in zip(est_sõnad, rus_sõnad)}
#     est_sõnastik = {sõna: tõlge for sõna, tõlge in zip(rus_sõnad, est_sõnad)}

#     while True:
#         print("\n1. Перевод с русского на эстонский")
#         print("2. Перевод с эстонского на русский")
#         print("3. Добавить слово в словарь")
#         print("4. Проверить знание слов")
#         print("5. Выход")
#         valik = input("Выберите действие: ")

#         if valik == "1":
#             sõna = input("Введите слово на русском: ")
#             tõlge = tõlgi(rus_sõnastik, sõna)
#             if tõlge:
#                 print(f"Перевод: {tõlge}")
#             else:
#                 print("Такого слова нет в словаре.")
#                 lisamine = input("Хотите добавить это слово в словарь? (да/нет): ")
#                 if lisamine.lower() == "да":
#                     tõlge = input("Введите перевод слова на эстонский: ")
#                     lisa_sõna(rus_sõnastik, sõna, tõlge)
#                     lisa_sõna(est_sõnastik, tõlge, sõna)
#                     print("Слово успешно добавлено в словарь.")
#         elif valik == "2":
#             sõna = input("Введите слово на эстонском: ")
#             tõlge = tõlgi(est_sõnastik, sõna)
#             if tõlge:
#                 print(f"Перевод: {tõlge}")
#             else:
#                 print("Такого слова нет в словаре.")
#                 lisamine = input("Хотите добавить это слово в словарь? (да/нет): ")
#                 if lisamine.lower() == "да":
#                     tõlge = input("Введите перевод слова на русский: ")
#                     lisa_sõna(est_sõnastik, sõna, tõlge)
#                     lisa_sõna(rus_sõnastik, tõlge, sõna)
#                     print("Слово успешно добавлено в словарь.")
#         elif valik == "3":
#             failinimi = input("Введите имя файла (rus.txt или est.txt): ")
#             sõna = input("Введите слово: ")
#             tõlge = input("Введите перевод слова: ")
#             if failinimi == "rus.txt":
#                 lisa_sõna(rus_sõnastik, sõna, tõlge)
#                 lisa_sõna(est_sõnastik, tõlge, sõna)
#             elif failinimi == "est.txt":
#                 lisa_sõna(est_sõnastik, sõna, tõlge)
#                 lisa_sõna(rus_sõnastik, tõlge, sõna)
#             else:
#                 print("Неправильный выбор файла.")
#         elif valik == "4":
#             print("Проверка знания слов")
#             sõnastik = rus_sõnastik.copy()
#             sõnastik.update(est_sõnastik)
#             õiged_vastused = 0
#             koguarv = len(sõnastik)
#             for _ in range(koguarv):
#                 sõna = random.choice(list(sõnastik.keys()))
#                 tõlge = sõnastik[sõna]
#                 print(f"Как переводится слово '{sõna}'?")
#                 kasutaja_vastus = input("Ваш перевод: ")
#                 if kasutaja_vastus == tõlge:
#                     õiged_vastused += 1
#                     print("Правильно!")
#                 else:
#                     print(f"Неправильно! Правильный ответ: '{tõlge}'")
#                 del sõnastik[sõna]
#             print(f"Результат: {õiged_vastused / koguarv * 100:.2f}% правильных ответов.")
#         elif valik == "5":
#             print("Выход из программы.")
#             break
#         else:
#             print("Неправильный выбор. Попробуйте еще раз.")

# if __name__ == "__main__":
#     main()


#Решение квадратного уравнения



import tkinter as tk
from tkinter import messagebox

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x,
    else:
        return None

def solve_equation():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        roots = solve_quadratic(a, b, c)
        if roots is not None:
            if len(roots) == 1:
                result_label.config(text=f"Уравнение имеет один корень: x = {roots[0]}")
            else:
                result_label.config(text=f"Уравнение имеет два корня: x1 = {roots[0]}, x2 = {roots[1]}")
        else:
            result_label.config(text="Уравнение не имеет действительных корней.")
    except ValueError:
        messagebox.showerror("Ошибка", "Поля должны содержать числовые значения!")

root = tk.Tk()
root.title("Решение квадратного уравнения")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_a = tk.Label(frame, text="a:", font=("Arial", 12))
label_a.grid(row=0, column=0)
entry_a = tk.Entry(frame, font=("Arial", 12))
entry_a.grid(row=0, column=1)

label_b = tk.Label(frame, text="b:", font=("Arial", 12))
label_b.grid(row=1, column=0)
entry_b = tk.Entry(frame, font=("Arial", 12))
entry_b.grid(row=1, column=1)

label_c = tk.Label(frame, text="c:", font=("Arial", 12))
label_c.grid(row=2, column=0)
entry_c = tk.Entry(frame, font=("Arial", 12))
entry_c.grid(row=2, column=1)

solve_button = tk.Button(frame, text="Решить", font=("Arial", 12), bg="green", fg="white", command=solve_equation)
solve_button.grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(frame, text="", font=("Arial", 12))
result_label.grid(row=4, columnspan=2)

root.mainloop()

