# initialize the database
conpath = path + '/chathistory.db'
def initdb():
    conn = sqlite3.connect(conpath)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS history (role, parts)')
    conn.commit()
    conn.close()

# add entry
def add_message(role, parts):
    conn = sqlite3.connect(conpath)
    c = conn.cursor()
    c.execute('INSERT INTO history VALUES (?, ?)', (role, parts))
    conn.commit()
    conn.close()

# retrieve entry
def get_messages():
    conn = sqlite3.connect(conpath)
    c = conn.cursor()
    c.execute('SELECT * FROM history')
    messages = c.fetchall()
    conn.close()
    if messages == []:
        return []
    else:
        output = []
        for i in messages:
            output.append({
                'role': i[0],
                'parts': [i[1]]
            })
        return output

# empty database
def clear_messages():
    conn = sqlite3.connect(conpath)
    c = conn.cursor()
    c.execute('DELETE FROM history')
    conn.commit()
    conn.close()
