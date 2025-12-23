from app.models import Appointment
from app.database import AsyncSessionLocal

async def save_appointment(data: dict):
    async with AsyncSessionLocal() as db:
        appointment = Appointment(
            email=data["email"],
            appointment_type=data["appointment_type"],
            reason=data["reason"],
            slot=data["selected_slot"]
        )
        db.add(appointment)
        await db.commit()
