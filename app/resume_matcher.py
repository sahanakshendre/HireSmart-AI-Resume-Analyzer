import PyPDF2

def extract_text_from_pdf(path):
    text = ""
    with open(path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text


def calculate_match(resume_text, job_description):

    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())

    match = resume_words.intersection(job_words)

    score = len(match) / len(job_words) * 100

    return round(score, 2), list(match)[:10]