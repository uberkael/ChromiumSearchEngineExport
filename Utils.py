import sqlite3
import json


def print_filas(filas):
    for fila in filas:
        print(fila)


def db_read_keywords(cursor):
    """read from the search engine database"""
    cursor.execute('SELECT * FROM keywords;')
    return cursor.fetchall()


def db_insertar_filas(conn, cursor, filas):
    """insert into the search engine"""
    cursor.executemany('''
        INSERT OR IGNORE INTO keywords (
            id, short_name, keyword, favicon_url, url, safe_for_autoreplace, originating_url,
            date_created, usage_count, input_encodings, suggest_url, prepopulate_id, created_by_policy,
            last_modified, sync_guid, alternate_urls, image_url, search_url_post_params,
            suggest_url_post_params, image_url_post_params, new_tab_url, last_visited,
            created_from_play_api, is_active, starter_pack_id, enforced_by_policy, featured_by_policy
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', filas)
    conn.commit()


def json_write(filas):
    with open('keywords.json', 'w') as f:
        json.dump(filas, f)


def json_read(f):
    with open(f, 'r') as file:
        filas = json.load(file)
        return filas


def comparar_datos(filas1, filas2):
    if len(filas1) != len(filas2):
        return False, "Las dimensiones externas no coinciden."

    for i in range(len(filas1)):
        if len(filas1[i]) != len(filas2[i]):
            return False, f"Las dimensiones internas no coinciden en la fila {i}."

        for j in range(len(filas1[i])):
            if filas1[i][j] != filas2[i][j]:
                return False, f"Diferencia encontrada en la fila {i}, columna {j}: {filas1[i][j]} != {filas2[i][j]}"

    return True, "Los arrays son iguales."


def add_spaces(lista, spaces=5):
    return [item + ' ' * spaces for item in lista]


if __name__ == "__main__":
    database = 'EdgeMal/Web Data'
    file_extract = 'keywords.json'

    # Connect to the database
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()

        # filas_a = db_read_keywords(cursor)

        # print_filas(filas)
        # json_write(filas)

        # filas = json_read(file_extract)

        # print_filas(filas)

        # print(comparar_datos(filas_a, filas))
        # db_insertar_filas(conn, cursor, filas)
