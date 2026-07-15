def _generate_date_formats(month: int,
                           day: int,
                           year: int):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    short_months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    months_ru = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ]
    short_months_ru = [
        "янв", "фев", "мар", "апр", "май", "июн",
        "июл", "авг", "сен", "окт", "ноя", "дек"
    ]
    month_name = months[month - 1]
    short_month_name = short_months[month - 1]
    month_name_ru = months_ru[month - 1]
    short_month_name_ru = short_months_ru[month - 1]
    day_with_suffix = f"{day}{_get_day_suffix(day)}"
    formats = [
        f"{month_name} {day_with_suffix}, {year}\t{day} {month_name_ru}, {year}",
        f"{day_with_suffix} {month_name}, {year}\t{day} {month_name_ru}, {year}",
        f"{month_name} {day}, {year}\t{day} {month_name_ru}, {year}",
        f"{day} {month_name} {year}\t{day} {month_name_ru} {year}",
        f"{month_name} {day_with_suffix}\t{day} {month_name_ru}",
        f"{day_with_suffix} {month_name}\t{day} {month_name_ru}",
        f"{month_name} {day}\t{day} {month_name_ru}",
        f"{day} {month_name}\t{day} {month_name_ru}",
        f"{short_month_name} {day_with_suffix}\t{day} {short_month_name_ru}",
        f"{day_with_suffix} {short_month_name}\t{day} {short_month_name_ru}",
        f"{short_month_name} {day}\t{day} {short_month_name_ru}",
        f"{day} {short_month_name}\t{day} {short_month_name_ru}",
    ]
    return formats


def _get_day_suffix(day: int) -> str:
    if 11 <= day <= 13:
        return "th"
    last_digit = day % 10
    if last_digit == 1:
        return "st"
    elif last_digit == 2:
        return "nd"
    elif last_digit == 3:
        return "rd"
    else:
        return "th"


def generate_months_corpus(output_path: str):
    print("Generating date pairs...")
    pairs = set()
    for day in range(1, 31):
        for month in range(1, 13):
            for year in range(988, 2029):
                for date_format in _generate_date_formats(month, day, year):
                    pairs.add(date_format)
    print(f"Generated {len(pairs):,} unique date pairs.")
    print(f"Saving to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        for sent in sorted(pairs):
            f.write(sent + '\n')

