from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Bug(Base):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'bug'
    id = Column(Integer, primary_key=True)
    bug_tracker_url = Column(String, unique=True)
    root_cause = Column(String)
    who = Column(String)
    when = Column(DateTime, default=func.now())

    # def __repr__(self):
    #     return 'id: {}, root cause: {}'.format(self.id, self.root_cause)