def get_athlete_from_id(athlete_id):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name, dob FROM athletes WHERE id=?""",
                                     (athlete_id,))
    (name, dob) = results.fetchone()
    results = cursor.execute("""SELECT value FROM timing_data WHERE athlete_id=?""",
                                     (athlete_id,))
    data = [row[0] for row in results.fetchall()]
    response = {'Name':   name,
                'DOB':    dob,
                'data':   data,
                'top3':   data[0:3]}
    connection.close()
    return(response)