import db
from datetime import datetime


class Habit:
  

    def __init__(self, name: str = None, periodicity: str = None, category: str = None, database="main.db"):
       

        self.name = name
        self.periodicity = periodicity
        self.category = category
        self.db = db.connectDB(database)
        self.streak = 0
        self.current_time = datetime.now().strftime("%m/%d/%Y %H:%M")

    def add(self):
      
        if db.habitExists(self.db, self.name) is False:
            db.addHabit(self.db, self.name, self.periodicity, self.category, self.current_time, self.streak)
            db.updateDB(self.db, self.name, False, 0, self.current_time)
            print(f"\nYour request to add '{self.name.capitalize()}' as '{self.periodicity.capitalize()}' "
                  f"Habit in '{self.category.capitalize()}' has been completed.\n")
        else:
            print("\nHabit already exists, please choose another habit.\n")

    def remove(self):
      
        db.removeHabit(self.db, self.name)
        print(f"\nDeleted '{self.name.capitalize()}' from database successfully.\n")

    def removeCategory(self):
        
        db.removeCategory(self.db, self.category)
        print(f"\nSuccessfully deleted the category '{self.category.capitalize()}'.\n")

    def changePeriodicity(self):
        
        db.updatePeriodicity(self.db, self.name, self.periodicity)
        db.updateDB(self.db, self.name, False, 0, self.current_time)
        print(f"\nChanged Periodicity of the Habit '{self.name.capitalize()}' to '{self.periodicity.capitalize()}'\n")

    def incrementStreak(self):
       
        self.streak = db.getStreakCount(self.db, self.name)
        self.streak += 1

    def resetStreak(self):
       
        self.streak = 1
        db.update_habit_streak(self.db, self.name, self.streak, self.current_time)
        db.updateDB(self.db, self.name, False, db.get_streak_count(self.db, self.name), self.current_time)
        print("\nOops! Looks like you missed your streak. Your streak has been reset.")
        print(f"Your new streak for Habit '{self.name.capitalize()}' is now {self.streak} because you completed it.\n")

    def updateStreak(self):
       
        self.incrementStreak()
        db.update_habit_streak(self.db, self.name, self.streak, self.current_time)
        db.updateDB(self.db, self.name, True, db.getStreakCount(self.db, self.name), self.current_time)
        print(f"\nGreat! Your new streak for habit '{self.name.capitalize()}' is {self.streak}\n")

    def markAsCompleted(self):
       
        
        if db.fetch_habit_streak_data(self.db, self.name) == "daily":
            if self.dailyHabitStreakVerification() == 0:
                print("\nYou have already completed this habit today, please try again tomorrow.\n")
            elif self.dailyHabitStreakVerification() == 1:
                self.updateStreak()
            else:
                self.resetStreak()

        
        elif db.fetch_habit_streak_data(self.db, self.name) == "weekly":
            if self.weeklyHabitStreakVerification() == 1:
                print("\nYou have already completed the habit this week, please try again next week.\n")
            elif self.weeklyHabitStreakVerification() == 2:
                self.updateStreak()
            else:
                self.resetStreak()

        
        elif db.fetch_habit_streak_data(self.db, self.name) == "monthly":
            if self.monthlyHabitStreakVerification() == 0:
                print("\nYou have already completed the habit this month, please try again next month.\n")
            elif self.monthlyHabitStreakVerification() == 1:
                self.updateStreak()
            else:
                self.resetStreak()

    def dailyHabitStreakVerification(self):
       
        last_visit = db.get_completion_time(self.db, self.name)
        previous_streak = db.getStreakCount(self.db, self.name)
        if previous_streak == 0 or last_visit is None:
            return 1
        else:
            today = self.current_time
            date = datetime.strptime(today[:10], "%m/%d/%Y") - datetime.strptime(last_visit[:10], "%m/%d/%Y")
            return date.days

    def weeklyHabitStreakVerification(self):
       
        lastStreak = db.get_completion_time(self.db, self.name)
        previousStreak = db.getStreakCount(self.db, self.name)
        if (previousStreak == 0) or (lastStreak is None):
            return 2
        else:
            today = self.current_time
            delt = datetime.strptime(today[:10], "%m/%d/%Y") - datetime.strptime(lastStreak[:10], "%m/%d/%Y")
            week = 3 if (delt.days + 1) > 14 else (2 if (delt.days + 1) > 7 else 1)
            return week

    def monthlyHabitStreakVerification(self):
        
        lastVisit = db.get_completion_time(self.db, self.name)
        previousStreak = db.getStreakCount(self.db, self.name)
        if (previousStreak == 0) or (lastVisit is None):
            return 1
        else:
            currentMonth = self.current_time
            m = int(currentMonth[:2]) - int(lastVisit[:2])
            print(m)
            return m
