#!/bin/bash
# Script to run the Google Site scraper and utilities

# Default values
SUMMARY_PATH="SUMMARY.md"
OUTPUT_DIR="gitbook_output"
TITLE="GitBook Documentation"
AUTHOR="Author"
DOWNLOAD_IMAGES=false
MAX_WORKERS=10
START_URL=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --summary)
      SUMMARY_PATH="$2"
      shift 2
      ;;
    --output)
      OUTPUT_DIR="$2"
      shift 2
      ;;
    --title)
      TITLE="$2"
      shift 2
      ;;
    --author)
      AUTHOR="$2"
      shift 2
      ;;
    --download-images)
      DOWNLOAD_IMAGES=true
      shift
      ;;
    --max-workers)
      MAX_WORKERS="$2"
      shift 2
      ;;
    --url)
      START_URL="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

echo "Starting Google Site scraper..."

# If a URL is provided, create a temporary SUMMARY.md file
if [ -n "$START_URL" ]; then
  echo "Creating temporary SUMMARY.md file from URL: $START_URL"
  echo "# Summary" > temp_summary.md
  echo "" >> temp_summary.md
  echo "* [Home]($START_URL)" >> temp_summary.md
  SUMMARY_PATH="temp_summary.md"
  echo "Using temporary summary file: $SUMMARY_PATH"
fi

echo "Summary file: $SUMMARY_PATH"
echo "Output directory: $OUTPUT_DIR"
echo "Title: $TITLE"
echo "Author: $AUTHOR"
echo "Download images: $DOWNLOAD_IMAGES"
echo "Max download workers: $MAX_WORKERS"

# Run the scraper
SCRAPER_CMD="python scraper.py --summary \"$SUMMARY_PATH\" --output \"$OUTPUT_DIR\""

# Add image download if specified
if [ "$DOWNLOAD_IMAGES" = true ]; then
  SCRAPER_CMD="$SCRAPER_CMD --download-images --max-workers $MAX_WORKERS"
fi

# Run the command
echo "Running: $SCRAPER_CMD"
eval $SCRAPER_CMD

# Check if the scraper was successful
if [ $? -ne 0 ]; then
  echo "Error: Scraper failed"
  exit 1
fi

echo "Scraper completed successfully"

# Run the post-processing utilities if needed
echo "Running post-processing utilities..."

# Prepare the command
UTILS_CMD="python utils.py --gitbook \"$OUTPUT_DIR\" --fix-links --create-book-json --title \"$TITLE\" --author \"$AUTHOR\""

# Run the command
echo "Running: $UTILS_CMD"
eval $UTILS_CMD

echo "All done! GitBook structure created in $OUTPUT_DIR"
echo "You can now use this with GitBook or any other Markdown-based documentation system."

# Clean up temp file if it was created
if [ -n "$START_URL" ]; then
  rm -f temp_summary.md
fi
