from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class Visits(Base):
    __tablename__ = "visits"

    page = Column(String, primary_key=True,  index=True)
    count = Column(Integer)
    last_visit = Column(DateTime)

    def __repr__(self):
        return f"<Visits(page={self.page},\
                count={self.count},\
                last_visit={self.last_visit})>"
