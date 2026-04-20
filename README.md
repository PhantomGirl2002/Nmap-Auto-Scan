Educatief Nmap Port Scanner Script

Dit is een Python-script dat gebruikmaakt van de python-nmap bibliotheek om een efficiënte, tweestaps netwerkscan uit te voeren. Het is ontworpen om snel poorten te identificeren en vervolgens gerichte scans uit te voeren op de ontdekte services.

⚠️ Disclaimer

Gebruik dit script uitsluitend op netwerken en systemen waarvoor je expliciete, schriftelijke toestemming hebt (bijvoorbeeld je eigen lokale testnetwerk of een CTF-omgeving). Ongeautoriseerd scannen van netwerken van derden is illegaal en strafbaar.

Vereisten

Om dit script te kunnen draaien, moet aan de volgende voorwaarden worden voldaan:

Python 3.x: Zorg ervoor dat Python is geïnstalleerd op je systeem.

Nmap: De daadwerkelijke Nmap-software moet geïnstalleerd zijn op je besturingssysteem.

Windows/macOS/Linux: Download via nmap.org of via je pakketbeheerder (bijv. apt install nmap).

Python-nmap bibliotheek: Dit is de Python-wrapper die in het script wordt gebruikt. Installeer deze via pip:

pip install python-nmap


Werking van het Script

Het script hanteert een methode door de scan in twee efficiënte fases op te splitsen:

Fase 1 (Brede Ontdekking): Voert een snelle TCP Connect-scan (-sT) uit met agressieve timing (-T4) op de 100 meest voorkomende poorten (-F). Dit identificeert snel welke poorten open staan zonder het netwerk onnodig zwaar te belasten.

Fase 2 (Gerichte Diepte-scan): Als er open poorten zijn gevonden in Fase 1, voert het script specifiek op die poorten een agressieve scan uit (-A). Dit omvat OS-fingerprinting, service-versiedetectie en script scanning. (Let op: Voor OS-fingerprinting zijn vaak beheerders/root-rechten vereist).

Gebruik en Output

Start het script in je terminal of command prompt:

python autoscan.py


Volg de instructies op het scherm en voer het doel-IP-adres in. Het script zal zijn voortgang in de console printen.