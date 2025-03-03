#!/bin/bash

# Retry Failed Pages Script
# This script retries the pages that failed during the initial scraping

# Default values
ERROR_FILE="gitbook_output/error_pages.txt"
DOWNLOAD_IMAGES=false
MAX_WORKERS=10

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  key="$1"

  case $key in
    --error-file)
      ERROR_FILE="$2"
      shift # past argument
      shift # past value
      ;;
    --download-images)
      DOWNLOAD_IMAGES=true
      shift # past argument
      ;;
    --max-workers)
      MAX_WORKERS="$2"
      shift # past argument
      shift # past value
      ;;
    *)    # unknown option
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

# Display parameters
echo "Starting retry for failed pages..."
echo "Error file: $ERROR_FILE"
echo "Download images: $DOWNLOAD_IMAGES"
echo "Max download workers: $MAX_WORKERS"

# Build the Python command
CMD="python retry_failed.py --error-file \"$ERROR_FILE\""

if $DOWNLOAD_IMAGES; then
  CMD="$CMD --download-images"
fi

CMD="$CMD --max-workers $MAX_WORKERS"

# Run the command
echo "Running: $CMD"
eval $CMD

if [ $? -eq 0 ]; then
  echo "Retry completed successfully."
else
  echo "Error: Retry failed."
  exit 1
fi
