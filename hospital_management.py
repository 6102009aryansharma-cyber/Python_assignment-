
from pathlib import Path
import json

# -------------------------
# Patient & Doctor Classes
# -------------------------
class Person:
    """Base class for Patient and Doctor"""
    def __init__(self, name, unique_id):
        self.name = name
        self.unique_id = unique_id

    def __str__(self):
        return f"{self.unique_id} - {self.name}"

    def __repr__(self):
        return self.__str__()


class Patient(Person):
    def __init__(self, name, patient_id, age, disease, status="Admitted"):
        super().__init__(name, patient_id)
        self.age = age
        self.disease = disease
        self.status = status
        self.doctor_id = None

    def admit(self):
        self.status = "Admitted"

    def discharge(self):
        self.status = "Discharged"

    def assign_doctor(self, doctor_id):
        self.doctor_id = doctor_id

    def to_dict(self):
        return {
            "name": self.name,
            "patient_id": self.unique_id,
            "age": self.age,
            "disease": self.disease,
            "status": self.status,
            "doctor_id": self.doctor_id,
        }


class Doctor(Person):
    def __init__(self, name, doctor_id, specialization):
        super().__init__(name, doctor_id)
        self.specialization = specialization

    def to_dict(self):
        return {
            "name": self.name,
            "doctor_id": self.unique_id,
            "specialization": self.specialization,
        }


# -------------------------
# Hospital Management
# -------------------------
class HospitalManagement:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.data_file = Path("hospital_records.json")

    # -------- Patient Operations ----------
    def add_patient(self):
        print("\n--- Add Patient ---")
        pid = input("Enter Patient ID: ").strip()
        name = input("Enter name: ").strip()
        age = input("Enter age: ").strip()
        disease = input("Enter disease: ").strip()
        self.patients[pid] = Patient(name, pid, age, disease)
        print("✅ Patient added successfully.")

    def view_patients(self):
        print("\n--- Patient List ---")
        if not self.patients:
            print("No patient data available.")
            return
        print(f"{'ID':<8} {'Name':<20} {'Age':<5} {'Disease':<15} {'Status':<12} {'Doctor':<10}")
        print("-" * 70)
        for p in self.patients.values():
            print(f"{p.unique_id:<8} {p.name:<20} {p.age:<5} {p.disease:<15} {p.status:<12} {p.doctor_id}")
        print("-" * 70)

    def search_patient(self):
        keyword = input("Enter Patient ID or Name keyword: ").lower().strip()
        results = [p for p in self.patients.values() if keyword in p.unique_id.lower() or keyword in p.name.lower()]
        if results:
            for p in results:
                print(p)
        else:
            print("✅ Patient not found.")

    def discharge_patient(self):
        pid = input("Enter Patient ID to discharge: ").strip()
        if pid in self.patients:
            self.patients[pid].discharge()
            print("✅ Patient discharged successfully.")
        else:
            print("✅ Patient ID not found.")

    # -------- Doctor Operations ----------
    def add_doctor(self):
        print("\n--- Add Doctor ---")
        did = input("Enter Doctor ID: ").strip()
        name = input("Enter Doctor Name: ").strip()
        spec = input("Enter Specialization: ").strip()
        self.doctors[did] = Doctor(name, did, spec)
        print("✅ Doctor added successfully.")

    def view_doctors(self):
        print("\n--- Doctor List ---")
        if not self.doctors:
            print("No doctor data available.")
            return
        print(f"{'ID':<8} {'Name':<20} {'Specialization':<15}")
        print("-" * 50)
        for d in self.doctors.values():
            print(f"{d.unique_id:<8} {d.name:<20} {d.specialization:<15}")
        print("-" * 50)

    def assign_doctor(self):
        pid = input("Enter Patient ID: ").strip()
        did = input("Enter Doctor ID: ").strip()

        if pid not in self.patients:
            print("Patient not found.")
            return
        if did not in self.doctors:
            print("Doctor not found.")
            return

        self.patients[pid].assign_doctor(did)
        print("Doctor assigned successfully.")

    # -------- File Handling ----------
    def save_data(self):
        """Save patients and doctors to JSON file."""
        data = {
            "patients": {pid: p.to_dict() for pid, p in self.patients.items()},
            "doctors": {did: d.to_dict() for did, d in self.doctors.items()},
        }
        try:
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            print("💾 Data saved successfully.")
        except Exception as e:
            print("❌ Error saving file:", e)

    def load_data(self):
        """Load patients and doctors from JSON file."""
        if not self.data_file.exists():
            print("✅ No saved data found.")
            return
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Reconstruct objects (guard if file format is older/missing fields)
            self.patients = {pid: Patient(**info) for pid, info in data.get("patients", {}).items()}
            self.doctors = {did: Doctor(**info) for did, info in data.get("doctors", {}).items()}
            print("📂 Data loaded successfully.")
        except Exception as e:
            print("❌ Error loading file:", e)


# -------------------------
# CLI Menu
# -------------------------
def menu():
    while True:
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Discharge Patient")
        print("5. Add Doctor")
        print("6. View Doctors")
        print("7. Assign Doctor to Patient")
        print("8. Save Records")
        print("9. Load Records")
        print("0. Exit")
        ch = input("Enter choice: ").strip()
        if ch == "1":
            HMS.add_patient()
        elif ch == "2":
            HMS.view_patients()
        elif ch == "3":
            HMS.search_patient()
        elif ch == "4":
            HMS.discharge_patient()
        elif ch == "5":
            HMS.add_doctor()
        elif ch == "6":
            HMS.view_doctors()
        elif ch == "7":
            HMS.assign_doctor()
        elif ch == "8":
            HMS.save_data()
        elif ch == "9":
            HMS.load_data()
        elif ch == "0":
            print("Goodbye ✅")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    HMS = HospitalManagement()  # create the instance so HMS is defined
    menu()