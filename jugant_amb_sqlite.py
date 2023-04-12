#!/usr/bin/python3

import sqlite3

RUTA_BD = "una_base_dades.bd"

def esborra_taules(conn):
    consulta = "DROP table if exists tasques;"
    cursor = conn.cursor()
    cursor.execute(consulta)
    conn.commit()
    cursor.close()

def crea_taules(conn):
    consulta = """CREATE table if not exists tasques(
    title text,
    done boolean
    );"""
    cursor = conn.cursor()
    cursor.execute(consulta)
    conn.commit()
    cursor.close()

def afegir_tasca(conn, titol, done=False):
    consulta = f"INSERT INTO tasques (title, done) VALUES('{titol}', {done});"
    cursor = conn.cursor()
    cursor.execute(consulta)
    conn.commit()
    cursor.close()

def main():
    print("Obrint conexió amb bbdd")
    conn = sqlite3.connect(RUTA_BD)
    esborra_taules(conn)
    crea_taules(conn)
    afegir_tasca(conn, "Ir a comprar el pan")
    conn.close()
    print("Conexió tancada.")

    

if __name__== "__main__":
    main()
