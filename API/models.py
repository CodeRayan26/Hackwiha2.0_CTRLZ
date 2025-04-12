from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import enum

# Define an Enum for channel types
class ChannelType(str, enum.Enum):
    COURSE = "course"
    GROUP_COACHING = "group_coaching"
    MENTORSHIP = "mentorship"

# Add the Channel model
class Channel(Base):
    __tablename__ = "channels"

    channel_id = Column(Integer, primary_key=True, index=True)
    channel_type = Column(Enum(ChannelType), nullable=False)  # "course", "group_coaching", or "mentorship"
    related_id = Column(Integer, nullable=False)  # ID of the related entity (e.g., ProContent.content_id, GroupCoaching.coaching_id, Mentorship.mentorship_id)
    professional_id = Column(Integer, ForeignKey("professionals.professional_id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    professional = relationship("Professional", back_populates="channels")
    messages = relationship("Message", back_populates="channel")
    channel_subscriptions = relationship("ChannelSubscription", back_populates="channel")

# Add the Message model
class Message(Base):
    __tablename__ = "messages"

    message_id = Column(Integer, primary_key=True, index=True)
    channel_id = Column(Integer, ForeignKey("channels.channel_id"), nullable=False)
    sender_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    channel = relationship("Channel", back_populates="messages")
    sender = relationship("User")

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    account_type = Column(String(20), nullable=False)  # e.g., "free", "premium"
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    creator = relationship("Creator", uselist=False, back_populates="user")
    professional = relationship("Professional", uselist=False, back_populates="user")
    subscriptions = relationship("Subscription", back_populates="user")
    channel_subscriptions = relationship("ChannelSubscription", back_populates="user")

class Creator(Base):
    __tablename__ = "creators"

    creator_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), unique=True, nullable=False)
    nin_number = Column(String(50), nullable=False)
    id_card_front_url = Column(String(255), nullable=False)
    id_card_back_url = Column(String(255), nullable=False)
    specialty = Column(String(100), nullable=True)
    specialty_proof_url = Column(String(255), nullable=True)
    is_verified = Column(Boolean, default=False, nullable=False)
    verification_date = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="creator")
    feed_contents = relationship("FeedContent", back_populates="creator")

class Professional(Base):
    __tablename__ = "professionals"

    professional_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), unique=True, nullable=False)
    diploma_url = Column(String(255), nullable=True)
    diploma_issuer = Column(String(100), nullable=True)
    certification_url = Column(String(255), nullable=True)
    years_experience = Column(Integer, nullable=True)
    specialty = Column(String(100), nullable=True)
    is_verified = Column(Boolean, default=False, nullable=False)
    verification_date = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="professional")
    plans = relationship("ProfessionalPlan", back_populates="professional")
    pro_contents = relationship("ProContent", back_populates="professional")
    group_coachings = relationship("GroupCoaching", back_populates="professional")
    mentorships = relationship("Mentorship", back_populates="professional")
    channels = relationship("Channel", back_populates="professional")

class FeedContent(Base):
    __tablename__ = "feed_content"

    content_id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey("creators.creator_id"), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    content_type = Column(String(50), nullable=False)  # e.g., "post", "mini_course", "full_course"
    is_featured = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    creator = relationship("Creator", back_populates="feed_contents")
    media = relationship("FeedMedia", back_populates="content")

class FeedMedia(Base):
    __tablename__ = "feed_media"

    media_id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer, ForeignKey("feed_content.content_id"), nullable=False)
    media_url = Column(String(255), nullable=False)
    media_type = Column(String(50), nullable=False)  # e.g., "image", "video"
    display_order = Column(Integer, default=0, nullable=False)

    content = relationship("FeedContent", back_populates="media")

class ProContent(Base):
    __tablename__ = "pro_content"

    content_id = Column(Integer, primary_key=True, index=True)
    professional_id = Column(Integer, ForeignKey("professionals.professional_id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    full_content = Column(Text, nullable=False)
    preview_content = Column(Text, nullable=False)
    content_type = Column(String(50), nullable=False)  # e.g., "full_course", "coaching", "mentorship"
    price = Column(Integer, nullable=False)  # Price in cents
    is_featured = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    professional = relationship("Professional", back_populates="pro_contents")

class ProfessionalPlan(Base):
    __tablename__ = "professional_plans"

    plan_id = Column(Integer, primary_key=True, index=True)
    professional_id = Column(Integer, ForeignKey("professionals.professional_id"), nullable=False)
    plan_type = Column(String(50), nullable=False)  # e.g., "monthly", "yearly"
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)  # Price in cents
    duration_days = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    professional = relationship("Professional", back_populates="plans")
    subscriptions = relationship("Subscription", back_populates="plan")

class Subscription(Base):
    __tablename__ = "subscriptions"

    subscription_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    plan_id = Column(Integer, ForeignKey("professional_plans.plan_id"), nullable=False)
    payment_method = Column(String(50), nullable=False)
    transaction_id = Column(String(100), nullable=False)

    user = relationship("User", back_populates="subscriptions")
    plan = relationship("ProfessionalPlan", back_populates="subscriptions")

class GroupCoaching(Base):
    __tablename__ = "group_coaching"

    coaching_id = Column(Integer, primary_key=True, index=True)
    professional_id = Column(Integer, ForeignKey("professionals.professional_id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    capacity = Column(Integer, nullable=False)  # Maximum number of participants
    price = Column(Integer, nullable=False)  # Price in cents
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    professional = relationship("Professional", back_populates="group_coachings")

class Mentorship(Base):
    __tablename__ = "mentorships"

    mentorship_id = Column(Integer, primary_key=True, index=True)
    professional_id = Column(Integer, ForeignKey("professionals.professional_id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)  # Price in cents
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    professional = relationship("Professional", back_populates="mentorships")

class ChannelSubscription(Base):
    __tablename__ = "channel_subscriptions"

    subscription_id = Column(Integer, primary_key=True, index=True)
    channel_id = Column(Integer, ForeignKey("channels.channel_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    channel = relationship("Channel", back_populates="channel_subscriptions")
    user = relationship("User")