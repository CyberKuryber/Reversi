import random
from map import Map

class HashingMap(object):
    """
    Klasa modeluje heš mapu
    """

    def __init__(self, capacity=8):
        """
        Konstruktor

        Argumenti:
        - `capacity`: inicijalni broj mesta u lookup nizu
        - `prime`: prost broj neophodan heš funkciji
        """
        self._data = capacity * [None]
        self._capacity = capacity
        self._size = 0
        self.prime = 109345121

        # konstante heširanja
        self._a = 1 + random.randrange(self.prime-1)
        self._b = random.randrange(self.prime)

    def __len__(self):
        return self._size

    def _hash(self, x):
        """
        Heš funkcija

        Izračunavanje heš koda vrši se po formuli (ax + b) mod p.

        Argument:
        - `x`: vrednost čiji se kod računa
        """
        hashed_value = (hash(x)*self._a + self._b) % self.prime
        compressed = hashed_value % self._capacity
        return compressed

    def _resize(self, capacity):
        """
        Skaliranje broja raspoloživih slotova

        Metoda kreira niz sa unapred zadatim kapacitetom u koji
        se prepisuju vrednosti koje se trenutno nalaze u tabeli.

        Argument:
        - `capacity`: kapacitet novog niza
        """
        old_data = list(self.items())
        self._data = capacity * [None]
        self._size = 0

        # prepisivanje podataka u novu tabelu
        for (k, v) in old_data:
            self[k] = v

    def __getitem__(self, key):
        """
        Pristup elementu sa zadatim ključem

        Apstraktna metoda koja opisuje pristup elementu na osnovu
        njegovog ključa. Implementacija pristupa bucketu varira u
        zavisnosti od načina rešavanja kolizija.

        Argument:
        - `key`: ključ elementa kome se pristupa
        """
        bucket_index = self._hash(key)
        return self._bucket_getitem(bucket_index, key)

    def __setitem__(self, key, value):
        bucket_index = self._hash(key)
        self._bucket_setitem(bucket_index, key, value)

        # povećaj broj raspoloživih mesta
        current_capacity = len(self._data)
        if self._size > current_capacity // 2:
            self._resize(2*current_capacity - 1)

    def __delitem__(self, key):
        bucket_index = self._hash(key)
        self._bucket_delitem(bucket_index, key)

    def items(self):
        raise NotImplementedError()

    def _bucket_getitem(self, index, key):
        raise NotImplementedError()

    def _bucket_setitem(self, index, key, value):
        raise NotImplementedError()

    def _bucket_delitem(self, index, key):
        raise NotImplementedError()


class ChainedHashMap(HashingMap):
    """
    Klasa modeluje heš mapu koja kolizije rešava ulančavanjem
    """
    def _bucket_getitem(self, i, key):
        """
        Pristup elementu u okviru bucketa

        Metoda najpre pristupa bucketu sa zadatim indeksom. Ukoliko
        bucket postoji, pretražuje se. Ako je element pronađen metoda
        vraća njegovu vrednostu, dok se u suprotnom podiže odgovarajući
        izuzetak.

        Argumenti:
        - `i`: indeks bucketa
        - `key`: ključ elementa
        """
        bucket = self._data[i]
        if bucket is None:
            return None

        return bucket[key]

    def _bucket_setitem(self, bucket_index, key, value):
        """
        Postavljanje vrednosti elementa sa zadatim ključem

        Metoda najpre pronalazi bucket sa zadatim indeksom, a zatim
        dodaje novi element ili ažurira postojeći na osnovu zadatog
        ključa. Ukoliko bucket ne postoji, kreira se novi.

        Argumenti:
        - `i`: indeks bucketa
        - `key`: ključ elementa
        - `value`: vrednost elementa
        """
        bucket = self._data[bucket_index]
        if bucket is None:
            self._data[bucket_index] = Map()

        # broj elemenata u mapi se menja samo u slučaju da je došlo do
        # dodavanja, dok ažuriranje ne menja broj elemenata
        current_size = len(self._data[bucket_index])
        self._data[bucket_index][key] = value
        if len(self._data[bucket_index]) > current_size:
            self._size += 1

    def _bucket_delitem(self, bucket_index, key):
        """
        Brisanje elementa sa zadatim ključem

        Metoda najpre pristupa bucketu sa zadatim indeksom. Ukoliko
        bucket postoji, pretražuje se. Ako je element pronađen vrši
        se njegovo brisanje, u suprotnom se podiže odgovarajući
        izuzetak.

        Argumenti:
        - `i`: indeks bucketa
        - `key`: ključ elementa
        """
        bucket = self._data[bucket_index]
        if bucket is None:
            return None

        del bucket[key]
        self._size -= 1

    def __iter__(self):
        for bucket in self._data:
            if bucket is not None:
                for key in bucket:
                    yield key

    def items(self):
        for bucket in self._data:
            if bucket is not None:
                for key, value in bucket.items():
                    yield key, value

    def generate_hash_value(self,grid):
        value = 0
        white = 1
        black = 1000
        for i in range(8):
            for j in range(8):
                trenutni = 0
                if grid[i][j].color == 'w':
                    trenutni= white
                elif grid[i][j].color == 'b':
                    trenutni= black
                else: continue

                if j == 1 or j == 6:
                    trenutni *=2
                elif j == 2 or j == 5:
                    trenutni *=3
                elif j ==3 or j ==4:
                    trenutni *=4


                if i == 1 or i == 6:
                    trenutni *=2
                elif i == 2 or i == 5:
                    trenutni *= 3
                elif i ==3 or i ==4:
                    trenutni *=4

                value +=trenutni
        return value

