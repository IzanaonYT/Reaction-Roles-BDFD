from pydantic import BaseModel


class RoleData(BaseModel):
    channel_id: str
    message_id: str
    emoji: str
    role_id: str