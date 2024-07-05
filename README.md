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
* Run `./bin/geocode.py` to append `latitude` and `longitude` to `./csv/cooling_centers_2024.csv`

## TODO
* [Issues](https://github.com/pythoninthegrass/cooling_centers/issues)
* Transform [NY state CSV](csv/ny_cooling_centers_2024.csv) to match [OK state CSV](csv/ok_cooling_centers_2024.csv)
* Load all CSVs into a database
  * First `sqlite`, then `edgedb`
* Embed as an [iframe](https://python-visualization.github.io/folium/latest/advanced_guide/flask.html)
  * Sub FastAPI for Flask
* Fix `506 Williams St.` being geocoded as NaN / Georgia
* Remove OG&E's Arkansas locations
  * Maybe keep Fort Smith as that's close to the border at least
* Open locations on map in [new tab](https://www.freecodecamp.org/news/how-to-open-a-link-in-a-new-tab/)
