import json

DATA_FILE = "progress.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(topics):
    with open(DATA_FILE, "w") as file:
        json.dump(topics, file, indent=2)

def show_menu():
    print("\n📘 AI Learning Tracker")
    print("1. Add new topic")
    print("2. Mark topic as complete")
    print("3. View topics")
    print("4. Exit")

def main():
    topics = load_data()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            topic = input("Enter topic name: ")
            topics.append({"topic": topic, "done": False})
            save_data(topics)
        elif choice == "2":
            for i, t in enumerate(topics):
                print(f"{i+1}. {'✅' if t['done'] else '❌'} {t['topic']}")
            index = int(input("Enter number to mark as complete: ")) - 1
            topics[index]["done"] = True
            save_data(topics)
        elif choice == "3":
            print("\nYour Topics:")
            for t in topics:
                status = "✅" if t["done"] else "❌"
                print(f"{status} {t['topic']}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
