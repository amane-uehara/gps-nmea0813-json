from const import Const
import fileinput
import json
from datetime import datetime, timezone, timedelta

def main():
  for line in fileinput.input():
    lst = line.strip().split("*")[0].split(",")
    sentence_type = lst[0]
    if sentence_type == "$GPRMC":
      dct = {}
      for index in range(len(lst)):
        label = Const().label_dict[sentence_type][index]
        dct[label] = lst[index]

      iso8601 = to_iso8601(dct)
      unixtime = datetime.fromisoformat(iso8601).timestamp()
      dt = to_yyyymmddhhmmss_jtc(iso8601)

      longtitude       = ddmm_to_decimal_degrees(dct["longitude (dddmm.mmmm)"], dct["longitude compass direction"])
      latitude         = ddmm_to_decimal_degrees(dct["latitude (ddmm.mmmm)"], dct["latitude compass direction"])
      speed            = knot_to_km(dct["speed (knots/hour)"])
      heading          = dct["heading"]
      validity_mode    = dct["data validity flag"]
      positioning_mode = dct["positioning system mode indicator"]
      print(f"{dt},{unixtime},{latitude:.7f},{longtitude:.7f},{speed:.1f},{heading},{validity_mode},{positioning_mode}")

def to_iso8601(dct):
  dd  = dct["date (ddmmyy)"][0:2]
  MM  = dct["date (ddmmyy)"][2:4]
  yy  = dct["date (ddmmyy)"][4:6]
  HH  = dct["current time (hhmmss.fff)"][0:2]
  mm  = dct["current time (hhmmss.fff)"][2:4]
  ss  = dct["current time (hhmmss.fff)"][4:6]
  fff = dct["current time (hhmmss.fff)"][7:10]
  return f"20{yy}-{MM}-{dd}T{HH}:{mm}:{ss}.{fff}+00:00"

def to_yyyymmddhhmmss_jtc(iso8601):
  utc_time = datetime.fromisoformat(iso8601)
  jst_timezone = timezone(timedelta(hours=9))
  jst_time = utc_time.astimezone(jst_timezone)
  return jst_time.strftime('%Y%m%d%H%M%S')

def ddmm_to_decimal_degrees(ddmm_str, direction):
  ddmm = float(ddmm_str)
  degrees = int(ddmm // 100)
  minutes = ddmm % 100
  decimal_degrees = degrees + (minutes / 60)
  if direction == 'S' or direction == 'W':
    decimal_degrees = -1.0 * decimal_degrees
  return decimal_degrees

def knot_to_km(knot_str):
  return float(knot_str)*1.852

main()

