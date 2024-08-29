from cityData import *
import requests, re
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
    
    def get_weather_content(self,time):
        if time == "1d":
            url = f"https://www.weather.com.cn/weather1d/{self.area_ID}.shtml"
        elif time == "7d":
            url = f"https://www.weather.com.cn/weather/{self.area_ID}.shtml"
        else:
            url = f"https://www.weather.com.cn/weather/{self.area_ID}.shtml"

        response = requests.get(url)
        if response.status_code == 200:
            # 解析网页内容
            tree = html.fromstring(response.content)
            
            # 使用XPath定位天气信息
            if time == "1d":
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

            elif time == "7d":
                weather_info = tree.xpath('/html/body/div[5]/div[1]/div[1]/div[2]/ul')[0]

                # 处理风速风向情况
                for element in weather_info.xpath('.//p[@class="win"]'):
                    wind_direction = element.xpath('.//span/@title')[0]
                    wind_level = element.xpath('.//i')[0].text
                    new_text = f"{wind_direction}{wind_level}"
                    element.xpath('.//i')[0].text = new_text

            else:
                weather_info = tree.xpath('/html/body/div[5]/div[1]/div[1]/div[2]/ul')[0]

            content = weather_info.text_content().replace("\n", " ").replace("（", "(").replace("）", ")")
            content = re.sub(r" +"," ",content)
            content = re.sub(r"([0-9]+日)",r"  ✦ \1",content).strip()
        else:
            content = 'Failed to retrieve the website'

        return content

if __name__ == "__main__":
    # Example usage
    Weather_Geter = WeatherGeter(city_data)
    name_cn = "大祥"
    Weather_Geter.get_area_id(name_cn)
    weather_content = Weather_Geter.get_weather_content("7d")
    print(weather_content)
