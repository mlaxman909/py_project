import json
import streamlit as st
from abc import ABC, abstractmethod
from pathlib import Path
# ─── PAGE CONFIG ──────────────────────────────────────────────
st.set_page_config(
    page_title="School Management System",
    page_icon="",
    layout="wide"
)
# ─── CUSTOM CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #1e2130;
        border-radius: 8px;
        padding: 8px 20px;
        color: white;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4f8ef7 !important;
    }
    .card {
        background-color: #1e2130;
        padding: 20px;
        border-radius: 12px;
        margin: 10px 0;
        border-left: 4px solid #4f8ef7;
    }
    .success-card {
        background-color: #1a3a2a;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #2ecc71;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)
# ─── DATABASE ─────────────────────────────────────────────────
database = "School_management_system.json"
data = {"Students": [], "Teachers": []}
if Path(database).exists():
    with open(database, 'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)
def save():
    with open(database, "w") as f:
        json.dump(data, f, indent=4)
# ─── OOP CLASSES ──────────────────────────────────────────────
class Person(ABC):
    @abstractmethod
    def roles(self): pass
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email
class Student(Person):
    def roles(self): return "Student"
    def register(self, name, age, gender, email, roll_no):
        for i in data['Students']:
            if i['roll_no'] == roll_no:
                return False, "Student with this Roll No already exists!"
        data['Students'].append({
            'name': name, 'age': age, 'email': email,
            'gender': gender, 'roll_no': roll_no, 'grade': {}
        })
        save()
        return True, f"✅ {name} registered successfully!"
    def add_grade(self, roll_no, subject, marks):
        for i in data['Students']:
            if i['roll_no'] == roll_no:
                i['grade'][subject] = marks
                save()
                return True, "✅ Marks added successfully!"
        return False, "❌ Student not found!"
    def get_details(self, roll_no):
        for s in data['Students']:
            if s['roll_no'] == roll_no:
                return s
        return None
class Teacher(Person):
    def roles(self): return "Teacher"
    def register(self, name, age, gender, email, emp_no, subject):
        for i in data['Teachers']:
            if i['Emp_no'] == emp_no:
                return False, "Teacher with this Employee No already exists!"
        data['Teachers'].append({
            'name': name, 'age': age, 'gender': gender,
            'Emp_no': emp_no, 'email': email, 'subject': subject
        })
        save()
        return True, f"✅ {name} registered successfully!"
    def get_details(self, emp_no):
        for t in data['Teachers']:
            if t['Emp_no'] == emp_no:
                return t
        return None
stud  = Student()
teach = Teacher()
# ─── HEADER ───────────────────────────────────────────────────
st.markdown("# 🏫 School Management System")
st.markdown("Built with **Python OOP + Streamlit** | by M Laxman")
st.divider()
# ─── SIDEBAR STATS ────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📊 Database Stats")
    st.metric("👨‍🎓 Total Students", len(data['Students']))
    st.metric("👨‍🏫 Total Teachers", len(data['Teachers']))
    st.divider()
    st.markdown("### 🛠️ Tech Stack")
    st.markdown("- Python 3\n- Streamlit\n- JSON\n- OOP (ABC)")
# ─── TABS ─────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👨‍🎓 Register Student",
    "👨‍🏫 Register Teacher",
    "📝 Add Marks",
    "🔍 Student Details",
    "🔍 Teacher Details"
])
# ── TAB 1: Register Student ────────────────────────────────────
with tab1:
    st.subheader("👨‍🎓 Register New Student")
    col1, col2 = st.columns(2)
    with col1:
        s_name   = st.text_input("Full Name", placeholder="e.g. Laxman", key="s_name")
        s_age    = st.number_input("Age", min_value=5, max_value=30, value=18, key="s_age")
        s_gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="s_gender")
    with col2:
        s_email  = st.text_input("Email", placeholder="e.g. student@gmail.com", key="s_email")
        s_roll   = st.number_input("Roll Number", min_value=1, value=1, key="s_roll")
    if st.button("✅ Register Student", use_container_width=True):
        if not s_name:
            st.error("Name cannot be empty!")
        elif not Person.validate_email(s_email):
            st.error("Please enter a valid email address!")
        else:
            success, msg = stud.register(s_name, int(s_age), s_gender, s_email, int(s_roll))
            if success: st.success(msg)
            else:       st.error(msg)
