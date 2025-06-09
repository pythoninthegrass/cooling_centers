# Oklahoma Cooling Centers

Originally a fork of [Oklahoma Cooling Centers](https://github.com/alex-code4okc/oklahoma_cooling_centers_python), now it's a standalone repo that aims to aggregate all public cooling centers in the United States.

Shoutout to [Alex Ayon](https://github.com/alex-code4okc) for the original local implementation and general idea! 🎉

## Minimum Requirements

* [python3.11+](https://www.python.org/downloads/)

## Recommended Requirements

* [devbox](https://www.jetify.com/devbox/docs/quickstart/)

## Quickstart

This is just for the map portion. The backend is still in development.

```bash
# create virtual environment
python3 -m venv .venv

# activate virtual environment
source .venv/bin/activate

# install dependencies
python3 -m pip install -r requirements.txt

# run script
./make_map.py

# open map in browser
open ./docs/index.html

# deactivate virtual environment
deactivate
```

## Development

### Read PDF

* ImageMagick is a problem child for `pdftotree` on macOS. Run the following to use `gen_csv.py`:

```bash
# install imagemagick v6
brew uninstall imagemagick
brew install imagemagick@6
brew unlink imagemagick
brew link imagemagick@6 --force

# ~/.bashrc
export BREW_PREFIX=$(brew --prefix)
export MAGICK_HOME="$BREW_PREFIX/opt/imagemagick@6"
```

* Run `./bin/gen_csv.py` to generate `./csv/cooling_centers_2024.csv`

### Geocoding

* Open a free Google Cloud Platform account and [setup the Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview)
* Fill out `.env` with your API key
* Run `./bin/geocode.py` to append `latitude_longitude` and prepend `city_county` to a CSV file
  * Needs to be in the `csv` directory
  * Named with state abbreviation and year (e.g., `ok_cooling_centers_2024.csv`)
  * Can be set in `.env` as `CSV_FILE`

## TODO

See [TODO.md](TODO.md) for more details.
