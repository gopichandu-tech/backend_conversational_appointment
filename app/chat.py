from app.slots import recommend_slots
from app.calendly import create_calendly_booking
from app.users import user_exists, save_user
import random

async def handle_message(session, message: str):
    if not session:
        return "⚠️ Oops! Your session expired. Please refresh and start again."

    phase = session["phase"]
    data = session["data"]

    if phase == 1:
        session["phase"] = 2
        greetings = [
            "👋 Hi there! Welcome to our clinic.",
            "Hello! Nice to see you here. 😊",
            "Hey! Hope you're having a good day. 👋"
        ]
        greeting = random.choice(greetings)
        return f"{greeting} To get started, could you please share your email address?"
    
    if phase == 2:
        if "@" not in message:
            return "⚠️ Hmm, that doesn't look like a valid email. Could you try again?"
        data["email"] = message
        if await user_exists(message):
            session["phase"] = 1
            return "📌 Looks like you already have an appointment with this email. Check your Calendly confirmation."
        session["phase"] = 3
        return "Great! Could you briefly tell me why you’d like to see a doctor today?"

    if phase == 3:
        data["reason"] = message
        session["phase"] = 4
        return "Thanks for sharing! What type of appointment would you like? (e.g., General Checkup, Consultation, Follow-up)"


    if phase == 4:
        data["appointment_type"] = message
        session["phase"] = 5
        return "Awesome! Do you have a preferred time for your appointment? (Morning / Afternoon / Evening)"
    
    if phase == 5:
        data["time_preference"] = message
        slots = recommend_slots(message)
        session["slots"] = slots
        session["phase"] = 6

        slot_text = "\n".join([f"• {s}" for s in slots])
        return (
            f"Here are some slots we suggest based on your preferred time ({message}):\n{slot_text}\n\n"
            "We picked these because they match your preferred part of the day and are currently available.\n"
            "Do any of these work for you? If not, just reply NO and we can find alternative dates and times."
        )

    if phase == 6:
        suggested_slots = session.get("slots", [])

        if "no" in message.lower():
            previous_pref = data.get("time_preference", "").lower()
            alternatives = ["morning", "afternoon", "evening"]
            if previous_pref in alternatives:
                alternatives.remove(previous_pref)
            alt_pref = random.choice(alternatives)
            alt_slots = recommend_slots(alt_pref)
            session["slots"] = alt_slots
            alt_slot_text = "\n".join([f"• {s}" for s in alt_slots])
            return (
                f"No worries! Here are some alternative slots for {alt_pref}:\n{alt_slot_text}\n\n"
                f"These slots are suggested based on availability during the {alt_pref}."
            )

        if message not in suggested_slots:
            slot_text = "\n".join([f"• {s}" for s in suggested_slots])
            return (
                "⚠️ Hmm, that doesn’t match any of the suggested slots. "
                "Please pick one from the list below:\n" + slot_text
            )

        data["selected_slot"] = message
        session["phase"] = 7
        return "Perfect! Can I have your full name, please?"

    if phase == 7:
        data["name"] = message
        session["phase"] = 8
        return f"Thanks {data['name']}! Could you provide your phone number as well?"


    if phase == 8:
        data["phone"] = message
        session["phase"] = 9
        return (
            "Almost done! Here’s a summary of your appointment:\n\n"
            f"Name: {data['name']}\n"
            f"Email: {data['email']}\n"
            f"Phone: {data['phone']}\n"
            f"Appointment Type: {data['appointment_type']}\n"
            f"Selected Slot: {data['selected_slot']}\n\n"
            "Reply YES to confirm, or NO if you’d like to change something."
        )

    if phase == 9:
        if message.lower() != "yes":
            session["phase"] = 1
            return "No problem! Let’s start over and get the details right. 😊"
        link = create_calendly_booking(data)
        await save_user(data)
        session["phase"] = 1
        return (
            f"🎉 Fantastic, {data['name']}! Your appointment is confirmed.\n\n"
            f"📅 Please complete your booking here: {link}\n\n"
            "You’ll receive a confirmation email shortly. See you soon! 👋"
        )
