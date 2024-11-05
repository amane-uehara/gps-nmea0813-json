class Const(object):
  __LABEL_DICT = {
    "$GPGGA": [
      "sentence type",
      "current time (hhmmss.fff)",
      "latitude (ddmm.mmmm)",
      "latitude compass direction",
      "longitude (dddmm.mmmm)",
      "longitude compass direction",
      "fix type",
      "number of satellites used for fix",
      "horizontal dilution of precision",
      "altitude above mean sea level",
      "altitude units",
      "geoidal separation",
      "units of the above geoid seperation",
      "time since last differential correction",
      "differential station ID",
      "checksum validation",
    ],

    "$GPGSA": [
      "sentence type",
      "mode (Manual Automatic)",
      "mode (Dimension)",
      "SV PRN number [0]",
      "SV PRN number [1]",
      "SV PRN number [2]",
      "SV PRN number [3]",
      "SV PRN number [4]",
      "SV PRN number [5]",
      "SV PRN number [6]",
      "SV PRN number [7]",
      "SV PRN number [8]",
      "SV PRN number [9]",
      "SV PRN number [10]",
      "SV PRN number [11]",
      "position Dilution of Precision",
      "horizontal dilution of precision",
      "vertical Dilution of Precision",
      "checksum validation",
    ],

    "$GPGSV": [
      "sentence type",
      "total number of messages",
      "message number",
      "total number of SVs in view",
      "SV PRN number [0]",
      "elevation (degree) [0]",
      "azimuth (degree) [0]",
      "signal to Noise Ratio (dB) [0]",
      "SV PRN number [1]",
      "elevation (degree) [1]",
      "azimuth (degree) [1]",
      "signal to Noise Ratio (dB) [1]",
      "SV PRN number [2]",
      "elevation (degree) [2]",
      "azimuth (degree) [2]",
      "signal to Noise Ratio (dB) [2]",
      "SV PRN number [3]",
      "elevation (degree) [3]",
      "azimuth (degree) [3]",
      "signal to Noise Ratio (dB) [3]",
      "checksum validation",
    ],

    "$GPRMC": [
      "sentence type",
      "current time (hhmmss.fff)",
      "data validity flag",
      "latitude (ddmm.mmmm)",
      "latitude compass direction",
      "longitude (dddmm.mmmm)",
      "longitude compass direction",
      "speed (knots/hour)",
      "heading",
      "date (ddmmyy)",
      "magnetic variation",
      "magnetic variation direction",
      "positioning system mode indicator",
      "checksum validation",
    ]
  }

  @property
  def label_dict(self) -> dict:
    return self.__LABEL_DICT