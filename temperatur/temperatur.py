"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║ ████████╗███████╗███╗   ███╗██████╗ ████████╗███████╗██████╗  █████╗ ██████╗  ║
║ ╚══██╔══╝██╔════╝████╗ ████║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗ ║
║    ██║   █████╗  ██╔████╔██║██████╔╝   ██║   █████╗  ██████╔╝███████║██████╔╝ ║
║    ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝    ██║   ██╔══╝  ██╔══██╗██╔══██║██╔══██╗ ║
║    ██║   ███████╗██║ ╚═╝ ██║██║        ██║   ███████╗██║  ██║██║  ██║██║  ██║ ║
║    ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║ 🔥 TEMPERATURUMRECHNER - EIN VIELSEITIGES KONVERTIERUNGSWERKZEUG 🔥            ║
╚═══════════════════════════════════════════════════════════════════════════════╝

📋 ÜBERSICHT:
   Ein leistungsstarkes Python-Tool zur einfachen Umrechnung zwischen verschiedenen
   Temperatureinheiten mit präzisen Ergebnissen und benutzerfreundlicher Oberfläche.

🔧 UNTERSTÜTZTE UMRECHNUNGEN:
   • Celsius (°C)   ↔ Fahrenheit (°F)
   • Celsius (°C)   → Kelvin (K)
   • Fahrenheit (°F) → Kelvin (K)

✨ FUNKTIONEN:
   ✓ Intuitive Menüführung
   ✓ Robuste Eingabevalidierung
   ✓ Unterstützung für Komma und Punkt als Dezimaltrennzeichen
   ✓ Mehrfache Umrechnungen in einer Sitzung
   ✓ Klare Fehlermeldungen
   ✓ Präzise Berechnungen

🚀 VERWENDUNG:
   1. Wählen Sie die gewünschte Umrechnungsrichtung
   2. Geben Sie den Temperaturwert ein
   3. Betrachten Sie das berechnete Ergebnis
   4. Entscheiden Sie, ob Sie eine weitere Umrechnung durchführen möchten

📝 BEISPIEL:
   ┌───────────────────────────────────────────────────────────────┐
   │ Bitte wählen Sie die Umrechnungsrichtung:                     │
   │ 1: Celsius zu Fahrenheit                                      │
   │ 2: Fahrenheit zu Celsius                                      │
   │ 3: Celsius zu Kelvin                                          │
   │ 4: Fahrenheit zu Kelvin                                       │
   │ Ihre Wahl (1-4): 1                                            │
   │                                                               │
   │ Bitte geben Sie die Temperatur in Celsius ein (z.B. 25.3): 25 │
   │                                                               │
   │ Ergebnis: 25.0°C entsprechen 77.0°F                           │
   │                                                               │
   │ Möchten Sie eine weitere Umrechnung durchführen? (ja/nein): n │
   │                                                               │
   │ Vielen Dank für die Nutzung des Temperaturumrechners.         │
   │ Auf Wiedersehen!                                              │
   └───────────────────────────────────────────────────────────────┘

📌 METADATEN:
   • Autor:        Paul Buchwald, FSV41
   • GitHub:       https://github.com/paulHnee/Python
   • Erstellt am:  05.06.2025
   • Letzte Änderung: 05.06.2025
   • Version:      1.0.0
   • Python:       3.13.3
   • Lizenz:       MIT
   • Credits:      SWE-1 KI Assistant für die Implementierung der Dokumentation
