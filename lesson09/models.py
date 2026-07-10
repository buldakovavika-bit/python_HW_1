from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200))
    students = relationship(
        "Student", secondary="student_courses", back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name})>"
