from data_handler import load_data, save_data
from commands_handler import listen_commands
from users import Users
from notes import Notes


def main():
    book = load_data("users.pkl", Users())
    notes = load_data("notes.pkl", Notes())
    
    def on_exit(book, notes):
        save_data(book, "users.pkl")
        save_data(notes, "notes.pkl")

    listen_commands(book, notes, on_exit)


if __name__ == "__main__":
    main()
