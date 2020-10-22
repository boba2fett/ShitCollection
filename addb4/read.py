#!/bin/env python3
import vobject

desired_categories = ["tel", "email"]

def parse_sequent(path):
    with open(path, 'r') as f:
        for vcard in vobject.readComponents(f.read()):
            try:
                values = dict()
                for category in desired_categories:
                    try:
                        values[category] = [
                            val.value for val in vcard.contents[category]]
                    except:
                        pass

                yield {vcard.contents['fn'][0].value: values}
            except:
                pass
def ensure_parsable(path):
    lastContact=None
    try:
        for contact in parse_sequent(path):
            lastContact=contact
    except:
        print("doesnt work behind of:")
        print(lastContact)
        exit(1)

allq=""

def exQuery(q): # hier anpassen XD
    global allq
    #print(q)
    allq+=f"{q}\n"
    return 0

ensure_parsable("Kontakte.vcf")

persnr=1000
startNum=input("Start Number: ")
try:
    startNum=int(startNum)
except:
    print("No number")
    exit(1)

print("\nenter is No\nAny char and enter is a Yes\npersons can have w or m for gender\n")

try:
    for contact in parse_sequent("Kontakte.vcf"):
        for name in contact:
            name=name.replace("  "," ").replace("  "," ")
            if answ:=input(f"Insert Name '{name}' ? ").strip().lower():
                geschlecht="NULL"
                if answ=='m' or answ=='w':
                    geschlecht=f"'{answ}'"
                exQuery(f"INSERT INTO `Person` (`PersonNr`,`Bezeichnung`,`Geburtsdatum`,`Geburtsort`,`Geschlecht`,`Staatsangehoerigkeit`,`Augenfarbe`,`Hautfarbe`,`PersonalausweisNr`,`Mutter`,`Vater`) VALUES ('{persnr}','{name}', NULL, NULL, {geschlecht}, 'deutsch', NULL, 'hell', NULL, NULL, NULL);")
                #persnr=exQuery(f"SELECT MAX(PersonNr) FROM Person WHERE Bezeichnung='{name}';")
                parts=name.split(' ')
                if len(parts)>1:
                    nachname=' '.join(parts[1:])
                    vorname=parts[0]
                    if answ:=input(f"Insert Name '{nachname}', Vorname '{vorname}'? ").strip():
                        exQuery(f"INSERT INTO `Name` (`NameNr`, `Person`, `Startdatum`, `Enddatum`, `Name`, `Vorname`, `Bemerkung`) VALUES (NULL, '{persnr}', NULL, NULL, '{nachname}', '{vorname}', NULL);")
                for category in desired_categories:
                    try:
                        for val in contact[name][category]:
                            if answ:=input(f"Insert Value '{val}' in category '{category}' for '{name}' ?").strip():
                                exQuery(f"INSERT INTO `Kontaktinfo` (`KontaktinfoNr`, `Person`, `Name`, `Bemerkung`) VALUES (NULL, '{persnr}', '{category}', '{val}');")
                    except:
                        pass
                persnr+=1
            print("")
except KeyboardInterrupt:
    print("abgebrochen")
print("-------------------------------\n")
print(allq)