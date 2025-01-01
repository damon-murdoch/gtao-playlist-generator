import math, csv
import argparse
import sys, os
import random
import json

parser = argparse.ArgumentParser(description="GTA Online Race Playlist Generator")
parser.add_argument("input", type=str, help="Name of the data file to use (e.g. 'stunts' -> 'data/stunts.csv')")
parser.add_argument("-t", "--target", type=int, default=10, help="Optional target race distance (for lap races).")
parser.add_argument("-r", "--races", type=int, default=6, help="Number of races per playlist")
parser.add_argument("-mr", "--rating", type=int, default=0, help="Minimum rating for races to include")
parser.add_argument("-s", "--sort", action="store_true", help="Balance the ratings of jobs between playlists")
parser.add_argument("-sh", "--shuffle", action="store_true", help="Randomly shuffle jobs between playlists")

def sort_playlist(playlist, sort=False, shuffle=False):
    # Shuffle
    if shuffle:
        # Shuffle playlist randomly
        random.shuffle(playlist)

    # Sort
    if sort:
        # Sort playlist based on rating (Highest first)
        playlist.sort(key=lambda x: x["rating"], reverse=True)

    # Return the playlist
    return playlist

def build_playlist(reader, target=10, min_rating=0):

    # Empty list
    playlist = []
    
    # Loop over rows
    for row in reader:

        # Parse data
        name = row[0]
        rating = int(row[1])
        distance = float(row[2])

        # Greater than min. rating
        if rating >= min_rating:

            # Number of laps
            laps = 1

            # If the race is a lap race
            has_laps = bool(row[3] == 'false')
            if has_laps:
                # Generate the number of laps
                laps = math.ceil(target / distance)

            # Add to the list
            playlist.append({
                "name": name, 
                "rating": rating, 
                "distance": distance, 
                "laps": laps
            })

    # Completed playlist
    return playlist

if __name__ == '__main__':

    try:
        # Parse the arguments
        args = parser.parse_args()

        # Generate the file path
        path = f"data/{args.input}.csv"

        # Empty placeholder
        playlists = None

        # Attempt to open the file
        with open(path, "r") as file:

            # Read the csv data from the contents
            reader = csv.reader(file, delimiter=',')

            # Generate the playlist from the reader
            playlist = build_playlist(reader, args.target, args.rating)

            # Shuffle the playlist based on parameters
            sorted = sort_playlist(playlist, args.sort, args.shuffle)

            # Total number of races
            total_races = len(sorted)

            print(f"Number of races: {total_races} ...")

            # Calculate the total number of playlists
            total_playlists = math.floor(total_races/args.races)

            print(f"Number of playlists: {total_playlists} ...")

            # Default list
            playlists = []
            for p in range(total_playlists):
                playlists.append([])

            # Loop over the total races
            for index in range(total_races):
                race = playlist[index]

                # Get the index of the current playlist
                playlist_index = index % total_playlists

                # Get the data for the current playlist
                current_playlist = playlists[playlist_index]

                # Playlist already has num. races
                if len(current_playlist) >= args.races:
                    print(f"Warning: Extra race added to playlist {playlist_index}: {(len(current_playlist) + 1)} ...")

                # Add the race to the playlist
                playlists[playlist_index].append(race)

        # Playlists defined
        if playlists != None:
            # Dump the playlists to json
            with open("playlists.json", "w+") as file:
                json.dump(playlists, file, indent=2)

    except Exception as e:
        print(f"Failed to generate playlist for file '{path}'! {str(e)}")