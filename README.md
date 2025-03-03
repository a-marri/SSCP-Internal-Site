# Google Site Scraper for GitBook

This tool scrapes Google Site pages listed in a SUMMARY.md file and converts them to markdown files organized in a GitBook-compatible directory structure.

## Features

- Parses SUMMARY.md file to extract Google Site links
- Scrapes content from Google Site pages
- Creates appropriate directory structure for GitBook
- Converts HTML content to Markdown
- Generates a new SUMMARY.md file with local links
- Preserves the hierarchy of pages
- **Handles embedded content:**
  - YouTube videos (with proper embedding)
  - Google Docs, Sheets, Slides, Forms, Calendar, and Drive files
  - PDF documents and other embedded objects
  - Custom Google Sites embeds
- **Downloads and manages images:**
  - Downloads images from remote URLs
  - Stores images in a local assets folder
  - Updates markdown links to reference local images
- **Network Resilience**: Robust retry and error handling for reliable scraping of large sites

## Requirements

- Python 3.6+
- Required packages: requests, beautifulsoup4, markdown, tqdm

## Installation

1. Clone this repository or download the files
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scraper.py --summary /path/to/SUMMARY.md --output /path/to/output/directory
```

### Arguments

- `--summary`: Path to the SUMMARY.md file (default: SUMMARY.md in the current directory)
- `--output`: Output directory for the GitBook files (default: gitbook in the current directory)

### Running with the Shell Script

For convenience, you can use the provided shell script:

```bash
./run_scraper.sh --summary /path/to/SUMMARY.md --output /path/to/output/directory [options]
```

#### Additional Shell Script Options

- `--title`: Title for the GitBook (default: "GitBook Documentation")
- `--author`: Author name (default: "Author")
- `--download-images`: Download images to a local assets folder
- `--max-workers`: Maximum number of concurrent image download workers (default: 10)

## Example

```bash
# Simple usage
python scraper.py --summary ~/Downloads/SUMMARY.md --output ~/my-gitbook

# With all options via shell script
./run_scraper.sh --summary ~/Downloads/SUMMARY.md --output ~/my-gitbook --title "My Documentation" --author "John Doe" --download-images --max-workers 20
```

This will:
1. Parse the SUMMARY.md file at ~/Downloads/SUMMARY.md
2. Scrape all Google Site links found in the file
3. Create a GitBook-compatible directory structure in ~/my-gitbook
4. Save the content as markdown files
5. Generate a new SUMMARY.md file with local links
6. Download all images to a local assets folder (if --download-images is specified)

## Image Handling

The scraper provides two options for handling images:

1. **Remote references (default)**: By default, the scraper will keep the original remote URLs for images.

2. **Local downloads**: When using the `--download-images` option:
   - All images are downloaded to an `assets` folder in your GitBook directory
   - Markdown image references are updated to point to local files
   - Duplicate images are automatically handled (same URL is downloaded only once)
   - File names are generated based on the original URL or using a hash if no filename is available
   - Images are downloaded in parallel for efficiency

Example of image references in the generated markdown:
```markdown
![Image alt text](assets/image_name.jpg)
```

## Embedded Content Handling

The scraper can extract and properly format various types of embedded content:

### YouTube Videos
- Extracts video ID from different YouTube URL formats
- Creates both a markdown link and an HTML iframe embedding

### Google Workspace Embeds
- Supports Google Docs, Sheets, Slides, Forms, Calendar, and Drive files
- Preserves the original content with HTML iframe embeddings

### Other Embedded Objects
- Handles PDF documents with appropriate embedding
- Supports other object and embed elements
- Detects and processes Google Sites special embedded content divs

## Network Error Handling

The scraper includes robust error handling to deal with network issues:

1. **Automatic Retries**: Failed network requests will be retried up to 5 times with progressive delays
2. **Connection Pooling**: Optimized connection pool for efficient handling of multiple requests
3. **Error Tracking**: Pages with errors are recorded in `error_pages.txt` for later retry
4. **DNS Resolution Handling**: Resilient to temporary DNS resolution failures
5. **Timeout Management**: Configurable timeouts to handle slow connections

If you encounter network errors while scraping, the scraper will:

1. Retry the failed request multiple times
2. Continue processing other pages even if some pages fail
3. Generate a summary of failed pages at the end of the run
4. Create `error_pages.txt` with details of all failed pages

### Retrying Failed Pages

If some pages fail to scrape due to temporary network issues, you can use the included retry script:

```bash
./retry_failed.sh --error-file "gitbook_output/error_pages.txt" --download-images
```

This script will:
1. Read the error_pages.txt file generated during the initial run
2. Attempt to scrape only the failed pages again
3. Generate a report of successfully retried pages and any pages that still fail
4. Create a new file `still_failed_pages.txt` with details of pages that continue to fail

#### Retry Options

- `--error-file`: Path to the error_pages.txt file (default: "gitbook_output/error_pages.txt")
- `--download-images`: Flag to download images for retried pages (default: False)
- `--max-workers`: Maximum number of concurrent workers for image download (default: 10)

## Notes

- The script adds a small delay between requests to avoid hitting rate limits
- Some complex HTML elements may not be perfectly converted to Markdown
- Embedded content requires HTML support in the GitBook or markdown renderer
- When downloading many images, consider adjusting the `--max-workers` parameter based on your system capabilities

## License

MIT
