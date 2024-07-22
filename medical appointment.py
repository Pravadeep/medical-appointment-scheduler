class Appointment:
    def __init__(self, patient_name, date, time):
        self.patient_name = patient_name
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment on {self.date} at {self.time} for {self.patient_name}"


class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def cancel_appointment(self, appointment):
        if appointment in self.appointments:
            self.appointments.remove(appointment)
        else:
            print("Appointment not found.")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            for appointment in self.appointments:
                print(appointment)

    def search_appointment(self, patient_name):
        found = False
        for appointment in self.appointments:
            if appointment.patient_name == patient_name:
                print(appointment)
                found = True
        if not found:
            print("No appointment found for", patient_name)


def main():
    scheduler = AppointmentScheduler()

    while True:
        print("\nMedical Appointment Scheduler")
        print("1. Add Appointment")
        print("2. Cancel Appointment")
        print("3. View Appointments")
        print("4. Search Appointment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_name = input("Enter patient's name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            appointment = Appointment(patient_name, date, time)
            scheduler.add_appointment(appointment)
            print("Appointment added successfully.")

        elif choice == '2':
            if scheduler.appointments:
                print("Select appointment to cancel:")
                for index, appointment in enumerate(scheduler.appointments):
                    print(f"{index + 1}. {appointment}")
                cancel_choice = int(input("Enter appointment number to cancel: "))
                scheduler.cancel_appointment(scheduler.appointments[cancel_choice - 1])
                print("Appointment canceled successfully.")
            else:
                print("No appointments scheduled.")

        elif choice == '3':
            scheduler.view_appointments()

        elif choice == '4':
            patient_name = input("Enter patient's name to search: ")
            scheduler.search_appointment(patient_name)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
Create
a
Medical
Appointment
Scheduler in python


class Appointment:
    def __init__(self, patient_name, date, time):
        self.patient_name = patient_name
        self.date = date
        self.time = time

    def _str_(self):
        return f"Appointment on {self.date} at {self.time} for {self.patient_name}"


class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def cancel_appointment(self, appointment):
        if appointment in self.appointments:
            self.appointments.remove(appointment)
        else:
            print("Appointment not found.")

    def view_appointments(self):
        if not self.Appointments:
            print("No appointments scheduled.")
        else:
            for appointment in self.Appointments:
                print(appointment)

    def search_appointment(self, patient_name):
        found = False
        for appointment in self.appointments:
            if appointment.patient_name == patient_name:
                print(appointment)
                found = True
        if not found:
            print("No appointment found for", patient_name)


def main():
    scheduler = AppointmentScheduler()

    while True:
        print("\nMedical Appointment Scheduler")
        print("1. Add Appointment")
        print("2. Cancel Appointment")
        print("3. View Appointments")
        print("4. Search Appointment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_name = input("Enter patient's name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            appointment = Appointment(patient_name, date, time)
            scheduler.add_appointment(appointment)
            print("Appointment added successfully.")

        elif choice == '2':
            if scheduler.appointments:
                print("Select appointment to cancel:")
                for index, appointment in enumerate(scheduler.appointments):
                    print(f"{index + 1}. {appointment}")
                cancel_choice = int(input("Enter appointment number to cancel: "))
                scheduler.cancel_appointment(scheduler.appointments[cancel_choice - 1])
                print("Appointment canceled successfully.")
            else:
                print("No appointments scheduled.")

        elif choice == '3':
            scheduler.view_appointments()

        elif choice == '4':
            patient_name = input("Enter patient's name to search: ")
            scheduler.search_appointment(patient_name)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()