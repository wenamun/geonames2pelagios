import csv

def esc(chars):
  return chars.replace('"','\'').replace('\\','')

# list of featureClasses to export
# for geonames feature classes see: http://www.geonames.org/export/codes.html
featureClasses = ['A','H','P','S'] 
featuresFromClassS = ['AMTH','ANS','DAM','DIKE','FRM','GRVE','HSTS','PYR','PYRS','RUIN','TMPL']

with open('EG.txt') as f: # download country files from http://download.geonames.org/export/dump/
  output = open('geonames.ttl', 'w')
  
  output.write('@prefix dcterms: <http://purl.org/dc/terms/> .\n')
  output.write('@prefix foaf: <http://xmlns.com/foaf/0.1/> .\n')
  output.write('@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .\n')
  output.write('@prefix lawd: <http://lawd.info/ontology/> .\n')
  output.write('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n')
  output.write('@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n')
  output.write('@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\n')
  
  reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
  
  cnt = 0
  
  for row in reader:
    featureClass = row[6]
    feature = row[7]
    if featureClass in featureClasses:
      if (featureClass == "S" and feature not in featuresFromClassS):
          continue
      cnt = cnt + 1
      idGeonames = row[0]
      placename = row[1] # csv list of variant spellings
      altNames = row[3]
      lat = row[4]
      lon = row[5]
      
      output.write('<http://www.geonames.org/' + idGeonames + '> a lawd:Place ;\n')
      output.write('  rdfs:label "' + esc(placename) + '" ;\n')
      
      # write alternative names which is csv in variable placenames
      listOfPlacenames = altNames.split(',')
      if len(listOfPlacenames) > 1:
        output.write('  lawd:hasName\n')
        output.write('    [ lawd:primaryForm "' + listOfPlacenames[0] + '" ]')
        for p in listOfPlacenames[1:-1]:      
          output.write(',\n    [ lawd:primaryForm "' + esc(p) + '" ]')
        output.write(';\n')  

      if (lat and lon):
        output.write('  geo:location [ geo:lat "' + str(lat) + '"^^xsd:double ; geo:long "' + str(lon) + '"^^xsd:double ] ;\n')
      
      output.write('  .\n\n')

  output.close()
  print "Converted " + str(cnt) + " places.";

