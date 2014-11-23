# geonames2pelagios

This script converts a geonames.org country export file (http://download.geonames.org/export/dump/) into the Pelagios Gazetteer Interconnection Format (https://github.com/pelagios/pelagios-cookbook/wiki/Pelagios-Gazetteer-Interconnection-Format).

Geonames feature classes A (country, state, region,...), H (stream, lake, ...) and P (city, village,...) are converted completely, from feature class S (spot, building, farm) only a small subset is useful for Pelagios (see python list `featuresFromClassS` in the script)
; for geonames feature codes see http://www.geonames.org/export/codes.html.
