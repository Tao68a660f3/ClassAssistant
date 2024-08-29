from cityData import *
import requests
from lxml import html

class WeatherGeter():
    def __init__(self, cityData):
        self.cityData = cityData
        self.index = None
        self.area_ID = None
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
        self.area_ID = self.index.get(name_cn)

    def get_report_url_1d(self):
        return f"https://www.weather.com.cn/weather1d/{self.area_ID}.shtml"
    
    def get_weather_content(self):
        url = self.get_report_url_1d()
        response = requests.get(url)
        if response.status_code == 200:
            # 解析网页内容
            tree = html.fromstring(response.content)
            
            # 使用XPath定位天气信息
            weather_info = tree.xpath('/html/body/div[5]/div[1]/div[1]/div[2]/div[1]/ul')[0]

            # 删除class为"sky"的部分
            for element in weather_info.xpath('.//div[@class="sky"]'):
                element.getparent().remove(element)

            # 处理风速风向情况
            for element in weather_info.xpath('.//span[@title]'):
                title = element.get('title')
                text = element.text
                if title and text:
                    new_text = f"{title}{text}"
                    element.text = new_text

        today_content = weather_info.text_content().replace("\n", " ").strip()
        return today_content

if __name__ == "__main__":
    # Example usage
    Weather_Geter = WeatherGeter(city_data)
    name_cn = "岳麓"
    Weather_Geter.get_area_id(name_cn)
    weather_content = Weather_Geter.get_weather_content()
    print(weather_content)
