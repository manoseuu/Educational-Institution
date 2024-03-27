# ΕΡΓΑΣΙΑ ΕΞΑΜΗΝΟΥ ΓΛΩΣΣΑ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ ΙΙΙ ΜΑΝΟΣ ΕΥΑΓΓΕΛΟΥΛΗΣ
# Το πρόγραμμα διαχειρίζεται μια λίστα φοιτητών, επιτρέποντας στον χρήστη να προβάλλει, να αναζητά, να προσθέτει, να διαγράφει και να εκτυπώνει σε ένα αρχείο πληροφορίες για τους φοιτητές εμφανίζοντας του ένα μενού πολλαπλών επιλογών.


# Λίστα η οποία αποθηκεύει πληοροφορίες ξεχωριστά για κάθε φοιτητή
students_list = []

# Εμφλανιση μενού στον χρήστη
def show_main_menu():
    print("\nΚύριο Μενού:")
    print("1. Προβολή όλων των φοιτητών")
    print("2. Αναζήτηση φοιτητών")
    print("3. Προσθήκη νέου φοιτητή")
    print("4. Διαγραφή φοιτητή")
    print("5. Εκτύπωση της λίστας των φοιτητών σε ένα αρχείο")
    print("6. Έξοδος")

# Εκτύπωση όλων των φοιτητών που υπάρχουν στο σύστημα
def print_students():
    if not students_list:
        print("Δεν υπάρχουν διαθέσιμοι φοιτητές.")
        return

    print("\nΑ/Α ΕΠΩΝΥΜΟ ΟΝΟΜΑ ΚΙΝΗΤΟ ΑΡΙΘΜΟΣ ΕΓΓΡΑΦΗΣ")
    for index, student in enumerate(students_list, start=1):
        print(f"{index}. {student['last_name']} {student['first_name']} {student['phone']} {student['reg_number']}")

# Αναζήτηση φοιτητή με βάση την επιλογή του χρήστη
def search_students():
    if not students_list:
        print("Δεν υπάρχουν διαθέσιμοι φοιτητές.")
        return

    print("\nΑναζήτηση φοιτητών:")
    print("1. Επώνυμο")
    print("2. Όνομα")
    print("3. Κινητό τηλέφωνο")
    print("4. Αριθμός εγγραφής")
    choice = input("Εισάγετε την επιλογή σας (1-4): ")

    search_term = input("Εισάγετε τον όρο αναζήτησης: ").lower()

    search_results = []

    for student in students_list:
        if search_term in student[choice.lower()]:
            search_results.append(student)

    if not search_results:
        print("Δεν βρέθηκαν αντίστοιχοι φοιτητές.")
    else:
        print_students(search_results)

# Έλεγχος χαρακτήρων ονόματος φοιτητών
def validate_name(name):
    return name.isalpha() and len(name) <= 15

# Έλεγχος αριθμού τηλεφώνου φοιτητών
def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

# Προσθήκη φοιτητή
def add_student():
    print("\nΠροσθήκη νέου φοιτητή:")
    last_name = input("Εισάγετε το επώνυμο: ")
    first_name = input("Εισάγετε το όνομα: ")
    phone = input("Εισάγετε τον αριθμό του κινητού τηλεφώνου: ")
    reg_number = input("Εισάγετε τον αριθμό εγγραφής: ")

    if not (validate_name(last_name) and validate_name(first_name) and validate_phone(phone) and reg_number.isdigit()):
        print("Μη έγκυρη είσοδος. Παρακαλώ ελέγξτε τη μορφή της εισόδου σας.")
        return

    students_list.append({
        'last_name': last_name,
        'first_name': first_name,
        'phone': phone,
        'reg_number': reg_number
    })
    print("Ο φοιτητής προστέθηκε στο σύστημα με επιτυχία!")

# Διαγραφή φοιτητή
def delete_student():
    if not students_list:
        print("Δεν υπάρχουν φοιτητές εγγεγραμένοι στο σύστημα.")
        return

    print_students()
    choice = input("Εισάγετε τον Α/Α του φοιτητή ώστε να γίνει η διαγραφή του: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(students_list):
            deleted_student = students_list.pop(choice - 1)
            print(f"Ο φοιτητής {deleted_student['first_name']} {deleted_student['last_name']} διαγράφηκε με επιτυχία.")
        else:
            print("Μη έγκυρη επιλογή ,εισάγετε έναν έγκυρο αριθμό σειράς.")
    except ValueError:
        print("Μη έγκυρη είσοδος ,εισάγετε έναν έγκυρο αριθμό σειράς.")

# Εκτύπωση των φοιτητών που είναι εγγεγραμμένοι στο σύστημα
def print_to_file():
    if not students_list:
        print("Δεν υπάρχουν φοιτητές εγγεγραμμένοι στο σύστημα.")
        return

    with open('students.txt', 'w') as file:
        file.write("Α/Α ΕΠΩΝΥΜΟ ΟΝΟΜΑ ΚΙΝΗΤΟ ΑΡΙΘΜΟΣ ΕΓΓΡΑΦΗΣ\n")
        for index, student in enumerate(students_list, start=1):
            file.write(f"{index}. {student['last_name']} {student['first_name']} {student['phone']} {student['reg_number']}\n")
        print("Οι φοιτητές όπου βρίσκονται εντός συστήματος έχουν εκτυπωθεί στο αρχείο με επιτυχία.")

# Η επανάληψη του προγράμματος με βάση την επιλογή του χρήστη από το μενού του προγράμματος
while True:
    show_main_menu()
    choice = input("Εισάγετε την επιλογή σας από το 1 εώς το 6: ")

    if choice == '1':
        print_students()
    elif choice == '2':
        search_students()
    elif choice == '3':
        add_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print_to_file()
    elif choice == '6':
        print("Έξοδος από την εφαρμογή.")
        break
    else:
        print("Μη έγκυρη επιλογή, εισάγετε έναν αριθμό από το 1 έως το 6.")
