import requests 
import pickle 
import json 




        
html1=(''' 
        
         <html>
  <head>
    <script src="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.js"></script>
    <link type="text/css" rel="stylesheet" href="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.css"/>
    <script src="https://leaflet.github.io/Leaflet.heat/dist/leaflet-heat.js"></script>
    <script src="nguyen_tyson.js"></script>

    <script type="text/javascript">
      window.onload = function() {
        L.mapquest.key = 'SRw3G61kG2oPxIUKnOt0Om8vuzSDxImn';
        var baseLayer = L.mapquest.tileLayer('map');

        var map = L.mapquest.map('map', {
          center: [39.8283, -98.5795],
          layers: baseLayer,
          zoom: 12
        });

        addressPoints = addressPoints.map(function (addressPoint) { return [addressPoint[0], addressPoint[1]]; });

        L.heatLayer(addressPoints).addTo(map);
      }
    </script>
  </head>

  <body style="border: 0; margin: 0;">
    <div id="map" style="width: 100%; height: 530px;"></div>
  </body>
</html>
        
        
        ''' )
        


f= open('nguyen_tyson.html','w')
f.write(html1)
f.close()

js_content='var addressPoints=['

with open("SampleLatLon.txt") as f:
    next(f)
    for line in f:
        lat=line.split("\t")[0]
        lon=line.split("\t")[1]
        count=line.split("\t")[2]
        count=count.rstrip("\n")
        
        
        js_content=js_content+ "\n[" +lat+ ","+ lon+","+ count +"],"
        
js_content=js_content.strip(",")
js_content=js_content+"];"



f1=open("nguyen_tyson.js","w")
f1.write(js_content)
f1.close()

        
