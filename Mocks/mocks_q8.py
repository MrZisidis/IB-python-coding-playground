def add_session(total_minutes, minutes):
    if not isinstance(minutes, int) or minutes <= 0:
        return total_minutes
    return total_minutes + minutes

def status(total_minutes):
    if total_minutes < 30:
        return "Start"
    elif total_minutes < 60:
        return "Good"
    elif total_minutes < 120:
        return "Strong"
    else:
        return "Excellent"

total_minutes = 0

while True:
    s = input("Minutes studied (or 'q' to quit): ").strip().lower()
    if s == "q":
        break
    try:
        minutes = int(s)
        total_minutes = add_session(total_minutes, minutes)
    except ValueError:
        pass

print(total_minutes)
print(status(total_minutes))