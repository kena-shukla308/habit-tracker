import pytest
from habit import Habit
# from db import add_habit, connect_database, fetch_habits_as_choices, habit_exists, remove_habit, \
#     fetch_categories, update_periodicity, fetch_habit_periodicity, update_habit_streak, get_streak_count
from freezegun import freeze_time
from db import addHabit, connectDB, get_habits_as_choices, habitExists, removeHabit, getCategories, updatePeriodicity, getStreakCount, update_habit_streak,fetch_habit_streak_data


@pytest.fixture(scope='module')
def db():
    print('\n*****SETUP*****\n')
    db = connectDB("test_habit.db")
    print("Created temporary test_habit.db for test purpose.\n")
    print("Initiating tests...\n")
    yield db
    print('******TEARDOWN******')
    print("\nClosing connection with test database...\n")
    db.close()
    print("Connection successfully terminated!")
    import os
    os.remove("test_habit.db")
    print("\nDeleted test_habit.db file.")
    print("\nTest completed :)")


def test_add(db):
    habit = Habit("coding", "daily", "career", database="test_habit.db")
    habit.add()
    habit1 = Habit("cooking", "daily", "food", database="test_habit.db")
    habit1.add()
    assert habitExists(db, "coding")
    assert habitExists(db, "cooking")





def test_change_periodicity(db):
    assert fetch_habit_streak_data(db, "cooking") == "daily"
    habit1 = Habit("cooking", "weekly", database="test_habit.db")
    habit1.changePeriodicity()
    assert fetch_habit_streak_data(db, "cooking") == "weekly"


def test_remove(db):
    assert habitExists(db, "coding") is True
    habit = Habit("coding", "daily", "career", database="test_habit.db")
    habit.remove()
    assert habitExists(db, "coding") is False


def test_delete_category(db):
    assert len(getCategories(db)) == 1
    habit3 = Habit("netflix", "daily", "entertainment", database="test_habit.db")
    habit3.add()
    assert len(getCategories(db)) == 2
    habit3.removeCategory()
    assert len(getCategories(db)) == 1


# Time format (YYYY-MM-DD)
@freeze_time("2022-01-01")
def test_add_custom_habits(db):
    habit4 = Habit("book", "daily", "knowledge", database="test_habit.db")
    habit4.add()
    habit5 = Habit("fishing", "weekly", "food", database="test_habit.db")
    habit5.add()
    habit6 = Habit("guitar", "monthly", "music", database="test_habit.db")
    habit6.add()
    assert habitExists(db, "book")






@freeze_time("2022-01-01")
def test_mark_habit6_as_completed(db):
    habit6 = Habit("guitar", "monthly", "music", database="test_habit.db")
    habit6.markAsCompleted()
    assert getStreakCount(db, "guitar") == 1



@freeze_time("2022-01-01")
def test_mark_habit4_as_completed(db):
    habit4 = Habit("book", "daily", "knowledge", database="test_habit.db")
    habit4.markAsCompleted()
    assert getStreakCount(db, "book") == 1


@freeze_time("2022-01-01")
def test_mark_habit4_as_completed_again(db):
    habit4 = Habit("book", "daily", "knowledge", database="test_habit.db")
    habit4.markAsCompleted()
    assert getStreakCount(db, "book") != 2


@freeze_time("2022-01-02")
def test_mark_habit4_as_completed_next_day(db):
    habit4 = Habit("book", "daily", "knowledge", database="test_habit.db")
    habit4.markAsCompleted()
    assert getStreakCount(db, "book") == 2




# Testing 10 days later
@freeze_time("2022-01-10")
def test_mark_habit6_as_completed_10days_later(db):
    habit6 = Habit("guitar", "monthly", "music", database="test_habit.db")
    habit6.markAsCompleted()
    assert getStreakCount(db, "guitar") != 2


# Testing a month later
@freeze_time("2022-02-10")
def test_mark_habit6_as_completed_month_later(db):
    habit6 = Habit("guitar", "monthly", "music", database="test_habit.db")
    habit6.markAsCompleted()
    assert getStreakCount(db, "guitar") == 2


@freeze_time("2022-01-01")
def test_mark_habit5_as_completed(db):
    assert getStreakCount(db, "fishing") == 0
    habit5 = Habit("fishing", "weekly", "food", database="test_habit.db")
    habit5.markAsCompleted()
    assert getStreakCount(db, "fishing") == 1


# Testing a day later
@freeze_time("2022-01-02")
def test_mark_habit5_as_completed_next_day(db):
    habit5 = Habit("fishing", "weekly", "food", database="test_habit.db")
    habit5.markAsCompleted()
    assert getStreakCount(db, "fishing") != 2


# Testing a week later
@freeze_time("2022-01-08")
def test_mark_habit5_as_completed_next_week(db):
    habit5 = Habit("fishing", "weekly", "food", database="test_habit.db")
    habit5.markAsCompleted()
    assert getStreakCount(db, "fishing") == 2
