# todo.py

tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Görevleri Listele")
    print("2. Görev Ekle")
    print("3. Görev Sil")
    print("4. Çıkış")

while True:
    show_menu()
    choice = input("Seçiminizi yapın (1-4): ")

    if choice == "1":
        if not tasks:
            print("Henüz görev yok.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Yeni görev: ")
        tasks.append(task)
        print(f"'{task}' eklendi.")

    elif choice == "3":
        num = int(input("Silmek istediğiniz görev numarası: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"'{removed}' silindi.")
        else:
            print("Geçersiz numara.")

    elif choice == "4":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")

