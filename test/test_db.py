
from db import addHabit, connectDB, get_habits_as_choices, habitExists, removeHabit, getCategories, updatePeriodicity, fetch_habit_streak_data, getStreakCount,update_habit_streak


class TestDatabase:
 

    def setup_method(self):
        self.db = connectDB("test_db.db")
        
        addHabit(self.db, "coding", "daily", "career", "01/01/2024 12:00", 0)
        addHabit(self.db, "Zumba", "daily", "career", "01/02/2024 12:00", 0)
        addHabit(self.db, "gym", "daily", "career", "01/02/2024 12:00", 0)
        addHabit(self.db, "Cycling", "weekly", "atmosphere", "02/01/2024 12:00", 0)
        addHabit(self.db, "Painting", "monthly", "growth", "02/01/2024 12:00", 0)
        addHabit(self.db, "Walking", "daily", "games", "01/01/2024 12:00", 0)

    def test_fetch_habits_as_choices(self):
        assert len(get_habits_as_choices(self.db)) == 6

    def test_update_habit_streak(self):
        update_habit_streak(self.db, "coding", 1, "01/02/2022 13:00")
        assert getStreakCount(self.db, "coding") == 1

    

    def test_remove_habit(self):
        removeHabit(self.db, "gaming")
        assert habitExists(self.db, "gaming") is False
        assert len(get_habits_as_choices(self.db)) == 5

    def teardown_method(self):
        self.db.close()
        import os
        os.remove("test_db.db")

    
    def test_update_periodicity(self):
        updatePeriodicity(self.db, "reflection", "weekly")
        assert fetch_habit_streak_data(self.db, "reflection") == "weekly"

    
    def test_fetch_categories(self):
        assert len(getCategories(self.db)) == 4

