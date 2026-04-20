import nmap
import sys
import os

def main():
    try:
        nm = nmap.PortScanner()
    except nmap.nmap.PortScannerError:
        print("Nmap is niet gevonden op het systeem. Installeer Nmap (https://nmap.org).")
        sys.exit(1)
    except Exception as e:
        print(f"Onverwachte fout: {e}")
        print("Zorg ervoor dat python-nmap is geïnstalleerd: pip install python-nmap")
        sys.exit(1)

    target_ip = input("Voer het IP-adres in om te scannen (geautoriseerde doelen): ")

    print(f"\n[+] Starten met Fase 1: Snelle TCP-scan op {target_ip}...")
    
    try:
        nm.scan(hosts=target_ip, arguments='-F -T4 -sT --open')
    except Exception as e:
        print(f"Fout tijdens de scan: {e}")
        sys.exit(1)

    if not nm.all_hosts():
        print("[-] Geen hosts gevonden of host is down.")
        sys.exit(0)

    open_tcp_ports = []
    
    for host in nm.all_hosts():
        print(f"Host : {host} ({nm[host].hostname()})")
        print(f"State : {nm[host].state()}")
        
        for proto in nm[host].all_protocols():
            print(f"Protocol : {proto}")
            
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                state = nm[host][proto][port]['state']
                print(f"  Poort : {port}\tStatus : {state}")
                if state == 'open' and proto == 'tcp':
                    open_tcp_ports.append(str(port))

    if open_tcp_ports:
        port_list = ",".join(open_tcp_ports)
        print(f"\n[+] Fase 2: Starten met diepte-scan (OS, Versie) op poorten: {port_list}")
        
        try:
            nm.scan(hosts=target_ip, arguments=f'-p {port_list} -A -T3')
            
            for host in nm.all_hosts():
                print(f"\n--- Gedetailleerde Resultaten voor {host} ---")
                
                if 'osmatch' in nm[host] and len(nm[host]['osmatch']) > 0:
                    os_match = nm[host]['osmatch'][0]
                    print(f"[OS] Mogelijk Besturingssysteem: {os_match['name']} ({os_match['accuracy']}% nauwkeurig)")
                
                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    for port in sorted(lport):
                        service = nm[host][proto][port]
                        print(f"[Poort {port}/{proto}] Service: {service.get('name', 'onbekend')} "
                              f"Versie: {service.get('product', '')} {service.get('version', '')}")
                        
        except Exception as e:
            print(f"Fout tijdens gedetailleerde scan: {e}")
            print("Let op: OS fingerprinting (-O of -A) vereist vaak beheerdersrechten (root/Administrator).")
    else:
        print("\n[-] Geen open poorten gevonden in Fase 1 om dieper te scannen.")

    try:
        # Sla de nmap output op in de volgende locatie:
        output_dir = r"C:\Users\PG2002\Desktop\Nmap_final\output"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"scan_{target_ip.replace('.', '_')}.txt")
        
        with open(output_file, 'w') as f:
            f.write(f"Scan resultaten voor {target_ip}\n")
            if open_tcp_ports:
                f.write(f"Open poorten: {','.join(open_tcp_ports)}\n")
            else:
                f.write("Geen open poorten gevonden.\n")
        print(f"\n[!] Resultaten tevens opgeslagen in: {output_file}")
    except Exception as e:
        print(f"\n[!] Kon output bestand niet aanmaken: {e}")

if __name__ == '__main__':
    main()