import random
from datetime import datetime

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don't watch the clock; do what it does. Keep going.",
    "Dream it. Wish it. Do it.",
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Sometimes later becomes never. Do it now."
]

quote = random.choice(quotes)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("🕯️ QuoteFlame 🕯️")
print(f"[{now}] 🔥 {quote}")
