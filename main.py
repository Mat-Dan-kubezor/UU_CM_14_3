import csv


def write_holiday_cities(first_letter):
    visited = set()
    to_visit = set()

    with open('travel-notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:  
                continue
            try:
                name, cities_visited, cities_to_visit = row
                if name.startswith(first_letter):
                    visited.update(cities_visited.split(';'))
                    to_visit.update(cities_to_visit.split(';'))
            except ValueError:
                print(f"Некорректный формат строки: {row}")
                continue

    not_visited = to_visit - visited

    visited = sorted(visited)
    to_visit = sorted(to_visit)
    not_visited = sorted(not_visited)

    first_city_to_visit = not_visited[0] if not_visited else 'None'

    with open('holiday.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Посетили'] + visited)
        writer.writerow(['Хотят посетить'] + to_visit)
        writer.writerow(['Никогда не были в'] + not_visited)
        writer.writerow(['Следующим городом будет'] + [first_city_to_visit])


write_holiday_cities('R')