"""

# Funktion zur Umrechnung von Celsius in Fahrenheit
def celsius_in_fahrenheit(celsius: float) -> float:
    """
    Konvertiert eine Temperatur von Celsius in Fahrenheit.
    Formel: °F = (°C × 9/5) + 32

    Args:
        celsius (float): Die Temperatur in Celsius.

    Returns:
        float: Die Temperatur in Fahrenheit.
    """
    # Durchführung der Umrechnung nach der Formel
    return celsius * 9/5 + 32


# Funktion zur Umrechnung von Fahrenheit in Celsius
def fahrenheit_in_celsius(fahrenheit: float) -> float:
    """
    Konvertiert eine Temperatur von Fahrenheit in Celsius.
    Formel: °C = (°F - 32) × 5/9

    Args:
        fahrenheit (float): Die Temperatur in Fahrenheit.

    Returns:
        float: Die Temperatur in Celsius.
    """
    return (fahrenheit - 32) * 5/9

def celsius_in_kelvin(celsius: float) -> float:
    """
    Konvertiert eine Temperatur von Celsius in Kelvin.
    Formel: K = °C + 273.15
    Der absolute Nullpunkt (0K) entspricht -273.15°C.

    Args:
        celsius (float): Die Temperatur in Celsius.

    Returns:
        float: Die Temperatur in Kelvin.
    """
    return celsius + 273.15

def fahrenheit_in_kelvin(fahrenheit: float) -> float:
    """
    Konvertiert eine Temperatur von Fahrenheit in Kelvin.
    Formel: K = (°F - 32) × 5/9 + 273.15
    Kombiniert die Umrechnung von Fahrenheit zu Celsius und dann zu Kelvin.

    Args:
        fahrenheit (float): Die Temperatur in Fahrenheit.

    Returns:
        float: Die Temperatur in Kelvin.
    """
    return (fahrenheit - 32) * 5/9 + 273.15

if __name__ == "__main__":
    # Programmüberschrift anzeigen
    print("=" * 30)
    print("   Temperaturumrechner")
    print("=" * 30)
    
    # Hauptschleife für die Programmwiederholung
    while True:
        # Schleife für die Auswahl der Umrechnungsrichtung
        while True:
            try:
                # Menü mit den verfügbaren Umrechnungsoptionen anzeigen
                eingabe = input("\nBitte wählen Sie die Umrechnungsrichtung:\n"
                               "1: Celsius zu Fahrenheit\n"
                               "2: Fahrenheit zu Celsius\n"
                               "3: Celsius zu Kelvin\n"
                               "4: Fahrenheit zu Kelvin\n"
                               "Ihre Wahl (1-4): ")
                
                # Verarbeitung der Benutzerauswahl
                if eingabe == '1':  # Celsius zu Fahrenheit
                    while True:
                        try:
                            # Eingabe der Temperatur in Celsius
                            celsius_str = input("\nBitte geben Sie die Temperatur in Celsius ein (z.B. 25.3): ")
                            # Umwandlung des Eingabestrings in eine Fließkommazahl (erlaubt Komma als Dezimaltrennzeichen)
                            celsius = float(celsius_str.replace(',', '.'))
                            # Umrechnung und Ausgabe des Ergebnisses
                            fahrenheit = celsius_in_fahrenheit(celsius)
                            print(f"\nErgebnis: {celsius}°C entsprechen {fahrenheit:.1f}°F")
                            break  # Gültige Eingabe erhalten, Schleife beenden
                        except ValueError:
                            # Fehlerbehandlung für ungültige Zahlenformate
                            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
                    break  # Zurück zum Hauptmenü nach erfolgreicher Umrechnung
                    
                elif eingabe == '2':  # Fahrenheit zu Celsius
                    while True:
                        try:
                            # Eingabe der Temperatur in Fahrenheit
                            fahrenheit_str = input("\nBitte geben Sie die Temperatur in Fahrenheit ein (z.B. 77.5): ")
                            # Umwandlung des Eingabestrings in eine Fließkommazahl
                            fahrenheit = float(fahrenheit_str.replace(',', '.'))
                            # Umrechnung und Ausgabe des Ergebnisses
                            celsius = fahrenheit_in_celsius(fahrenheit)
                            print(f"\nErgebnis: {fahrenheit}°F entsprechen {celsius:.1f}°C")
                            break
                        except ValueError:
                            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
                    break
                    
                elif eingabe == '3':  # Celsius zu Kelvin
                    while True:
                        try:
                            # Eingabe der Temperatur in Celsius
                            celsius_str = input("\nBitte geben Sie die Temperatur in Celsius ein (z.B. 25.3): ")
                            # Umwandlung des Eingabestrings in eine Fließkommazahl
                            celsius = float(celsius_str.replace(',', '.'))
                            # Umrechnung und Ausgabe des Ergebnisses
                            kelvin = celsius_in_kelvin(celsius)
                            print(f"\nErgebnis: {celsius}°C entsprechen {kelvin:.1f} Kelvin")
                            break
                        except ValueError:
                            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
                    break
                    
                elif eingabe == '4':  # Fahrenheit zu Kelvin
                    while True:
                        try:
                            # Eingabe der Temperatur in Fahrenheit
                            fahrenheit_str = input("\nBitte geben Sie die Temperatur in Fahrenheit ein (z.B. 77.5): ")
                            # Umwandlung des Eingabestrings in eine Fließkommazahl
                            fahrenheit = float(fahrenheit_str.replace(',', '.'))
                            # Umrechnung und Ausgabe des Ergebnisses
                            kelvin = fahrenheit_in_kelvin(fahrenheit)
                            print(f"\nErgebnis: {fahrenheit}°F entsprechen {kelvin:.1f} Kelvin")
                            break
                        except ValueError:
                            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
                    break
                    
                else:
                    # Behandlung ungültiger Menüauswahl
                    print("Ungültige Auswahl. Bitte wählen Sie 1, 2, 3 oder 4.")
                    
            except KeyboardInterrupt:
                # Behandelt das Abbrechen des Programms durch den Benutzer (Strg+C)
                print("\nProgramm wird beendet.")
                exit()
        
        # Abfrage, ob eine weitere Umrechnung durchgeführt werden soll
        while True:
            weiter = input("\nMöchten Sie eine weitere Umrechnung durchführen? (ja/nein): ").lower()
            # Überprüfung auf gültige Antworten
            if weiter in ['ja', 'j', 'nein', 'n']:
                break
            print("Bitte antworten Sie mit 'ja' oder 'nein'.")
            
        # Programm beenden, wenn der Benutzer keine weitere Umrechnung wünscht
        if weiter in ['nein', 'n']:
            print("\nVielen Dank für die Nutzung des Temperaturumrechners. Auf Wiedersehen!")
            break
