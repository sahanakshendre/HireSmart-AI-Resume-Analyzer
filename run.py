from app import create_app, db
from app.models import Job

app = create_app()

with app.app_context():

    if Job.query.count() == 0:

        jobs = [
            Job(title="Python Developer", description="Work with Flask and APIs"),
            Job(title="Web Developer", description="HTML CSS Bootstrap required"),
            Job(title="Data Analyst", description="Python Pandas SQL"),
            Job(title="Backend Developer", description="Python Django APIs SQL"),
            Job(title="Machine Learning Engineer", description="Python ML Tensorflow"),
        ]

        for job in jobs:
            db.session.add(job)

        db.session.commit()
        print("Jobs inserted successfully")

if __name__ == "__main__":
    app.run(debug=True)