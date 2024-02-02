def age_replace(age):
    if age > 0 and age <= 6:
        return "少年"

    elif age > 7 and age <= 18:
        return  "青年"

    elif age > 19 and age <= 65:
        return "中年"

    else:
        return "老年"

print(age_replace(80))
