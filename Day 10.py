import datetime
import os
import random

STREAK_FILE = "cricket_streak.txt"

cricket_quotes = [
    "🏏 'You don’t play for the crowd, you play for the country.' – MS Dhoni",
    "🔥 'Every ball is an opportunity. Make it count!'",
    "💪 'Practice like you’ve never won. Play like you’ve never lost.'",
    "🎯 'Coding is like batting – timing is everything!'",
    "🚀 'One good shot can change the game. One good day can change your streak!'"
]

def get_today():
    return datetime.date.today()

def read_streak():
    if not os.path.exists(STREAK_FILE):
        return 0, None
    with open(STREAK_FILE, "r") as f:
        lines = f.readlines()
        streak = int(lines[0].strip())
        last_date = datetime.datetime.strptime(lines[1].strip(), "%Y-%m-%d").date()
        return streak, last_date

def write_streak(streak, last_date):
    with open(STREAK_FILE, "w") as f:
        f.write(f"{streak}\n{last_date}\n")

def update_streak():
    today = get_today()
    streak, last_date = read_streak()

    if last_date == today:
        print("🏏 You already played your 'coding innings' today! Keep scoring runs!")
    elif last_date == today - datetime.timedelta(days=1):
        streak += 1
        write_streak(streak, today)
        print(f"🔥 What a shot! You're on a {streak}-day coding streak!")
    else:
        print("😢 Oh no! You missed a day. Your streak is reset.")
        streak = 1
        write_streak(streak, today)
        print("🏁 New innings started! Let's build a big score!")

    print(random.choice(cricket_quotes))

if __name__ == "__main__":
    update_streak()

