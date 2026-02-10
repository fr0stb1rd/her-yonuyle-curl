# DICT

DICT, sözlük aramaları için bir protokoldür.

## Kullanım

Eğlenmek için deneyin

    curl dict://dict.org/m:curl
    curl dict://dict.org/d:heisenbug:jargon
    curl dict://dict.org/d:daniel:gcide

'm' için takma adlar 'match' (eşleşme) ve 'find' (bul), 'd' için takma adlar 'define' (tanımla) ve 'lookup' (ara) şeklindedir. Örneğin,

    curl dict://dict.org/find:curl

RFC'nin URL açıklamasını bozan (ancak DICT protokolünü bozmayan) komutlar şunlardır:

    curl dict://dict.org/show:db
    curl dict://dict.org/show:strat
