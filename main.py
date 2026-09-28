from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import engine, get_db, Base
from models import Student
from schemas import StudentCreate, StudentResponse


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API"
)


#Create Student

@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = Student(
        name=student.name,
        email=student.email,
        course=student.course,
        age=student.age
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# Get All Students

@app.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_students(db: Session = Depends(get_db)):

    students = db.query(Student).all()

    return students

#GET - Get Student By ID

@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


#Update Student

@app.put(
    "/students/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = student_data.name
    student.email = student_data.email
    student.course = student_data.course
    student.age = student_data.age

    db.commit()
    db.refresh(student)

    return student


#Delete Student


@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }


# Search By Course

@app.get(
    "/students/search",
    response_model=list[StudentResponse]
)
def search_students(
    course: str,
    db: Session = Depends(get_db)
):

    students = (
        db.query(Student)
        .filter(Student.course.ilike(f"%{course}%"))
        .all()
    )

    return students