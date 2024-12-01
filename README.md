# Youtube_links_scraper

# Web Scraper for YouTube Video Links and Titles

This project is a Python-based web scraper that uses Selenium WebDriver to extract video links and titles from a YouTube channel's video page.

## Features
- Scrapes YouTube video titles and links.
- Saves the collected data to a text file (`video_links_and_titles.txt`).
- Optionally works in headless mode (without opening the browser UI).

## Installation

### Prerequisites

- Python 3.x
- ChromeDriver (compatible with your version of Chrome browser)
- Selenium package

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/Bek-dev-135/portfolioBek.git
   ```

2. Install required Python packages:
   ```bash
   pip install selenium
   ```

3. Download and install ChromeDriver if not already installed:
   - Visit: [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - Make sure the version matches your installed Chrome version.

4. Ensure `chromedriver` is available in your system's PATH or provide the path to the `chromedriver` in the script.

## Usage

1. Open `Link_Scraper.py` in your text editor.
2. Replace the `driver.get('https://www.youtube.com/c/YOUR_CHANNEL_NAME/videos')` line with the YouTube channel URL you want to scrape.
3. Run the script:
   ```bash
   python Link_Scraper.py
   ```
4. The script will scrape the video links and titles and save them to a file named `video_links_and_titles.txt`.

## Notes
- If you're running in headless mode, no browser window will appear during execution.
- The scraper waits for the page to load and scrolls to the bottom to capture all the video links.

## Troubleshooting

- **Error: No video elements found**: Make sure the YouTube channel URL is correct, and check if the page fully loaded before the scraper attempts to fetch video elements.
- **Timeout Errors**: Increase the timeout duration or ensure that the page is loading fast enough to allow the scraper to access the video links.

## License

This project is licensed under the MIT License 
https://opensource.org/license/mit

---

Feel free to contribute by forking the repository and submitting a pull request.

```

