from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import joinedload
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Import models
from models import (
    Base, User, Creator, Professional, FeedContent, FeedMedia, ProContent,
    ProfessionalPlan, Subscription, GroupCoaching, Mentorship,
    Channel, Message, ChannelSubscription, ChannelType
)

# Import schemas
from schemas import (
    UserCreate, UserOut, UserUpdate, LearnerToCreator, ProfessionalCreate,
    FeedContentCreate, FeedContent, FeedMediaCreate, FeedMedia, FeedContentWithMedia,
    ProContentCreate, ProContent, ProfessionalPlanCreate, ProfessionalPlan,
    SubscriptionCreate, Subscription, CreatorProfile,
    GroupCoachingCreate, GroupCoaching, MentorshipCreate, Mentorship,
    ChannelCreate, Channel, MessageCreate, Message, ChannelSubscriptionCreate,
    ChannelSubscription, ChannelWithMessages, ChannelType
)

from database import SessionLocal
from auth import get_db, get_current_user, hash_password, verify_password, create_access_token, OAuth2PasswordRequestForm

# Import the chat router
from chat import chat_router

app = FastAPI()

# Include the chat router
app.include_router(chat_router)

# Login endpoint
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    access_token_expires = timedelta(minutes=30)  # Use the same value as ACCESS_TOKEN_EXPIRE_MINUTES
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