# ── TAB 2: Register Teacher ────────────────────────────────────
with tab2:
    st.subheader("👨‍🏫 Register New Teacher")
    col1, col2 = st.columns(2)
    with col1:
        t_name    = st.text_input("Full Name", placeholder="e.g. Mr. Sharma", key="t_name")
        t_age     = st.number_input("Age", min_value=21, max_value=65, value=30, key="t_age")
        t_gender  = st.selectbox("Gender", ["Male", "Female", "Other"], key="t_gender")
    with col2:
        t_email   = st.text_input("Email", placeholder="e.g. teacher@school.com", key="t_email")
        t_emp_no  = st.number_input("Employee Number", min_value=1, value=101, key="t_emp")
        t_subject = st.text_input("Subject", placeholder="e.g. Mathematics", key="t_subject")
    if st.button("✅ Register Teacher", use_container_width=True):
        if not t_name:
            st.error("Name cannot be empty!")
        elif not Person.validate_email(t_email):
            st.error("Please enter a valid email address!")
        elif not t_subject:
            st.error("Subject cannot be empty!")
        else:
            success, msg = teach.register(t_name, int(t_age), t_gender, t_email, int(t_emp_no), t_subject)
            if success: st.success(msg)
            else:       st.error(msg)
# ── TAB 3: Add Marks ──────────────────────────────────────────
with tab3:
    st.subheader("📝 Add Marks for Student")
    col1, col2, col3 = st.columns(3)
    with col1:
        m_roll    = st.number_input("Roll Number", min_value=1, value=1, key="m_roll")
    with col2:
        m_subject = st.text_input("Subject", placeholder="e.g. Python", key="m_subject")
    with col3:
        m_marks   = st.number_input("Marks (out of 100)", min_value=0, max_value=100, value=0, key="m_marks")
    if st.button("➕ Add Marks", use_container_width=True):
        if not m_subject:
            st.error("Subject cannot be empty!")
        else:
            success, msg = stud.add_grade(int(m_roll), m_subject, int(m_marks))
            if success: st.success(msg)
            else:       st.error(msg)
# ── TAB 4: Student Details ─────────────────────────────────────
with tab4:
    st.subheader("🔍 Student Details")
    col1, col2 = st.columns([3, 1])
    with col1:
        d_roll = st.number_input("Enter Roll Number", min_value=1, value=1, key="d_roll")
    with col2:
        st.write(""); st.write("")
        search_stud = st.button("🔍 Search", use_container_width=True,key="btn_search_stud")
    if search_stud:
        student = stud.get_details(int(d_roll))
        if student:
            grade = student['grade']
            avg   = round(sum(grade.values()) / len(grade), 2) if grade else 0
            col1, col2, col3 = st.columns(3)
            col1.metric("👤 Name",     student['name'])
            col2.metric("🎂 Age",      student['age'])
            col3.metric("📊 Average",  f"{avg}%")
            col4, col5 = st.columns(2)
            col4.metric("⚧ Gender",   student['gender'])
            col5.metric("📧 Email",    student['email'])
            if grade:
                st.markdown("### 📚 Subject-wise Marks")
                for subject, marks in grade.items():
                    icon = "🟢" if marks >= 75 else "🟡" if marks >= 50 else "🔴"
                    st.markdown(f"<div class='success-card'>{icon} <b>{subject}</b> — {marks}/100</div>",
                                unsafe_allow_html=True)
            else:
                st.info("No marks added yet.")
        else:
            st.error("❌ Student not found!")
    if data['Students']:
        st.markdown("---")
        st.markdown("### 👥 All Registered Students")
        for s in data['Students']:
            grade = s['grade']
            avg   = round(sum(grade.values()) / len(grade), 2) if grade else 0
            st.markdown(f"<div class='card'><b>#{s['roll_no']} — {s['name']}</b> | {s['gender']} | Avg: {avg}%</div>",
                        unsafe_allow_html=True)
# ── TAB 5: Teacher Details ─────────────────────────────────────
with tab5:
    st.subheader("🔍 Teacher Details")
    col1, col2 = st.columns([3, 1])
    with col1:
        d_emp = st.number_input("Enter Employee Number", min_value=1, value=101, key="d_emp")
    with col2:
        st.write(""); st.write("")
        search_teach = st.button("🔍 Search", use_container_width=True,key="btn_search_teach")
    if search_teach:
        teacher = teach.get_details(int(d_emp))
        if teacher:
            col1, col2, col3 = st.columns(3)
            col1.metric("👤 Name",    teacher['name'])
            col2.metric("📚 Subject", teacher['subject'])
            col3.metric("🎂 Age",     teacher['age'])
            col4, col5 = st.columns(2)
            col4.metric("⚧ Gender",  teacher['gender'])
            col5.metric("📧 Email",  teacher['email'])
        else:
            st.error("❌ Teacher not found!")
    if data['Teachers']:
        st.markdown("---")
        st.markdown("### 👥 All Registered Teachers")
        for t in data['Teachers']:
            st.markdown(f"<div class='card'><b>#{t['Emp_no']} — {t['name']}</b> | {t['subject']} | {t['gender']}</div>",
                        unsafe_allow_html=True)