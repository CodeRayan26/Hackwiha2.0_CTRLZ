from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import Enum

# Define ChannelType as an Enum for the schema
class ChannelType(str, Enum):
    course = "course"
    group_coaching = "group_coaching"
    mentorship = "mentorship"

# User-related schemas
class UserBase(BaseModel):
    username: str
    email: str
    password: str  # Note: In production, this should be password_hash
    account_type: str

class UserCreate(UserBase):
    pass

class UserOut(BaseModel):
    user_id: int
    username: str
    email: str
    account_type: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    email: Optional[str] = None
    account_type: Optional[str] = None

# Creator-related schemas
class LearnerToCreator(BaseModel):
    nin_number: str
    id_card_front_url: str
    id_card_back_url: str
    specialty: Optional[str] = None
    specialty_proof_url: Optional[str] = None

class CreatorProfile(BaseModel):
    creator_id: int
    user_id: int
    nin_number: str
    id_card_front_url: str
    id_card_back_url: str
    specialty: Optional[str] = None
    specialty_proof_url: Optional[str] = None
    is_verified: bool
    verification_date: Optional[datetime] = None

    class Config:
        from_attributes = True

# Professional-related schemas
class ProfessionalCreate(BaseModel):
    diploma_url: Optional[str] = None
    diploma_issuer: Optional[str] = None
    certification_url: Optional[str] = None
    years_experience: Optional[int] = None
    specialty: Optional[str] = None

class Professional(BaseModel):
    professional_id: int
    user_id: int
    diploma_url: Optional[str] = None
    diploma_issuer: Optional[str] = None
    certification_url: Optional[str] = None
    years_experience: Optional[int] = None
    specialty: Optional[str] = None
    is_verified: bool
    verification_date: Optional[datetime] = None

    class Config:
        from_attributes = True

# Feed content schemas
class FeedContentBase(BaseModel):
    title: str
    content: str
    content_type: str

class FeedContentCreate(FeedContentBase):
    pass

class FeedContent(FeedContentBase):
    content_id: int
    creator_id: int
    is_featured: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class FeedMediaBase(BaseModel):
    media_url: str
    media_type: str
    display_order: int = 0

class FeedMediaCreate(FeedMediaBase):
    pass

class FeedMedia(FeedMediaBase):
    media_id: int
    content_id: int

    class Config:
        from_attributes = True

class FeedContentWithMedia(FeedContent):
    media: List[FeedMedia] = []

# Professional content schemas
class ProContentBase(BaseModel):
    title: str
    description: str
    full_content: str
    preview_content: str
    content_type: str
    price: int
    is_featured: bool

class ProContentCreate(ProContentBase):
    pass

class ProContent(ProContentBase):
    content_id: int
    professional_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Professional plan schemas
class ProfessionalPlanBase(BaseModel):
    plan_type: str
    name: str
    description: str
    price: int
    duration_days: int
    is_active: bool

class ProfessionalPlanCreate(ProfessionalPlanBase):
    pass

class ProfessionalPlan(ProfessionalPlanBase):
    plan_id: int
    professional_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Subscription schemas
class SubscriptionBase(BaseModel):
    payment_method: str
    transaction_id: str

class SubscriptionCreate(SubscriptionBase):
    pass

class Subscription(SubscriptionBase):
    subscription_id: int
    user_id: int
    plan_id: int

    class Config:
        from_attributes = True

# Group coaching schemas
class GroupCoachingBase(BaseModel):
    title: str
    description: str
    capacity: int
    price: int

class GroupCoachingCreate(GroupCoachingBase):
    pass

class GroupCoaching(GroupCoachingBase):
    coaching_id: int
    professional_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Mentorship schemas
class MentorshipBase(BaseModel):
    title: str
    description: str
    price: int

class MentorshipCreate(MentorshipBase):
    pass

class Mentorship(MentorshipBase):
    mentorship_id: int
    professional_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Channel-related schemas
class ChannelBase(BaseModel):
    channel_type: ChannelType
    related_id: int
    professional_id: int

class ChannelCreate(ChannelBase):
    pass

class Channel(ChannelBase):
    channel_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    message_id: int
    channel_id: int
    sender_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ChannelSubscriptionBase(BaseModel):
    channel_id: int
    user_id: int

class ChannelSubscriptionCreate(ChannelSubscriptionBase):
    pass

class ChannelSubscription(ChannelSubscriptionBase):
    subscription_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ChannelWithMessages(Channel):
    messages: List[Message] = []