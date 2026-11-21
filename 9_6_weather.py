# 9.6 天气查询工具，继承实现
class WeatherBase:
    def get_weather(self):
        pass

    def forecast(self):
        pass


class BeijingWeather(WeatherBase):
    def get_weather(self):
        return "北京：晴，22℃"
    def forecast(self):
        return "北京未来三天晴天"


class ShanghaiWeather(WeatherBase):
    def get_weather(self):
        return "上海：多云，25℃"
    def forecast(self):
        return "上海未来两天有小雨"


if __name__ == "__main__":
    w1 = BeijingWeather()
    print(w1.get_weather())
    print(w1.forecast())
    w2 = ShanghaiWeather()
    print(w2.get_weather())