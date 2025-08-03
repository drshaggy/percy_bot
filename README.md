# Percy Bot

A chess position analysis bot using computer vision and machine learning.

## Dependencies

### ChessCog
This project requires the ChessCog library as a dependency. To set it up:

```bash
# Clone the ChessCog repository
git clone https://github.com/chesscog/chesscog.git

# Follow the installation instructions in the ChessCog repository
cd chesscog
# (Follow ChessCog's setup instructions)
```

## Setup

1. Install the ChessCog dependency as described above
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt  # (if requirements.txt exists)
   ```

## Usage

Run the main script:
```bash
python main.py
```

## Files

- `main.py` - Main application entry point
- `image_board.py` - Chess board image processing
- `download_training_example.py` - Training data utilities
- Various PNG files - Chess board images and test positions