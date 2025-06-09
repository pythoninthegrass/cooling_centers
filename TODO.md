# TODO

* [Issues](https://github.com/pythoninthegrass/cooling_centers/issues)
* Load all CSVs into a database
  * First `sqlite`, then `neon`
* Embed as an [iframe](https://python-visualization.github.io/folium/latest/advanced_guide/flask.html)
  * Sub FastAPI for ~~Flask~~ Plain
* Transform
  * Fix NaN values
    * Missing cells (e.g., `city_county`, `latitude_longitude`)
    * `506 Williams St.` being geocoded as NaN / Georgia
  * Normalize
    * phone numbers
    * hours of operation
  * Remove OG&E's Arkansas locations
    * Maybe keep Fort Smith as that's close to the border at least
* Open locations on map in [new tab](https://www.freecodecamp.org/news/how-to-open-a-link-in-a-new-tab/)