# Existing endpoints (unchanged for brevity)
@app.post("/register/learner", response_model=UserOut)
def register_learner(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    existing_email = db.query(User).filter(User.email == user_data.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_pw = hash_password(user_data.password)
    user = User(
        username=user_data.username, 
        email=user_data.email, 
        password_hash=hashed_pw, 
        account_type=user_data.account_type
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return UserOut(user_id=user.user_id, username=user.username, email=user.email, account_type=user.account_type, created_at=user.created_at, updated_at=user.updated_at)

@app.post("/register/professional", response_model=UserOut)
def register_professional(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    existing_email = db.query(User).filter(User.email == user_data.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_pw = hash_password(user_data.password)
    user = User(
        username=user_data.username, 
        email=user_data.email, 
        password_hash=hashed_pw, 
        account_type=user_data.account_type
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    pro = Professional(user_id=user.user_id)
    db.add(pro)
    db.commit()
    db.refresh(pro)

    return UserOut(user_id=user.user_id, username=user.username, email=user.email, account_type=user.account_type, created_at=user.created_at, updated_at=user.updated_at)

@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserOut(user_id=user.user_id, username=user.username, email=user.email, account_type=user.account_type, created_at=user.created_at, updated_at=user.updated_at)

@app.put("/feed/media/{media_id}", response_model=FeedMedia)
def update_feed_media(
    media_id: int,
    media_data: FeedMediaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    media = db.query(FeedMedia).filter(FeedMedia.media_id == media_id).first()
    if not media:
        raise HTTPException(status_code=404, detail="Media item not found")

    content = db.query(FeedContent).filter(FeedContent.content_id == media.content_id).first()
    if content.creator_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this media")

    for key, value in media_data.dict(exclude_unset=True).items():
        setattr(media, key, value)

    db.commit()
    db.refresh(media)
    return media

@app.get("/feed/{content_id}/media", response_model=List[FeedMedia])
def get_feed_media(
    content_id: int,
    db: Session = Depends(get_db)
):
    content = db.query(FeedContent).filter(FeedContent.content_id == content_id).first()
    if not content:
        raise HTTPException(status_code=404, detail="Feed content not found")
    
    media_items = db.query(FeedMedia).filter(FeedMedia.content_id == content_id).all()
    return media_items

@app.post("/feed/{content_id}/media", response_model=FeedMedia)
def create_feed_media(
    content_id: int,
    media_data: FeedMediaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    content = db.query(FeedContent).filter(FeedContent.content_id == content_id).first()
    if not content:
        raise HTTPException(status_code=404, detail="Feed content not found")

    if content.creator_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to add media to this content")

    media = FeedMedia(**media_data.dict(), content_id=content_id)
    db.add(media)
    db.commit()
    db.refresh(media)
    return media

@app.post("/users/{user_id}/become_creator", response_model=UserOut)
def become_creator(user_id: int, creator_data: LearnerToCreator, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.creator:
        raise HTTPException(status_code=400, detail="User is already a creator")

    creator = Creator(
        user_id=user_id,
        nin_number=creator_data.nin_number,
        id_card_front_url=creator_data.id_card_front_url,
        id_card_back_url=creator_data.id_card_back_url,
        specialty=creator_data.specialty,
        specialty_proof_url=creator_data.specialty_proof_url
    )
    db.add(creator)
    db.commit()
    db.refresh(creator)

    return UserOut(user_id=user.user_id, username=user.username, email=user.email, account_type=user.account_type, created_at=user.created_at, updated_at=user.updated_at)

@app.delete("/feed/media/{media_id}", response_model=dict)
def delete_feed_media(
    media_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    media = db.query(FeedMedia).filter(FeedMedia.media_id == media_id).first()
    if not media:
        raise HTTPException(status_code=404, detail="Media item not found")

    content = db.query(FeedContent).filter(FeedContent.content_id == media.content_id).first()
    if content.creator_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this media")

    db.delete(media)
    db.commit()
    return {"message": "Media item deleted successfully"}

@app.get("/feed/{content_id}", response_model=FeedContentWithMedia)
def get_feed_content_with_media(content_id: int, db: Session = Depends(get_db)):
    content = db.query(FeedContent).filter(FeedContent.content_id == content_id).options(joinedload(FeedContent.media)).first()
    if not content:
        raise HTTPException(status_code=404, detail="Feed content not found")
    return content

@app.post("/professionals/{professional_id}/content", response_model=ProContent)
def create_pro_content(
    professional_id: int,
    content_data: ProContentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    professional = db.query(Professional).filter(Professional.professional_id == professional_id).first()
    if not professional:
        raise HTTPException(status_code=404, detail="Professional not found")
    
    if professional.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to create content for this professional")

    content = ProContent(**content_data.dict(), professional_id=professional_id)
    db.add(content)
    db.commit()
    db.refresh(content)
    return content

@app.get("/professionals/{professional_id}/content", response_model=List[ProContent])
def get_pro_content(professional_id: int, db: Session = Depends(get_db)):
    professional = db.query(Professional).filter(Professional.professional_id == professional_id).first()
    if not professional:
        raise HTTPException(status_code=404, detail="Professional not found")
    
    contents = db.query(ProContent).filter(ProContent.professional_id == professional_id).all()
    return contents

@app.post("/professionals/{professional_id}/plans", response_model=ProfessionalPlan)
def create_professional_plan(
    professional_id: int,
    plan_data: ProfessionalPlanCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    professional = db.query(Professional).filter(Professional.professional_id == professional_id).first()
    if not professional:
        raise HTTPException(status_code=404, detail="Professional not found")
    
    if professional.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to create plans for this professional")

    plan = ProfessionalPlan(**plan_data.dict(), professional_id=professional_id)
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan

@app.get("/professionals/{professional_id}/plans", response_model=List[ProfessionalPlan])
def get_professional_plans(professional_id: int, db: Session = Depends(get_db)):
    professional = db.query(Professional).filter(Professional.professional_id == professional_id).first()
    if not professional:
        raise HTTPException(status_code=404, detail="Professional not found")
    
    plans = db.query(ProfessionalPlan).filter(ProfessionalPlan.professional_id == professional_id).all()
    return plans

@app.post("/users/{user_id}/subscribe/{plan_id}", response_model=Subscription)
def create_subscription(
    user_id: int,
    plan_id: int,
    subscription_data: SubscriptionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to subscribe for this user")

    plan = db.query(ProfessionalPlan).filter(ProfessionalPlan.plan_id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    if not plan.is_active:
        raise HTTPException(status_code=400, detail="This plan is not active")

    existing_subscription = db.query(Subscription).filter(
        Subscription.user_id == user_id,
        Subscription.plan_id == plan_id
    ).first()
    if existing_subscription:
        raise HTTPException(status_code=400, detail="User already subscribed to this plan")

    subscription = Subscription(**subscription_data.dict(), user_id=user_id, plan_id=plan_id)
    db.add(subscription)
    db.commit()
    db.refresh(subscription)

    # Determine the channel type based on the plan
    professional = db.query(Professional).filter(Professional.professional_id == plan.professional_id).first()
    channel_type = None
    related_id = None

    if "course" in plan.description.lower():
        channel_type = ChannelType.course
        pro_content = db.query(ProContent).filter(ProContent.professional_id == plan.professional_id).first()
        related_id = pro_content.content_id if pro_content else None
    elif "coaching" in plan.description.lower():
        channel_type = ChannelType.group_coaching
        group_coaching = db.query(GroupCoaching).filter(GroupCoaching.professional_id == plan.professional_id).first()
        related_id = group_coaching.coaching_id if group_coaching else None
    elif "mentorship" in plan.description.lower():
        channel_type = ChannelType.mentorship
        mentorship = db.query(Mentorship).filter(Mentorship.professional_id == plan.professional_id).first()
        related_id = mentorship.mentorship_id if mentorship else None

    if channel_type and related_id:
        # Create a channel
        channel = Channel(
            channel_type=channel_type,
            related_id=related_id,
            professional_id=plan.professional_id
        )
        db.add(channel)
        db.commit()
        db.refresh(channel)

        # Grant the user access to the channel
        channel_subscription = ChannelSubscription(
            channel_id=channel.channel_id,
            user_id=user_id
        )
        db.add(channel_subscription)
        db.commit()

    return subscription

@app.get("/users/{user_id}/subscriptions", response_model=List[Subscription])
def get_user_subscriptions(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to view subscriptions for this user")

    subscriptions = db.query(Subscription).filter(Subscription.user_id == user_id).all()
    return subscriptions

@app.put("/users/{user_id}/profile", response_model=UserOut)
def update_user_profile(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this profile")

    for key, value in user_data.dict(exclude_unset=True).items():
        if key == "password":
            value = hash_password(value)
            setattr(user, "password_hash", value)
        else:
            setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return UserOut(user_id=user.user_id, username=user.username, email=user.email, account_type=user.account_type, created_at=user.created_at, updated_at=user.updated_at)

@app.get("/creators/{creator_id}/profile", response_model=CreatorProfile)
def get_creator_profile(creator_id: int, db: Session = Depends(get_db)):
    creator = db.query(Creator).filter(Creator.creator_id == creator_id).first()
    if not creator:
        raise HTTPException(status_code=404, detail="Creator not found")
    
    return creator

@app.post("/admin/creators/{creator_id}/promote-to-pro", response_model=UserOut)
def promote_to_pro(creator_id: int, db: Session = Depends(get_db)):
    creator = db.query(Creator).filter(Creator.creator_id == creator_id).first()
    if not creator:
        raise HTTPException(status_code=404, detail="Creator not found")
    
    user = db.query(User).filter(User.user_id == creator.user_id).first()
    if user.professional:
        raise HTTPException(status_code=400, detail="User is already a Professional")

    professional = Professional(
        user_id=user.user_id,
        is_verified=True,
        verification_date=datetime.utcnow()
    )
    db.add(professional)
    db.commit()
    db.refresh(professional)

    return UserOut(user_id=user.user_id, username=user.username, email=user.email, account_type=user.account_type, created_at=user.created_at, updated_at=user.updated_at)

@app.post("/professionals/{professional_id}/coaching", response_model=GroupCoaching)
def create_group_coaching(
    professional_id: int,
    coaching_data: GroupCoachingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    professional = db.query(Professional).filter(Professional.professional_id == professional_id).first()
    if not professional:
        raise HTTPException(status_code=404, detail="Professional not found")
    
    if professional.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to create coaching for this professional")

    coaching = GroupCoaching(**coaching_data.dict(), professional_id=professional_id)
    db.add(coaching)
    db.commit()
    db.refresh(coaching)
    return coaching

@app.get("/professionals/{professional_id}/coaching", response_model=List[GroupCoaching])
def get_group_coaching(professional_id: int, db: Session = Depends(get_db)):
    professional = db.query(Professional).filter(Professional.professional_id == professional_id).first()
    if not professional:
        raise HTTPException(status_code=404, detail="Professional not found")
    
    coachings = db.query(GroupCoaching).filter(GroupCoaching.professional_id == professional_id).all()
    return coachings

@app.post("/professionals/{professional_id}/mentorship", response_model=Mentorship)
def create_mentorship(
    professional_id: int,
    mentorship_data: MentorshipCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    professional = db.query(Professional).filter(Professional.professional_id == professional_id).first()
    if not professional:
        raise HTTPException(status_code=404, detail="Professional not found")
    
    if professional.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to create mentorship for this professional")

    mentorship = Mentorship(**mentorship_data.dict(), professional_id=professional_id)
    db.add(mentorship)
    db.commit()
    db.refresh(mentorship)
    return mentorship

@app.get("/professionals/{professional_id}/mentorship", response_model=List[Mentorship])
def get_mentorship(professional_id: int, db: Session = Depends(get_db)):
    professional = db.query(Professional).filter(Professional.professional_id == professional_id).first()
    if not professional:
        raise HTTPException(status_code=404, detail="Professional not found")
    
    mentorships = db.query(Mentorship).filter(Mentorship.professional_id == professional_id).all()
    return mentorships

@app.get("/feed", response_model=List[FeedContentWithMedia])
def get_feed(sort: str = "recent", content_type: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(FeedContent).options(joinedload(FeedContent.media))
    
    if content_type:
        query = query.filter(FeedContent.content_type == content_type)
    
    if sort == "recent":
        query = query.order_by(FeedContent.created_at.desc())

    contents = query.all()
    return contents

@app.get("/feed/search", response_model=List[FeedContentWithMedia])
def search_feed(query: str, db: Session = Depends(get_db)):
    contents = db.query(FeedContent).options(joinedload(FeedContent.media))\
        .filter(FeedContent.title.ilike(f"%{query}%")).all()
    return contents

@app.get("/admin/creators/{creator_id}/metrics")
def get_creator_metrics(creator_id: int, db: Session = Depends(get_db)):
    creator = db.query(Creator).filter(Creator.creator_id == creator_id).first()
    if not creator:
        raise HTTPException(status_code=404, detail="Creator not found")
    
    post_count = db.query(FeedContent).filter(FeedContent.creator_id == creator_id).count()
    
    return {"creator_id": creator_id, "post_count": post_count}