import uuid

sessions = {}

def create_session():
    session_id = str(uuid.uuid4())
    sessions[session_id] = {"phase": 1, "data": {}}
    return session_id

def get_session(session_id):
    return sessions.get(session_id)
