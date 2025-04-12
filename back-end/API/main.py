from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User, Creator, Professional, FeedContent  # Make sure to import FeedContent
from database import get_db, Base, engine
from schemas import UserCreate, UserOut, UserUpdate, FeedContentCreate, FeedContent  # Import UserUpdate and FeedContent schemas
from auth import hash_password, verify_password

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register", response_model=UserOut)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter((User.username == user_data.username) | (User.email == user_data.email)).first():
        raise HTTPException(status_code=400, detail="Username or email already exists")

    hashed_pw = hash_password(user_data.password)
    user = User(username=user_data.username, email=user_data.email, password_hash=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)

    role = "learner"
    return UserOut(**user.__dict__, role=role)

@app.post("/login", response_model=UserOut)
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Detect role
    if user.creator:
        role = "creator"
    elif user.pro:
        role = "pro"
    else:
        role = "learner"

    return UserOut(**user.__dict__, role=role)

@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Determine user role
    role = "learner"
    if user.creator:
        role = "creator"
    elif user.pro:
        role = "pro"

    return UserOut(**user.__dict__, role=role)

@app.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update user attributes
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.add(user)
    db.commit()
    db.refresh(user)

    # Determine user role
    role = "learner"
    if user.creator:
        role = "creator"
    elif user.pro:
        role = "pro"

    return UserOut(**user.__dict__, role=role)

@app.get("/feed", response_model=list[FeedContent])
def get_feed(db: Session = Depends(get_db)):
    feed_content = db.query(FeedContent).all()
    return feed_content

@app.post("/feed", response_model=FeedContent)
def create_feed_content(content_data: FeedContentCreate, db: Session = Depends(get_db)):
    #  Authorization:  Check if the user is a creator (You'll need to implement authentication first)
    #  Example (replace with your authentication/authorization logic):
    #  current_user = get_current_user(db)  # Function to get the authenticated user
    #  if current_user.creator is None:
    #      raise HTTPException(status_code=403, detail="Only creators can create feed content")

    feed_content = FeedContent(
        creator_id=content_data.creator_id,  #  Get creator_id from the authenticated user
        title=content_data.title,
        content=content_data.content,
        content_type=content_data.content_type
    )
    db.add(feed_content)
    db.commit()
    db.refresh(feed_content)
    return feed_content



