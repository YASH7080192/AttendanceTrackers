# =====================================================================
#  PYTHON ASSIGNMENT 01
#  Project: Command-Line Attendance Tracker
#   Submitted by: Yashvant Giri
#   Date: 12-Nov-2025
# =====================================================================

# 🔹 Import required module
import datetime

# ---------------------------------------------------------------------
#  TASK 1: INTRODUCTION & PROJECT SETUP
# ---------------------------------------------------------------------
'''
In this project, we are building a Python-based Command-Line tool that:
→ Records student names and their check-in times.
→ Validates data (no empty or duplicate names).
→ Displays a formatted attendance summary.
→ Optionally calculates absentees and saves the report to a text file.
'''

print("\n================= WELCOME TO ATTENDANCE TRACKER =================")
print("This Python program records student attendance with timestamps.")
print("=================================================================\n")

# ---------------------------------------------------------------------
#  TASK 2 & 3: INPUT, DATA COLLECTION, AND VALIDATION
# ---------------------------------------------------------------------

attendance_data = {}  # Dictionary to store attendance as {name: time}

# Ask total number of entries
while True:
    try:
        total_entries = int(input("👉 Enter the number of attendance entries to record: "))
        if total_entries <= 0:
            print("⚠️ Please enter a positive number greater than zero.")
            continue
        break
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.\n")

# Loop for each student entry
for i in range(total_entries):
    print(f"\n--- ENTRY {i+1} ---")

    # Step 1: Take student name with validation
    while True:
        student_name = input("Enter Student Name: ").strip().title()
        if student_name == "":
            print("❌ Error: Name cannot be empty.")
            continue
        if student_name in attendance_data:
            print(f"⚠️ Warning: {student_name} is already marked present at {attendance_data[student_name]}")
            continue
        break

    # Step 2: Take check-in time with validation
    while True:
        check_in = input("Enter Check-in Time (e.g., 09:15 AM): ").strip()
        if check_in == "":
            print("❌ Error: Check-in time cannot be blank.")
            continue
        break

    # Store the entry in dictionary
    attendance_data[student_name] = check_in
    print(f"✅ {student_name} marked present at {check_in}")

print("\n✅ All entries recorded successfully!")

# ---------------------------------------------------------------------
#  TASK 5: ABSENTEE VALIDATION
# ---------------------------------------------------------------------
print("\n----------------- ABSENTEE CALCULATION -----------------")

while True:
    try:
        total_students = int(input("Enter total number of students in class: "))
        if total_students < len(attendance_data):
            print("⚠️ Total strength cannot be smaller than total present count. Try again.")
            continue
        break
    except ValueError:
        print("❌ Please enter a valid number.")

total_present = len(attendance_data)
total_absent = total_students - total_present

# ---------------------------------------------------------------------
# TASK 4: DISPLAY FORMATTED ATTENDANCE SUMMARY
# ---------------------------------------------------------------------
print("\n==================== ATTENDANCE SUMMARY ====================")
print(f"{'Student Name':<25}Check-in Time")
print("-------------------------------------------------------------")

# Display all attendance data (sorted by name for clarity)
for name, time in sorted(attendance_data.items()):
    print(f"{name:<25}{time}")

print("-------------------------------------------------------------")
print(f"Total Students Present : {total_present}")
print(f"Total Students Absent  : {total_absent}")
print(f"Total Class Strength   : {total_students}")
print("=============================================================\n")

# ---------------------------------------------------------------------
#  TASK 6 (BONUS): SAVE REPORT TO FILE
# ---------------------------------------------------------------------
save_choice = input("💾 Do you want to save this attendance report to a file? (yes/no): ").lower()

if save_choice == "yes":
    now = datetime.datetime.now()
    timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
    file_name = f"attendance_report_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    # Prepare formatted report
    report = []
    report.append("K.R. MANGALAM UNIVERSITY - ATTENDANCE REPORT")
    report.append(f"Generated On: {timestamp}")
    report.append("-------------------------------------------------------------")
    report.append(f"{'Student Name':<25}Check-in Time")
    report.append("-------------------------------------------------------------")
    for name, time in sorted(attendance_data.items()):
        report.append(f"{name:<25}{time}")
    report.append("-------------------------------------------------------------")
    report.append(f"Total Present : {total_present}")
    report.append(f"Total Absent  : {total_absent}")
    report.append(f"Class Strength: {total_students}")
    report.append("-------------------------------------------------------------")
    report.append("Report Generated by: Yashvant Giri (MCA AI & ML)")
    report.append("=============================================================")

    try:
        with open(file_name, "w") as file:
            file.write("\n".join(report))
        print(f"\n✅ Attendance report successfully saved as '{file_name}'")
    except IOError:
        print("❌ Error: Unable to write the file.")
else:
    print("\n📂 Report not saved. Exiting without file creation.")

# ---------------------------------------------------------------------
#  PROGRAM END
# ---------------------------------------------------------------------
print("\n-------------------------------------------------------------")
print("Program completed successfully. Have a great day!")
print("-------------------------------------------------------------\n")
