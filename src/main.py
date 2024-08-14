def get_date(date_str: str) -> str:
    """
    Извлекает дату из строки и возвращает ее ".
    """
    year = date_str[0:4]
    month = date_str[5:7]
    day = date_str[8:10]
    return f"{day}.{month}.{year}"
print(get_date(str(2024003111)))
