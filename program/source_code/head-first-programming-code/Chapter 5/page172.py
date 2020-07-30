import sqlite3 
def find_details(id2find): 
    db = sqlite3.connect("surfersDB.sdb") 
    db.row_factory = sqlite3.Row 
    cursor = db.cursor() 
    cursor.execute("select * from surfers") 
    rows = cursor.fetchall() 
    for row in rows: 
        if row['id'] == id2find: 
            s = {} 
            s['id']      = str(row['id']) 
            s['name']    = row['name'] 
            s['country'] = row['country'] 
            s['average'] = str(row['average']) 
            s['board']   = row['board'] 
            s['age']     = str(row['age']) 
            cursor.close() 
            return(s) 
    cursor.close() 
    return({})

lookup_id = int(input("Enter the id of the surfer: ")) 
surfer = find_details(lookup_id) 
if surfer: 
    print("ID:         " + surfer['id']) 
    print("Name:       " + surfer['name']) 
    print("Country:    " + surfer['country']) 
    print("Average:    " + surfer['average']) 
    print("Board type: " + surfer['board']) 
    print("Age:        " + surfer['age'])
