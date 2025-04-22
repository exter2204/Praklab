temperature = input("Температура выше двадцати градусов? ").strip().lower()
if temperature == "да":
    is_rainy = input("На улице дождь? ").strip().lower()
    if is_rainy == "да":
        print("Футболка, шорты и дождевик")
    else:
        print("Футболка и шорты")
else:
    temperature = input("Температура выше восьми градусов? ").strip().lower()
    if temperature == "да":
        is_rainy = input("Осадки есть? ").strip().lower()
        if is_rainy == "да":
            is_rainy_heavily = input("Льёт как из ведра? ").strip().lower()
            if is_rainy_heavily == "да":
                print("Пальто, сапоги и зонт")
            else:
                print("Пальто, дождевик")
        else:
            print("Пальто")
    else:
        print("Пуховик")
