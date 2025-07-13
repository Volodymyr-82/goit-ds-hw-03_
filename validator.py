import inspect
from functools import wraps
import re

def validate_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            for name, value in bound.arguments.items():
                if name == "name":
                    if not isinstance(value, str):
                        raise ValueError("Ім'я кота може тільки бути рядком.")
                    if not value.strip():
                        raise ValueError("Ім'я кота не може бути порожнім.")
                    if value.strip().isdigit():
                        raise ValueError("Ім'я кота не може складатися лише з цифр.")


                elif name in ("age", "new_age"):
                    if not isinstance(value, int):
                        raise ValueError(f"вік кота повинно бути цілим числом.")
                    if value < 0:
                        raise ValueError(f"Значення віку кота не може бути меншим за нуль.")

                elif name == "features":
                    if not isinstance(value, (list, tuple)):
                        raise ValueError("Перелік особливостей кота повинно бути списком або кортежем.")
                    for f in value:
                        if not isinstance(f, str):
                            raise ValueError("Кожна характеристика кота повинна бути рядком.")
                        if not f.strip() or re.fullmatch(r"\d+", f.strip()):
                            raise ValueError(f"Характеристика кота не може бути числом або порожньою.")

                elif name == "new_feature":
                    if not isinstance(value, str):
                        raise ValueError("Кожна характеристика кота повинна бути рядком.")
                    if not value.strip() or value.strip().isdigit():
                        raise ValueError("Нова характеристика повинна бути змістовною.")

            return func(*args, **kwargs)

        except ValueError as e:
            print(f"❌ Невірний ввід даних: {e}")
        except TypeError as e:
            print(f"❌ Помилка виклику функції: {e}")

    return wrapper
