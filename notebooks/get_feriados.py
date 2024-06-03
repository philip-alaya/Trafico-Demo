
import requests

contents=requests.get("https://apis.digital.gob.cl/fl/feriados").contents.decode()
print(str(contents))