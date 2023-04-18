#!usr/bin/python3
import sqlite3
import tasca

class Persitencia_tasca_sqlite():
    def __init__(self,ruta):
        self._ruta = ruta
        if not self.existeixen_taules():
             self.reset_database()
       

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
    
    def modifica_tasca(self,tasca):
        resultat = None
        self._conn = sqlite3.connect(self._ruta)
        titol = tasca.titol
        done = tasca._done
        id = tasca._id
        consulta = f"UPDATE TASQUES set done={done}, titol='{titol}' where rowid={id};"
        cursor = self._conn.cursor()
        try:
            cursor.execute(consulta)
        except sqlite3.IntegrityError:
            print("[X] IntegrityError: possiblemenent aquest titol ja existeix.")
        self._conn.commit()
        cursor.close()
        self._conn.close()
        return resultat 
    
    def esborra_tasca(self,id):
        self._conn = sqlite3.connect(self._ruta)
        consulta = f"delete from tasques where rowid={id};"
        cursor = self._conn.cursor()
        cursor.execute(consulta)
        self._conn.commit()
        cursor.close
        self._conn.close()
    
    def existeixen_taules(self):
        self._conn = sqlite3.connect(self._ruta)
        consulta = "SELECT * FROM tasques LIMIT 1;"
        cursor = self._conn.cursor()
        try:
            cursor.execute(consulta)
        except sqlite3.OperationalError:
             return False
        cursor.close()
        self._conn.close
        return True    
       
    def reset_database(self):
        self._conn = sqlite3.connect(self._ruta)
        cursor = self._conn.cursor()
        consulta = "DROP TABLE if exists tasques;"
        cursor.execute(consulta)
        consulta = f"CREATE TABLE if not exists tasques(titol TEXT UNIQUE, done BOOLEAN);"
        cursor.execute(consulta)
        self._conn.commit()
        cursor.close()
        self._conn.close

def main():
    id = None
    titol = "Fer la bugada"
    persistencia = Persitencia_tasca_sqlite("deleteme.bd")
    una_tasca = tasca.Tasca(persistencia, titol)
    print(persistencia.desa(una_tasca))
    tasques = persistencia.get_list()
    for taska in tasques:
        print(taska)
        if taska.titol == titol:
            id = taska.id
            taska.titol = "Refer la bugada"
            taska.done = True
            persistencia.modifica_tasca(taska)
            print("------taska modificada---------")
    tasques = persistencia.get_list()
    print("\n\n---lista de tasques:---")
    for taska in tasques:
        print(taska)
    if id: 
        persistencia.esborra_tasca(id)
        print("----taska esborrada---")
if __name__== "__main__":
    main()


