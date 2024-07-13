from db import connectDB


def info_of_all_habits(db) -> list:

    current = db.cursor()
    current.execute("SELECT * FROM habit_tracker")
    records = current.fetchall()
    return records


def info_of_custom_periodicity_habits(db, periodicity) -> list:
    
    current = db.cursor()
    query = "SELECT * FROM habit_tracker WHERE periodicity = ?"
    current.execute(query, (periodicity,))
    rec = current.fetchall()
    return rec


def info_of_single_habit(db, habit_name) -> list:
    
    current = db.cursor()
    query = "SELECT * FROM habit_tracker WHERE habit = ?"
    current.execute(query, (habit_name,))
    rec = current.fetchall()
    return rec


def longest_streak(db, habit_name) -> int:
    
    current = db.cursor()
    query = "SELECT MAX(streak) FROM habit_log WHERE habit = ?"
    current.execute(query, (habit_name,))
    info = current.fetchone()
    return info[0]


def habit_log(db, habit_name) -> list:
    
    current = db.cursor()
    query = "SELECT * FROM habit_log WHERE habit = ?"
    current.execute(query, (habit_name,))
    rec = current.fetchall()
    return rec



def show_habits_info(periodicity=None):
    
    db = connectDB()
    if periodicity is not None:
        data = info_of_custom_periodicity_habits(db, periodicity)
    else:
        data = info_of_all_habits(db)
    if len(data) > 0:
        
        print("\n{:<10} {:<15} {:<10} {:<15}".format("Name", "Periodicity", "Category", "Date/Time"))
        print("-------------------------------------------------------")
        for row in data:
            print("{:<10} {:<15} {:<10} {:<15}".format(
                row[0].capitalize(),  
                row[1].capitalize(),  
                row[2].capitalize(),  
                row[3].capitalize()))  
        print("-------------------------------------------------------\n")

    else:
        print("\nNo habit found in the specified periodicity!\n")



def show_streak_info(habit=None):
    

    db = connectDB()
    if habit is None:
        data = info_of_all_habits(db)
    else:
        data = info_of_single_habit(db, habit)
    if len(data) > 0:
        
        print("\n{:<10} {:^15} {:>10} {:>10}".format("Name |", "Periodicity |", "Completion Time |",
                                                     "Current Streak" if habit is None else "Longest Streak"))
        print(f"{'_' * 70}")  
        for row in data:
            period = " Day(s)" if row[1] == "daily" else (" Week(s)" if row[1] == "weekly" else " Month(s)")
            print("{:<10} {:^15} {:>10} {:^15}".format(
                row[0].capitalize(),  
                row[1].capitalize(),  
                row[5] if row[5] is not None else "--/--/-- --:--",  
                str(row[4]) + period if habit is None else str(longest_streak(db, habit)) + period))  
            print(f"{'_' * 70}\n")
    else:
        print("\nNo Habit Found; Please Add a Habit First!\n")



def show_habit_logged_data(name_of_habit):
   
    db = connectDB()
    data = habit_log(db, name_of_habit)
    print(f"\n{'-' * 75}")  
    if len(data) > 0:
        for row in data:
            print(f"Habit: {row[0].capitalize()} | "
                  f"Completed : {'True' if row[1] == 1 else 'False'} | "
                  f"Streak: {row[2]} | Logged at: {row[3]}")
    else:
        print("No record found!")
    print(f"{'-' * 75}\n")
