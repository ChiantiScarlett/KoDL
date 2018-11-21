class KWeather:
    def __init__(self, key=None):
        self._key = key

    def authenticate(self, key):
        self._key = key
        # Run sample code
        pass

    def parse(self, X, Y, target_date, target_time):
        self.validate(target_date, target_time)
        endpoint = \
            "http://newsky2.kma.go.kr/service/" + \
            "SecndSrtpdFrcstInfoService2/ForecastSpaceData"

    def validate(self, target_date, target_time):
        """
        This method validates whether target_date and target_time are valid.
        """
        pass
