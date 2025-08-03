# CLAUDE.md - Percy Bot

This file provides context to Claude Code when working with the Percy Bot project.

## Project Overview

Percy Bot is a chess position analysis system that uses computer vision and machine learning to analyze chess positions from images. The project combines image processing techniques with the ChessCog library for chess position recognition.

## Key Components

- **main.py** - Main application entry point
- **image_board.py** - Chess board image processing and analysis
- **download_training_example.py** - Utilities for downloading and preparing training data

## Dependencies

### ChessCog
This project depends on the ChessCog library (https://github.com/chesscog/chesscog), which provides:
- Chess position recognition from images
- Board detection and piece classification
- Neural network models for chess piece recognition

The ChessCog dependency should be cloned separately as it's not included in this repository.

## Development Notes

- The project contains various test images (PNG files) for chess positions and board states
- Image processing focuses on chess board detection and piece recognition
- The system appears to work with both empty boards and positioned pieces

## Architecture

The project follows a modular approach:
1. Image input and preprocessing
2. Board detection and segmentation
3. Piece recognition using ChessCog
4. Position analysis and output

## Testing

Test images included:
- `chess_board.png`, `chess_board_empty.png` - Board reference images
- `position1.png`, `test_position.png` - Test chess positions
- Various piece-specific images for validation