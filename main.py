from seeds import (
    create_cat,
    read_all_cats,
    find_cat_by_name,
    update_cat_age,
    add_feature_to_cat,
    delete_cat_by_name,
    delete_all_cats
)

def menu():
    while True:
        print("\n📋 Меню дій:")
        print("1. Додати кота")
        print("2. Показати всіх котів")
        print("3. Знайти кота за ім’ям")
        print("4. Оновити вік кота")
        print("5. Додати характеристику коту")
        print("6. Видалити кота")
        print("7. Видалити всіх котів")
        print("0. Вийти")
        choice = input("👉 Виберіть дію: ")

        if choice == "1":
            name = input("Ім'я кота: ")
            age = int(input("Вік кота: "))
            features = input("Введіть характеристики через кому: ").split(",")
            create_cat(name, age, [f.strip() for f in features])
        elif choice == "2":
            read_all_cats()
        elif choice == "3":
            name = input("Ім'я кота для пошуку: ")
            find_cat_by_name(name)
        elif choice == "4":
            name = input("Ім'я кота: ")
            new_age = int(input("Новий вік: "))
            update_cat_age(name, new_age)
        elif choice == "5":
            name = input("Ім'я кота: ")
            feature = input("Нова характеристика: ")
            add_feature_to_cat(name, feature)
        elif choice == "6":
            name = input("Ім'я кота: ")
            delete_cat_by_name(name)
        elif choice == "7":
            delete_all_cats()
        elif choice == "0":
            print("👋 До зустрічі!")
            break
        else:
            print("❗ Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        print(f"❌ Сталася помилка: {e}")
