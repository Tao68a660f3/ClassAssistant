import requests
from lxml import html

# 发送请求
url = 'https://www.weather.com.cn/weather1d/101250109.shtml'
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
    

    print(weather_info.text_content().replace("\n", " ").strip())
else:
    print('Failed to retrieve the website')