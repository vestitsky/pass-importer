import csv
import subprocess

def read_csv(file_path):
    """Reads a CSV file and returns a list of password data."""
    pass_data = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print('HEAD:', header)
        for row in reader:
            # If value is "0" or empty, use the header name
            title = row[0] if row[0] != "0" and row[0] != "" else header[0]
            login = row[1] if row[1] != "0" and row[1] != "" else header[1]
            password = row[2] if row[2] != "0" and row[2] != "" else header[2]
            # Combine all columns after the third as notes
            notes = ' '.join(row[3:]) if len(row) > 3 else ''
            print(f"Title: {title}, Login: {login}, Password: {password}, Notes: {notes}")
            pass_data.append((title, login, password, notes))

    return pass_data

def pass_exists(path):
    """Checks if a pass entry exists at the given path."""
    result = subprocess.run(["pass", "show", path], capture_output=True, text=True)
    return result.returncode == 0

def insert_pass(title, login, password, notes):
    """Inserts a password into the pass store with the given data."""
    cmd = ["pass", "insert", f"{title}/{login}"]

    if pass_exists(f"{title}/{login}"):
        print(f"Entry {title}/{login} already exists, renaming.")
        title += "(duble)"

    subprocess.run(cmd, input=f"{password}\n{password}\n", text=True)
    insert_notes(title, login, notes)

def insert_notes(title, login, notes):
    """Inserts notes into the pass store for the given title and login."""
    note_path = f"{title}/{login}/note"

    if len(notes) <= 1:
        print(f"No notes for {note_path}, skipping.")
        return

    if pass_exists(f"{title}/{login}"):
        print(f"Note {note_path} already exists, renaming.")
        title += "(duble)"
        return

    cmd = ["pass", "insert", "-m", note_path]
    subprocess.run(cmd, input=f"{notes}\n", text=True)

def main():
    pass_data = read_csv('PASS.csv')
    print(pass_data)

    for title, login, password, notes in pass_data:
        print(f'Inserting password for {title}/{login}: {password}, Notes: {notes}')
        insert_pass(title, login, password, notes)

if __name__ == "__main__":
    main()