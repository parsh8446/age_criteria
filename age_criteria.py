import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta


def check_exam_eligibility(dob, std_class):
    exams = {
        "Sainik School": [(10, 12)],  # Age 10-12 for Class 6
        "RMS (Rashtriya Military Schools)": [(10, 12), (13, 15)],  # Class 6 and 9
        "Jawahar Navodaya Vidyalaya (JNV)": [(9, 13)],  # Class 6
        "Scindia School Scholarship": [(10, 14)],
        "KVPY (for Class 11 & 12)": [(16, 18)],
    }

    eligible_exams = {}
    today = datetime.date.today()
    current_age = relativedelta(today, dob).years

    for exam, age_ranges in exams.items():
        for age_range in age_ranges:
            if age_range[0] <= current_age <= age_range[1]:
                if exam not in eligible_exams:
                    eligible_exams[exam] = []
                eligible_exams[exam].append(f"Current Age: {current_age}, Suitable for Class {std_class}")

    return eligible_exams


# Streamlit UI
st.set_page_config(page_title="Competitive Exam Eligibility Checker", page_icon="🎓", layout="wide")

st.title("🎓 Competitive Exam Eligibility Checker for Students")
st.markdown("Find out which competitive exams a student is eligible for based on age and class.")

# User Input
col1, col2 = st.columns(2)
with col1:
    dob = st.date_input("📅 Enter Student's Date of Birth:", min_value=datetime.date(2005, 1, 1),
                        max_value=datetime.date(2020, 12, 31))
with col2:
    std_class = st.selectbox("📖 Select Current Class:", list(range(1, 12)))

if st.button("Check Eligibility 🏆"):
    eligible_exams = check_exam_eligibility(dob, std_class)

    if eligible_exams:
        st.success("✅ The student is eligible for the following exams:")
        for exam, details in eligible_exams.items():
            with st.expander(f"📌 {exam}"):
                for detail in details:
                    st.write(detail)
    else:
        st.warning("⚠️ No major competitive exams found for this age and class.")

st.sidebar.header("About the Exams")
st.sidebar.info(
    "This tool helps students find out their eligibility for competitive school exams in India, including Sainik School, RMS, JNV, and others."
)
