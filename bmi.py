# -*- coding: utf-8 -*-
"""
BMI_Rechner.py

Dieses Skript berechnet den Body Mass Index (BMI) eines Benutzers
basierend auf dessen Eingaben für Gewicht und Körpergröße.

Autor: Paul Buchwald
Datum: 02.06.2025
"""

def berechne_bmi(gewicht_kg: float, groesse_m: float) -> float:
    """
    Berechnet den Body Mass Index (BMI).

    Args:
        gewicht_kg (float): Das Gewicht der Person in Kilogramm.
        groesse_m (float): Die Körpergröße der Person in Metern.

    Returns:
        float: Der berechnete BMI. Gibt 0.0 zurück, wenn die Größe 0 ist,
               um eine Division durch Null zu vermeiden.
    """
    if groesse_m == 0:
        return 0.0  # Verhindert Division durch Null
    return round(gewicht_kg / (groesse_m ** 2), 2)

def bmi_kategorie(bmi: float) -> str:
    """
    Bestimmt die BMI-Kategorie basierend auf dem BMI-Wert.

    Args:
        bmi (float): Der Body Mass Index.

    Returns:
        str: Die entsprechende BMI-Kategorie.
    """
    if bmi == 0.0:
        return "Ungültige Eingabe für Größe."
    elif bmi < 18.5:
        return "Untergewicht"
    elif 18.5 <= bmi < 24.9:
        return "Normalgewicht"
    elif 25 <= bmi < 29.9:
        return "Übergewicht"
    elif 30 <= bmi < 34.9:
        return "Adipositas Grad I"
    elif 35 <= bmi < 39.9:
        return "Adipositas Grad II"
    else:
        return "Adipositas Grad III (schwere Adipositas)"

def main():
    """
    Hauptfunktion des Programms.
    Fordert den Benutzer zur Eingabe von Gewicht und Größe auf,
    berechnet den BMI und gibt das Ergebnis sowie die Kategorie aus.
    """
    print("=" * 30)
    print("   BMI-Rechner")
    print("=" * 30)

    while True:
        try:
            # Benutzereingabe für Gewicht
            gewicht_str = input("Bitte geben Sie Ihr Gewicht in Kilogramm ein (z.B. 70.5): ")
            gewicht = float(gewicht_str.replace(',', '.')) # Erlaubt Komma als Dezimaltrennzeichen
            if gewicht <= 0:
                print("Das Gewicht muss positiv sein. Bitte versuchen Sie es erneut.")
                continue
            break
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl für das Gewicht ein.")

    while True:
        try:
            # Benutzereingabe für Größe
            groesse_str = input("Bitte geben Sie Ihre Körpergröße in Metern ein (z.B. 1.75): ")
            groesse = float(groesse_str.replace(',', '.')) # Erlaubt Komma als Dezimaltrennzeichen
            if groesse <= 0:
                print("Die Körpergröße muss positiv sein. Bitte versuchen Sie es erneut.")
                continue
            break
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl für die Körpergröße ein.")

    # BMI berechnen
    bmi_wert = berechne_bmi(gewicht, groesse)

    # BMI-Kategorie bestimmen
    kategorie = bmi_kategorie(bmi_wert)

    # Ergebnis ausgeben
    print("\n--- Ihr Ergebnis ---")
    print(f"Ihr BMI beträgt: {bmi_wert}")
    print(f"Das entspricht: {kategorie}")
    print("---" * 10)

if __name__ == "__main__":
    main()