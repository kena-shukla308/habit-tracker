import sqlite3


def connectDB(name="main.db"):

    db = sqlite3.connect(name)
    buildTables(db)
    return db


def buildTables(db):

    current = db.cursor()
    current.execute('''
        CREATE TABLE IF NOT EXISTS habit_tracker (
               habit TEXT PRIMARY KEY , 
               periodicity TEXT,
               category TEXT,
               creation_time TEXT,
               streak INT,
               completion_time TEXT   
           )''')

    current.execute('''
        CREATE TABLE IF NOT EXISTS habit_log (
            habit TEXT,
            completed BOOL,
            streak INT DEFAULT 0,
            completion_time TIME,
            FOREIGN KEY (habit) REFERENCES habit_tracker(habit)
        )''')
    db.commit()


def addHabit(db, name, periodicity, category, creation_time, streak, completion_time=None):
  
    current = db.cursor()
    current.execute("INSERT INTO habit_tracker VALUES(?, ?, ?, ?, ?, ?)",
                (name, periodicity, category,
                 creation_time, streak, completion_time))
    db.commit()


def updateDB(db, name, is_completed, streak, completion_time):
    
    current = db.cursor()
    current.execute("INSERT INTO habit_log VALUES(?, ?, ?, ?)",
                (name, is_completed, streak, completion_time))
    db.commit()


def habitExists(db, habit_name):
    
    current = db.cursor()
    query = """SELECT * FROM habit_tracker WHERE habit = ?"""
    current.execute(query, (habit_name,))
    info = current.fetchone()
    return True if info is not None else False


def removeHabit(db, habit_name):
    
    current = db.cursor()
    current.execute(f"DELETE FROM habit_tracker WHERE habit == '{habit_name}';")
    db.commit()
    reset_logs(db, habit_name)


def getCategories(db):
    
    current = db.cursor()
    current.execute("SELECT category FROM habit_tracker")
    info = current.fetchall()
    return [i[0].capitalize() for i in set(info)]



def getStreakCount(db, habit_name):
    
    current = db.cursor()
    query = "SELECT streak FROM habit_tracker WHERE habit = ?"
    current.execute(query, (habit_name,))
    count = current.fetchall()
    return count[0][0]


def update_habit_streak(db, habit_name, streak, time=None):
   
    current = db.cursor()
    query = "UPDATE habit_tracker SET streak = ?, completion_time = ? WHERE habit = ?"
    info = (streak, time, habit_name)
    current.execute(query, info)
    db.commit()


def reset_logs(db, habit_name):
    
    current = db.cursor()
    query = "DELETE FROM habit_log WHERE habit = ?"
    current.execute(query, (habit_name,))
    db.commit()


def get_completion_time(db, habit_name):
    
    current = db.cursor()
    query = "SELECT completion_time FROM habit_tracker WHERE habit = ?"
    current.execute(query, (habit_name,))
    info = current.fetchall()
    return info[0][0]


def fetch_habit_streak_data(db, habit_name):
    
    current = db.cursor()
    query = "SELECT periodicity FROM habit_tracker WHERE habit =?"
    current.execute(query, (habit_name,))
    info = current.fetchall()
    return info[0][0]

def removeCategory(db, category_name):
    
    current = db.cursor()
    current.execute(f"DELETE FROM habit_Tracker where category == '{category_name}';")
    db.commit()


def get_habits_as_choices(db):
    
    current = db.cursor()
    current.execute("SELECT habit FROM habit_tracker")
    info = current.fetchall()
    return [i[0].capitalize() for i in set(info)] if len(info) > 0 else None


def updatePeriodicity(db, habit_name, new_periodicity):
   
    current = db.cursor()
    query = "UPDATE habit_tracker SET periodicity = ?, streak = 0, completion_time = NULL WHERE habit = ?"
    info = (new_periodicity, habit_name)
    current.execute(query, info)
    db.commit()
    reset_logs(db, habit_name)


