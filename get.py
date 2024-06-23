import questionary as qt

from db import connectDB, getCategories, get_habits_as_choices



def categoryDeleteConfirmation():
    
    return qt.confirm("Deleting the category will also delete all the assigned habits, "
                      "would you still like to proceed?").ask()


def periodicityChangeConfirmed():
   
    return qt.confirm("Changing periodicity of the habit will reset streak, would you like to continue?").ask()



def habitName():
    
    return qt.text("Please Enter the Name of Your Habit:",
                   validate=lambda name: True if name.isalpha() and len(name) > 1
                   else "Please enter a valid name").ask().lower()


def habitPeriodicity():
    
    return qt.select("Please Select Habit Periodicity",
                     choices=["Daily", "Weekly", "Monthly"]).ask().lower()


def habitCategory():
   
    return qt.text("Please Enter the Name of Your Category:",
                   validate=lambda category: True if category.isalpha() and len(category) > 1
                   else "Please enter a valid category").ask().lower()


def definedCategories():
    
    db = connectDB()
    arr = getCategories(db)
    if len(arr) > 0:
        return qt.select("Please Select a Category",
                         choices=sorted(arr)).ask().lower()
    else:
        raise ValueError("No categories found in Database; Please define a category using 'Add habit' function")




def habitsFromDb():
    
    db = connectDB()
    list_of_habits = get_habits_as_choices(db)
    if list_of_habits is not None:
        return qt.select("Please Select a Habit",
                         choices=sorted(list_of_habits)).ask().lower()
    else:
        raise ValueError("No habit in database; Add a habit first to use this function")


def habitDeleteConfirmation(habit_name_to_delete):
  
    return qt.confirm(f"Would you like to delete '{habit_name_to_delete}' habit from database?").ask()


def showPeriodChoices():
   
    choice = qt.select("Would you like to view all habits or sort habit by periodicity?",
                       choices=[
                           "View All Habits",
                           "View Daily Habits",
                           "View Weekly Habits",
                           "View Monthly Habits",
                           "Back to Main Menu"
                       ]).ask()
    return choice


def analyticsChoices():
    
    choice = qt.select("Please choose an option:",
                       choices=[
                           "View All Habit's Streaks",
                           "View Longest Streak of Specific Habit",
                           "View Streak Log of Specific Habit",
                           "Back to Main Menu"
                       ]).ask()
    return choice
