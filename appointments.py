import streamlit as st
import datetime

st.set_page_config(layout="wide")

# Data for doctors
doctors_data = {
    "Dr. Thomas Edison": {"Specialty": "Cardiology", "Availability": "Monday, Wednesday, Friday", "Time Slots": ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM"]},
    "Dr. Samuel Morse": {"Specialty": "Dermatology", "Availability": "Tuesday, Thursday", "Time Slots": ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM"]},
    "Dr. Grace Hopper": {"Specialty": "Pediatrics", "Availability": "Monday to Friday", "Time Slots": ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM"]},
    "Dr. Marie Curie": {
        "Specialty": "Cardiology",
        "Availability": "Tuesday, Thursday",
        "Time Slots": ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM"],
        "Unavailable Slots": ["11:00 AM"]
    }
}

specialties = sorted(set(doctor["Specialty"] for doctor in doctors_data.values()))

# Initialize session state for tracking selection
if "selected_specialty" not in st.session_state:
    st.session_state["selected_specialty"] = None

if "selected_doctor" not in st.session_state:
    st.session_state["selected_doctor"] = None

if "selected_time" not in st.session_state:
    st.session_state["selected_time"] = None

# Function to select the doctor's time slot
def select_time(slot):
    st.session_state["selected_time"] = slot

# Function to filter doctors by specialty
def filter_doctors(specialty):
    return {name: info for name, info in doctors_data.items() if info["Specialty"] == specialty}

st.title('Doctor Appointment Scheduling')
selected_specialty = st.selectbox("Select Medical Specialty", specialties)
matching_doctors = filter_doctors(selected_specialty)
st.session_state["selected_specialty"] = selected_specialty
left_column, doctor_columns = st.columns([2, 3])

with left_column:
    st.header("Book Your Appointment")
    name = st.text_input("Enter your name")
    doctor = st.selectbox("Select Doctor", list(matching_doctors.keys()) if matching_doctors else [])
    date = st.date_input("Select Date", min_value=datetime.date.today())
    # Determine available slots by excluding unavailable ones
    unavailable_slots = doctors_data[doctor].get("Unavailable Slots", [])
    all_slots = doctors_data[doctor]["Time Slots"] if doctor in matching_doctors else []
    available_slots = [slot for slot in all_slots if slot not in unavailable_slots]

    # Maintain consistency with unavailable slots and session state
    selected_time = st.selectbox("Select Time", available_slots, index=available_slots.index(st.session_state["selected_time"]) if st.session_state["selected_time"] in available_slots else 0)
    symptoms = st.text_area("Symptoms")
    notes = st.text_area("Additional Notes")

    # Button to book appointment
    if st.button('Book Appointment'):
        st.success(f"Appointment booked successfully for {name} with {doctor} on {date.strftime('%A, %B %d, %Y')} at {selected_time}")

# Doctors' individual information
with doctor_columns:
    st.header("Doctor Information")
    doctor_cols = st.columns(len(matching_doctors))
    for col, (doc, details) in zip(doctor_cols, matching_doctors.items()):
        with col:
            st.subheader(doc)
            st.write(f"**Specialty:** {details['Specialty']}")
            st.write(f"**Availability:** {details['Availability']}")
            st.write("**Time Slots:**")
            unavailable_slots = details.get("Unavailable Slots", [])
            for slot in details["Time Slots"]:
                if slot in unavailable_slots:
                    col.button(slot, key=f"{doc}_{slot}", disabled=True)
                else:
                    if col.button(slot, key=f"{doc}_{slot}"):
                        select_time(slot)
