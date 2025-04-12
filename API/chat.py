from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi import FastAPI  # For running independently

# Import models
from models import Channel, Message, ChannelSubscription, ChannelType, ProContent, User, Professional

# Import schemas
from schemas import Channel, ChannelWithMessages, Message, MessageCreate, ChannelSubscription

# Import dependencies
from database import SessionLocal, get_db
from main import get_current_user  # Import the get_current_user dependency from main.py

# Create an APIRouter for the chat system
chat_router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

# Get a channel (for Learners to access course content or messages)
@chat_router.get("/channels/{channel_id}", response_model=ChannelWithMessages)
def get_channel(
    channel_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if the user has access to the channel
    channel_subscription = db.query(ChannelSubscription).filter(
        ChannelSubscription.channel_id == channel_id,
        ChannelSubscription.user_id == current_user.user_id
    ).first()
    if not channel_subscription:
        raise HTTPException(status_code=403, detail="Not authorized to access this channel")

    channel = db.query(Channel).filter(Channel.channel_id == channel_id).first()
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")

    # For course channels, include the course content in the response
    if channel.channel_type == ChannelType.COURSE:
        pro_content = db.query(ProContent).filter(ProContent.content_id == channel.related_id).first()
        if pro_content:
            # For simplicity, we'll add the course content as a "message" in the channel
            # In a real app, you might want to return the content directly in the channel response
            message = Message(
                channel_id=channel.channel_id,
                sender_id=channel.professional.user_id,
                content=pro_content.full_content
            )
            db.add(message)
            db.commit()

    return channel

# Send a message in a channel (for Professionals in group coaching or mentorship channels)
@chat_router.post("/channels/{channel_id}/messages", response_model=Message)
def send_message(
    channel_id: int,
    message_data: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    channel = db.query(Channel).filter(Channel.channel_id == channel_id).first()
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")

    # Only the Professional who owns the channel can send messages
    if channel.professional.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Only the Professional can send messages in this channel")

    # Only group coaching and mentorship channels support messaging
    if channel.channel_type not in [ChannelType.GROUP_COACHING, ChannelType.MENTORSHIP]:
        raise HTTPException(status_code=400, detail="Messaging is only supported for group coaching and mentorship channels")

    message = Message(
        channel_id=channel_id,
        sender_id=current_user.user_id,
        content=message_data.content
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

# Get all channels a user has access to
@chat_router.get("/users/{user_id}/channels", response_model=List[Channel])
def get_user_channels(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to view channels for another user")

    channels = db.query(Channel).join(ChannelSubscription).filter(ChannelSubscription.user_id == user_id).all()
    return channels

# Allow running chat.py independently for testing
if __name__ == "__main__":
    import uvicorn
    app = FastAPI()
    app.include_router(chat_router)
    uvicorn.run(app, host="127.0.0.1", port=8001)  # Use a different port to avoid conflict with main.py