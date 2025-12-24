# 🏥 Clinico – Conversational Appointment Backend

This repository contains the **backend service** for the Clinico conversational appointment booking system.  
It provides a chat-based API built with **FastAPI**, integrates with **PostgreSQL**, and generates **Calendly booking links**.


## 🌐 Live Demo
#### Frontend URL : [Frontend Demo](https://frontend-conversational-appointment-cz7mrl05d.vercel.app/)
#### Backend URL  : [Backend Demo](https://backend-conversational-appointment.onrender.com/docs)

---

## 🚀 Features

- 💬 Conversational appointment workflow
- 🧠 Session-based chat handling
- 📅 Smart time-slot suggestions
- 🔗 Calendly booking link generation
- 🗄 PostgreSQL database integration
- 🌐 CORS-enabled for frontend access
- ☁️ Deployed on Render

---

## 🛠 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **SQLAlchemy (Async)**
- **asyncpg**
- **PostgreSQL**
- **python-dotenv**

---

## 📂 Project Structure
<img width="281" height="409" alt="image" src="https://github.com/user-attachments/assets/d6842f89-3bd7-4135-a500-df096cb53897" />

---

## 📦 Prerequisites

- **Python 3.10 or higher**
- **PostgreSQL**
- **pip** or **virtualenv**

Check:
```bash
python --version
```

## ⚙️ Installation & Setup
### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/backend-repo-name.git
cd backend-repo-name
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Running the Server
Development
```bash
uvicorn app.main:app --reload
```

### Production
```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

### 📡 API Endpoint
```bash
POST /chat

Request

{
  "message": "Hello",
  "session_id": null
}
```

```bash
Response

{
  "reply": "👋 Hi there! Welcome to our clinic.",
  "session_id": "uuid-string"
}
```

### 🧠 Chat Flow

Email collection

Reason for visit

Appointment type

Time preference

## 👨‍💻 Author

Gopi Chandu

Slot suggestions

Confirmation

Calendly booking link generation
