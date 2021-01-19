from datetime import datetime
from string import ascii_uppercase

HETU = '123456-XXXX'

def hetutarkistus(hetu):
    
    hetu = str.upper(hetu)
    
    # Tarkastustaulukko
    numerot = '0123456789'
    
    abc = ascii_uppercase
    for i in ['G','I','O','Q','Z']:
        abc = abc.replace(i,'')
        
    tarkistustaul = numerot + abc
    
    # Paivamaaran, yksilonumeron ja tarkistusnumeron muunnokset
    try:
        syntaika = hetu[0:6]
        syntaika_date = datetime.strptime(syntaika,'%d%m%y')
        
        ynro = int(hetu[7:10])
        
        tarkluku = int(hetu[0:6]+hetu[7:10])
        vikamerkki = tarkistustaul[tarkluku % 31]
        
    except:
        print("Henkilötunnusta ei hyväksytä.")
        return None
    
    # Pituus
    e1 = (len(hetu) != 11)
    # Yksilonumeron tarkistus 002-899
    e2 = not (ynro in range(2,899))
    # Vuosisadan tunnuksen tarkistus
    e3 = not (hetu[6] in ['+','-','A'])
    # Tarkistusmerkin tarkistus
    e4 = (hetu[-1] != vikamerkki)
    
    if(e1 or e2 or e3 or e4):
        print('Henkilötunnusta ei hyväksytä.')
    else:
        print('Henkilötunnus hyväksytty.')    
    
    return None

hetutarkistus(HETU)