#!/usr/bin/env python

import csv
from bs4 import BeautifulSoup
from decouple import config
from pathlib import Path

html_file = config('HTML_FILE', default='../raw/tables.html')
csv_file = config('CSV_FILE', default='../csv/ny_cooling_centers_2024.csv')


def clean_whitespace(text):
    # Replace multiple spaces with a single space
    text = ' '.join(text.split())
    # Remove spaces around commas
    text = text.replace(' ,', ',').replace(', ', ', ')
    return text


def parse_html(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    data = []
    headers = ["Facility", "Street Address", "Contact Number", "Days and Hours of Operation"]

    tbody_elements = soup.find_all('tbody', class_='cc-table-body ng-scope')

    for tbody in tbody_elements:
        rows = tbody.find_all('tr', class_='cc-table-tr-m1 ng-scope')
        for row in rows:
            cells = row.find_all('td')
            row_data = [clean_whitespace(cell.get_text(separator=' ', strip=True)) for cell in cells]
            data.append(row_data)

    return headers, data


def save_to_csv(csv_file_path, headers, data):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as fn:
        csv_writer = csv.writer(fn)
        csv_writer.writerow(headers)
        csv_writer.writerows(data)


def main():
    headers, html_data = parse_html(html_file)
    save_to_csv(csv_file, headers, html_data)
    print(f'Tables have been successfully extracted and saved to {csv_file}')


if __name__ == '__main__':
    main()

