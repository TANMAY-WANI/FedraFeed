import csv
from scraper import scrape_url

def scrape_and_save_headlines_to_csv(csv_filename):
    try:
        # List of URLs to scrape
        urls = [
            "https://m.inshorts.com/en/read/national",
            "https://m.inshorts.com/en/read/sports",
            "https://m.inshorts.com/en/read/politics",
            "https://m.inshorts.com/en/read/technology",
            "https://m.inshorts.com/en/read/entertainment"
            # Add more URLs here
        ]

        headlines = []
        for url in urls:
            scraped_data = scrape_url(url)
            if scraped_data:
                headlines.extend(scraped_data)

        if headlines:
            with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ["Category", "Headline", "Author", "Date", "Description", "Image URL", "Article Body"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                if csvfile.tell() == 0:
                    writer.writeheader()

                for headline in headlines:
                    writer.writerow({
                        "Category": headline['Category'],
                        "Headline": headline['Headline'],
                        "Author": headline['Author'],
                        "Date": headline['Date'],
                        "Description": headline['Description'],
                        "Image URL": headline['Image URL'],
                        "Article Body": headline['Article Body']
                    })

            print(f'New headlines appended to {csv_filename}')
        else:
            print('Failed to retrieve headlines from the web page.')

    except Exception as e:
        print('Error:', str(e))

if __name__ == '__main__':
    csv_filename = './data_scraper.csv'
    scrape_and_save_headlines_to_csv(csv_filename)
