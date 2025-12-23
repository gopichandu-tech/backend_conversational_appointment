from datetime import datetime, timedelta

def recommend_slots(preference: str):
    """
    Returns 3-5 available slots for a given time preference (morning/afternoon/evening)
    with actual upcoming dates.
    """
    now = datetime.now()
    slots = []

    times = {
        "morning": ["09:00 AM", "10:00 AM", "11:00 AM"],
        "afternoon": ["01:00 PM", "02:30 PM", "03:30 PM"],
        "evening": ["05:00 PM", "06:00 PM", "07:00 PM"]
    }

    pref_times = times.get(preference.lower(), times["morning"])

    for i in range(1, 4):
        day = now + timedelta(days=i)
        day_name = day.strftime("%A")
        date_str = day.strftime("%b %d") 
        for t in pref_times:
            slots.append(f"{day_name}, {date_str} {t}")

    return slots[:3]
