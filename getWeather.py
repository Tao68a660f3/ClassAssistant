from cityData import *

class WeatherUrlGeter():
    def __init__(self, cityData):
        self.cityData = cityData
        self.index = None

        self.create_index()

    def create_index(self):
        index = {}
        for province in self.cityData.values():
            for city in province.values():
                for district in city.values():
                    index[district.get("NAMECN")] = district.get("AREAID")
        # return index
        self.index = index    

    def get_area_id(self,name_cn):
        return self.index.get(name_cn)

    def get_report_url(self,name_cn):
        area_id = self.get_area_id(name_cn)
        return f"https://www.weather.com.cn/weather1d/{area_id}.shtml"
    

if __name__ == "__main__"
    # Example usage
    Url_Geter = WeatherUrlGeter(city_data)
    name_cn = "岳麓"
    print(Url_Geter.get_report_url(name_cn))
