import mapnik
m = mapnik.Map(3840,2160)
m.background = mapnik.Color('steelblue')
# MAP 1 JAWA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#7FFF00')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('umar',s)
ds = mapnik.Shapefile(file="shp batas desa/Desa_Jawa.shp")
layer = mapnik.Layer('desa')
layer.datasource = ds
layer.styles.append('umar')
m.layers.append(layer)
# BATAS DESA

# MAP 2 JAWA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#D2691E')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('umar2',s)
ds = mapnik.Shapefile(file="shp batas kabupaten jawa/batas_kab.shp")
layer = mapnik.Layer('kabupaten')
layer.datasource = ds
layer.styles.append('umar2')
m.layers.append(layer)
# BATAS KABUPATEN

# MAP 3 JAWA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#00FFFF')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('umar3',s)
ds = mapnik.Shapefile(file="shp batas kecamatan/batas_kecamatan.shp")
layer = mapnik.Layer('kecamatan')
layer.datasource = ds
layer.styles.append('umar3')
m.layers.append(layer)
# BATAS KECAMATAN

# MAP 4 JAWA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FF0000')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('umar4',s)
ds = mapnik.Shapefile(file="shp batas provinsi/batas_prov.shp")
layer = mapnik.Layer('provinsi')
layer.datasource = ds
layer.styles.append('umar4')
m.layers.append(layer)
# BATAS PROVBINSI

# MAP 5 JAWA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FF00FF')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('umar5',s)
ds = mapnik.Shapefile(file="shp jalan utama/jalan_utama.shp")
layer = mapnik.Layer('jalan utama')
layer.datasource = ds
layer.styles.append('umar5')
m.layers.append(layer)
# BATAS JALAN UTAMA

m.zoom_all()
mapnik.render_to_file(m,'tugas5.pdf','pdf')
print "rendered image to 'tugas5.pdf '"