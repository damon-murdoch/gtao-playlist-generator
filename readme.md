# GTA Online Race Playlist Generator
### Created By Damon Murdoch ([@SirScrubbington](https://github.com/SirScrubbington))

## Description

The GTA Online Race Playlist Generator is a Python script designed to help players create customized playlists of races based on their preferences. 
The script processes race data from a CSV file and organizes them into playlists with options for sorting, shuffling, and filtering by minimum rating and target race distance.

Please note, that this program does not actually perform the step of creating the playlists ingame - This must be done manually. This program simply aims to simplify the process
of generating balanced playlists. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Future Changes](#future-changes)
- [Problems / Improvements](#problems--improvements)
- [Changelog](#changelog)
- [Sponsor this Project](#sponsor-this-project)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SirScrubbington/gta-race-playlist-generator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd gta-race-playlist-generator
   ```

3. Install any required dependencies (if any are needed in future versions).

4. Ensure your race data is formatted as a CSV file in the following format and placed in the `data/` directory:
   ```csv
   Name,Rating,Distance,LapRace
   Race1,4,3.5,false
   Race2,5,2.8,true
   ```

## Usage

Run the script with the required arguments:

```bash
python script.py <input> [-t TARGET] [-r RACES] [-mr RATING] [-s] [-sh]
```

### Arguments:
- `input`: The name of the data file to use (e.g., `stunts` -> `data/stunts.csv`).
- `-t`, `--target`: Optional target race distance for lap races (default: 10).
- `-r`, `--races`: Number of races per playlist (default: 6).
- `-mr`, `--rating`: Minimum rating for races to include (default: 0).
- `-s`, `--sort`: Balance the ratings of jobs between playlists.
- `-sh`, `--shuffle`: Randomly shuffle jobs between playlists.

### Example:

```bash
python script.py stunts -t 15 -r 8 -mr 4 -s -sh
```

This command generates playlists using the `data/stunts.csv` file, targeting a lap distance of 15, with 8 races per playlist, a minimum rating of 4, sorting the ratings, and shuffling the jobs.

### Output:
The playlists are saved in a JSON file named `playlists.json` in the project directory.

## Future Changes

List any planned fixes or improvements for the future.

### Change Table

| Change Description            | Priority |
| ----------------------------- | -------- |
| No Planned Changes            | -        | 

## Problems / Improvements

If you have any suggested improvements for this project or encounter any issues, please feel free to open an
issue [here](../../issues) or send me a message on Twitter detailing the issue and how it can be replicated.

## Changelog

### Ver. 1.0.0

- Initial release of the GTA Online Race Playlist Generator.
- Added support for sorting and shuffling playlists.
- Minimum rating filter implemented.

## Sponsor this Project

If you'd like to support this project and other future projects, please feel free to use the PayPal donation link below.
[https://www.paypal.com/paypalme/sirsc](https://www.paypal.com/paypalme/sirsc)

## License

This project is licensed under the MIT License.
