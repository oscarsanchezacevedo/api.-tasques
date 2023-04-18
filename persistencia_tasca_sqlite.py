#!usr/bin/python3
import sqlite3
import tasca

class Persitencia_tasca_sqlite():
    def __init__(self,ruta):
        self._ruta = ruta
        self._conn = sqlite3. connect(self._ruta)

    def desa(self, tasca):
        self._conn = sqlite3.connect(self._ruta)
        titol = tasca.titol 
        done = tasca.done
        resultat = None

        consulta = "INSERT INTO tasques"\
                    +"(titol, done)" \
                    + f"VALUES('{titol}', {done});"  #siempre para crear en sqlite3 hay que hacerlo: INSERT INTO nombretabla (campos a crear) VALUES (valores a crear);
        cursor = self._conn.cursor()
        try:
            cursor.execute(consulta)
            tasca.id = cursor.lastrowid
            resultat = tasca
        except sqlite3.IntegrityError:
            print("[X] IntegrityError: possiblement aquesta tasca ja está registrada.")
        self._conn.commit()
        self._conn.close
        cursor.close()
        return resultat
    
    def get_list(self):
        self._conn = sqlite3.connect(self._ruta)
        consulta = "SELECT rowid, titol, done FROM tasques;"
        cursor = self._conn.cursor()
        cursor.execute(consulta)
        llista = cursor.fetchall()
        resultat = []
        for registre in llista:
            tarea = tasca.Tasca(self, registre[1], registre[2], registre[0])
            resultat.append(tarea)
        self._conn.close
        return resultat

def main():
    persistencia = Persitencia_tasca_sqlite("deleteme.bd")
    una_tasca = tasca.Tasca(persistencia, "Comprar pa")
    print(persistencia.desa(una_tasca))
    tasques = persistencia.get_list()
    for taska in tasques:
        print(taska)
if __name__== "__main__":
    main()


