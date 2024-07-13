import questionary as qt
import get
from habit import Habit
import analytics


print("""
*** Habit Tracker ***
""")



def menu():
   
   
    choice = qt.select(
        "select any option you want to perform",
        choices=[
            "Add/Remove Habit OR Category",
            "Modify Habit's Periodicity",
            "Mark Habit as Completed",
            "Show Habits (All or Sort by Periodicity)",
            "Analytics",
            "Exit"
        ]).ask()

    if choice == "Add/Remove Habit OR Category":
       
        second_choice = qt.select(
            "Would you like to Add, Remove Habit or Category?",
            choices=[
                "Add Habit",
                "Remove Habit",
                "Delete Category",
                "Back to Main Menu"
            ]).ask()

        if second_choice == "Add Habit":
            habit_name = get.habitName()
            habit_periodicity = get.habitPeriodicity()
            habit_category = get.habitCategory()
            habit = Habit(habit_name, habit_periodicity, habit_category)
            habit.add()

        elif second_choice == "Remove Habit":
            try:
                habit_name = get.habitsFromDb()
            except ValueError:  
                print("\nNo habit found in database: Please add a habit first.\n")
            else:
                habit = Habit(habit_name)
                if get.habitDeleteConfirmation(habit_name):
                    habit.remove()
                else:
                    print("\nNo problem! We all get confused sometimes :)\n")

        elif second_choice == "Delete Category":
            try:
                habit_category = get.definedCategories()
            except ValueError:  
                print("\nNo category found! Please add a habit & category using the 'Add habit' function.\n")
            else:
                if get.categoryDeleteConfirmation():
                    habit = Habit(category=habit_category)
                    habit.removeCategory()
                else:
                    print("\nThanks for confirming!\n")

        elif second_choice == "Back to Main Menu":
            menu()

    elif choice == "Modify Habit's Periodicity":
        try:
            habit_name = get.habitsFromDb()
        except ValueError:  
            print("\nDatabase empty; Please add a habit first.\n")
        else:
            new_periodicity = get.habitPeriodicity()
            if get.periodicityChangeConfirmed():
                habit = Habit(habit_name, new_periodicity)
                habit.changePeriodicity()
            else:
                print(f"\nPeriodicity of {habit_name} remains unchanged! Thanks for confirming.\n")

    elif choice == "Mark Habit as Completed":
        try:
            habit_name = get.habitsFromDb()
        except ValueError:  
            print("\nNo habit defined; please add a habit first to complete it!\n")
        else:
            habit = Habit(habit_name)
            habit.markAsCompleted()

    elif choice == "Show Habits (All or Sort by Periodicity)":
        second_choice = get.showPeriodChoices()  
        if second_choice == "View All Habits":
            analytics.show_habits_info()  #
        elif second_choice == "View Daily Habits":
            analytics.show_habits_info("daily")
        elif second_choice == "View Weekly Habits":
            analytics.show_habits_info("weekly")
        elif second_choice == "View Monthly Habits":
            analytics.show_habits_info("monthly")
        elif second_choice == "Back to Main Menu":
            menu()

    elif choice == "Analytics":
        second_choice = get.analyticsChoices()
        if second_choice == "View All Habit's Streaks":
            analytics.show_streak_info()
        elif second_choice == "View Longest Streak of Specific Habit":
            try:
                habit_name = get.habitsFromDb()
            except ValueError:  
                print("\nNo habit data found in the database; Please add a habit first\n")
            else:
                analytics.show_streak_info(habit_name)
        elif second_choice == "View Streak Log of Specific Habit":
            try:
                habit_name = get.habitsFromDb()
            except ValueError:  
                print("\nNo habit log found; Please add a habit first\n")
            else:
                analytics.show_habit_logged_data(habit_name)
        elif second_choice == "Back to Main Menu":
            menu()

    elif choice == "Exit":
        print("\nGoodbye! Remember to maintain your habit streaks!") 
        exit()  


if __name__ == "__main__":
    while True:
        menu()
