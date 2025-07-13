from models import Cat
from validator import validate_input


@validate_input
def create_cat(name, age, features):
    cat = Cat(name=name, age=age, features=features)
    cat.save()
    print(f"✅ Додано кота '{name}' з ID {cat.id}")

@validate_input
def read_all_cats():
    print("\n🐾 Усі котики в базі:")
    for cat in Cat.objects:
        print(cat)

@validate_input
def find_cat_by_name(name):
    cat = Cat.objects(name=name).first()
    if cat:
        print(f"\n🔎 Знайдено кота '{name}':")
        print(cat)
    else:
        print(f"❌ Кота '{name}' не знайдено.")

@validate_input
def update_cat_age(name, new_age):
    cat = Cat.objects(name=name).first()
    if cat:
        cat.age = new_age
        cat.save()
        print(f"✅ Вік кота '{name}' оновлено до {new_age}.")
    else:
        print(f"⚠️ Кота '{name}' не знайдено.")

@validate_input
def add_feature_to_cat(name, new_feature):
    cat = Cat.objects(name=name).first()
    if cat:
        if new_feature not in cat.features:
            cat.features.append(new_feature)
            cat.save()
            print(f"✅ Додано нову характеристику '{new_feature}' для '{name}'.")
        else:
            print(f"⚠️ Характеристика вже є у '{name}'.")
    else:
        print(f"❌ Кота '{name}' не знайдено.")

@validate_input
def delete_cat_by_name(name):
    result = Cat.objects(name=name).delete()
    if result:
        print(f"🗑️ Кота '{name}' видалено.")
    else:
        print(f"❌ Кота '{name}' не знайдено.")

@validate_input
def delete_all_cats():
    confirmation = input("⚠️ Ви точно хочете видалити ВСІХ котів? (так/ні): ")
    if confirmation.lower() == "так":
        count = Cat.objects.delete()
        print(f"🔥 Видалено {count} записів.")
    else:
        print("❎ Видалення скасовано.")
