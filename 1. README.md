
# Table of Contents
- [Habit Tracker](#habit-tracker)
  * [Core Functionality](#core-functionality)
    + [Progress and Streak Tracking](#progress-and-streak-tracking)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installing](#installing)
    + [Packages for Running Tests](#packages-for-running-tests)
  * [How to Run the Program](#how-to-run-the-program)
  * [Running Tests](#running-tests)
- [Usage Guide](#usage-guide)
  * [Manage Habit or Category](#manage-habit-or-category)
    + [1. Create a Habit](#1-create-a-habit)
    + [2. Remove a Habit](#2-remove-a-habit)
    + [3. Delete a Category](#3-delete-a-category)
    + [4. Return to Main Menu](#4-return-to-main-menu)
  * [Change Habit's Periodicity](#change-habits-periodicity)
  * [Complete a Habit](#complete-a-habit)
  * [Display Habits (All or Sort by Periodicity)](#display-habits-all-or-sort-by-periodicity)
    + [1. Show All Habits](#1-show-all-habits)
    + [2. Show Daily Habits](#2-show-daily-habits)
    + [3. Show Weekly Habits](#3-show-weekly-habits)
    + [4. Show Monthly Habits](#4-show-monthly-habits)
    + [5. Return to Main Menu](#5-return-to-main-menu)
  * [Analytics](#analytics)
    + [1. Show All Habits' Streaks](#1-show-all-habits-streaks)
    + [2. Show Longest Streak of Specific Habit](#2-show-longest-streak-of-specific-habit)
    + [3. Show Streak Log of Specific Habit](#3-show-streak-log-of-specific-habit)
    + [4. Return to Main Menu](#4-return-to-main-menu-1)
  * [Exit](#exit)
- [Contributing](#contributing)

# Habit Tracker

Establishing and sustaining positive habits is essential for a healthy and successful life. Our Habit Tracker simplifies this process by helping you manage, monitor, and visualize your progress.

Developed as part of the IU Akademie DLBDSOOFPP01 course, this program utilizes Python 3.9.

## Core Functionality
The habit tracker allows you to:
* Create a habit
* Delete a habit or category
* Define periodicity of habits (Daily, Weekly, Monthly)
* Add habit categories for reference
* Mark habits as completed

### Progress and Streak Tracking
Additionally, you can:
* View all created habits
* View habits for a specific period
* View streaks of all habits
* View the longest streak of a specific habit
* View the streak history of a specific habit

# Getting Started
**Important**: Ensure Python 3.9+ is installed on your OS. Download the latest version of Python [here](https://www.python.org/downloads/).

## Prerequisites
* Python 3.9+

## Installing
Install Python from [here](https://www.python.org/downloads/) and ensure "ADD to path" is checked during installation.

Next, install the following libraries:

- Questionary:
  ```
  pip install questionary
  ```

### Packages for Running Tests
To run tests, install:
- Pytest:
  ```
  pip install -U pytest
  ```
- Freezegun:
  ```
  pip install freezegun
  ```

## How to Run the Program
After installing the prerequisites, download the repository files and navigate to the folder in your command/terminal window. Then run:
```
python main.py
```
For Python 3.9+:
```
python3 main.py
```

## Running Tests
To run tests, navigate to the test folder and run:
```
pytest
```

# Usage Guide
**Note**: The **main.db** file contains predefined habits: Zumba, XYZ.dancing, jumping.

## Manage Habit or Category
Add or remove habits and categories.

#### 1. Create a Habit
Launch the program and select:
```
create/remove Habit OR Category
```
Then choose *Add Habit* and enter the required information:
```
Would you like to Add, Remove Habit or Category? (Use arrow keys)
 » Add Habit
   Remove Habit
   Delete Category
   Back to Main Menu
```

#### 2. Remove a Habit
Select a habit from the list to delete it.

#### 3. Delete a Category
Select a category from the list to delete it.

#### 4. Return to Main Menu
Go back to the main menu.

## Change Habit's Periodicity
Select the habit you'd like to change and choose the new periodicity.

## Complete a Habit
Mark a habit as completed. A habit can only be marked once within its period. If not completed in time, the streak resets to 1.

## Display Habits (All or Sort by Periodicity)
Choose to view all habits or sort by periodicity.

#### 1. Show All Habits
Displays all created habits with their details.

#### 2. Show Daily Habits
Displays daily habits.

#### 3. Show Weekly Habits
Displays weekly habits.

#### 4. Show Monthly Habits
Displays monthly habits.

#### 5. Return to Main Menu
Go back to the main menu.

## Analytics
#### 1. Show All Habits' Streaks
Displays streaks for all habits.

#### 2. Show Longest Streak of Specific Habit
Displays the longest streak for a specific habit.

#### 3. Show Streak Log of Specific Habit
Displays the streak history for a specific habit.

#### 4. Return to Main Menu
Go back to the main menu.

## Exit
Exit the program.

# Contributing
Contributions are welcome! Fork the repository and submit a pull request. You can also open an issue labeled "enhancement." Don't forget to star the project!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.
