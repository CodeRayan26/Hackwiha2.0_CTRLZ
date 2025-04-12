from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    account_type = Column(Enum("free", "premium"), default="free")
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    creator = relationship("Creator", back_populates="user", uselist=False)
    pro = relationship("Professional", back_populates="user", uselist=False)

class Creator(Base):
    __tablename__ = "creators"
    creator_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), unique=True)
    nin_number = Column(String(50))
    id_card_front_url = Column(String(255))
    id_card_back_url = Column(String(255))
    specialty = Column(String(100))
    is_verified = Column(Boolean, default=False)

    user = relationship("User", back_populates="creator")

class Professional(Base):
    __tablename__ = "professionals"
    professional_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), unique=True)
    diploma_url = Column(String(255))
    diploma_issuer = Column(String(100))
    certification_url = Column(String(255))
    specialty = Column(String(100))
    is_verified = Column(Boolean, default=False)

    user = relationship("User", back_populates="pro")

class FeedContent(Base):
    __tablename__ = "feed_content"

    content_id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey("creators.creator_id"), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)  # Changed from Text to String
    content_type = Column(Enum('post', 'mini_course', 'full_course'), nullable=False)
    is_featured = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)