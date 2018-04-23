import mapnik
m = mapnik.Map(1080,480)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#ff3300')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')


r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('umar',s)
ds = mapnik.Shapefile(file="shp kota/batas_kab.shp")
layer = mapnik.Layer('kabupaten')
layer.datasource = ds 
layer.styles.append('umar')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'kabupaten.pdf', 'pdf')
print "rendered image to 'kabupaten.pdf'"
