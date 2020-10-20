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

def exQuery(q): # hier anpassen XD
    print(q)
    return 0

ensure_parsable("Kontakte.vcf")

for contact in parse_sequent("Kontakte.vcf"):
    for name in contact:
        exQuery(f"INSERT INTO `Person`  (`PersonNr`,    `Bezeichnung`,  `Geburtsdatum`, `Geburtsort`,   `Geschlecht`,   `Staatsangehoerigkeit`, `Augenfarbe`,   `Hautfarbe`,    `PersonalausweisNr`,    `Mutter`,   `Vater`) VALUES (NULL, '{name}', NULL, NULL, NULL, 'deutsch', NULL, 'hell', NULL, NULL, NULL);")
        persnr=exQuery(f"SELECT MAX(PersonNr) FROM Person WHERE Bezeichnung='{name}';")
        for category in desired_categories:
            try:
                for val in contact[name][category]:
                    exQuery(f"INSERT INTO `Kontaktinfo` (`KontaktinfoNr`, `Person`, `Name`, `Bemerkung`) VALUES (NULL, '{persnr}', '{category}', '{val}');")
            except:
                pass
