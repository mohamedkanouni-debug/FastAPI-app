from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON, func
from sqlalchemy.orm import relationship
from db.database import Base

class Story(Base) :
    __tablename__ = "story"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    session_id = Column(String , index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    nodes = relationship("StoryNode" , back_populates="story")
    

class StoryNode(Base):
    __tablename__ = "story_node"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer , ForeignKey("story.id") , index=True)
    content = Column(String)
    is_root = Column(Boolean , default=False)
    is_ending = Column(Boolean , default=False)
    is_winning = Column(Boolean , default=False)
    options = Column(JSON , default=list)
    story = relationship("Story" , back_populates="nodes")
