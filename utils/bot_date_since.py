from datetime import datetime
import pytz


async def days_since():
    # Kiritilgan sana malumotini datetime objektiga o'tkazamiz
    input_date_str = "23.11.2023"
    input_date = datetime.strptime(input_date_str, "%d.%m.%Y")

    # Ayni damdagi sana (bu joyda Asia/Tashkent vaqt zonasi)
    tz = pytz.timezone('Asia/Tashkent')

    # Joriy sana (bu ham Asia/Tashkent vaqt zonasi)
    current_date = datetime.now(tz)

    # Kiritilgan va joriy sanalar orasidagi farqni olish
    input_date = tz.localize(input_date)  # Kiritilgan sana vaqt zonasini qo'shish
    delta = current_date - input_date

    # Natijani kunlar ko'rinishida qaytarish
    return delta.days



