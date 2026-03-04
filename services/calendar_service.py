import datetime
import sxtwl

class CalendarService:
    def __init__(self):
        # 初始化天干地支映射表
        self.gan_map = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        self.zhi_map = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        
        # 基础五行属性 (简易对应)
        self.wuxing_gan = {"甲":"木", "乙":"木", "丙":"火", "丁":"火", "戊":"土", "己":"土", "庚":"金", "辛":"金", "壬":"水", "癸":"水"}
        self.wuxing_zhi = {"子":"水", "丑":"土", "寅":"木", "卯":"木", "辰":"土", "巳":"火", "午":"火", "未":"土", "申":"金", "酉":"金", "戌":"土", "亥":"水"}

    def get_daily_info(self, date_obj: datetime.date | None = None) -> dict:
        """
        获取指定日期的万年历和干支信息。如果不传则默认获取当天的信息。
        返回格式化好的日历字典，可以直接传给 Notion。
        """
        if date_obj is None:
            date_obj = datetime.date.today()
            
        lunar = sxtwl.fromSolar(date_obj.year, date_obj.month, date_obj.day)
        
        # 农历日期
        lunar_year = lunar.getLunarYear()
        lunar_month = lunar.getLunarMonth()
        lunar_day = lunar.getLunarDay()
        
        # 处理可能的闰月前缀
        month_prefix = "闰" if lunar.isLunarLeap() else ""
        
        # 农历中文表达 (比如: 正月初九)
        chinese_months = ["", "正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "冬月", "腊月"]
        chinese_days = ["", "初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", 
                           "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
                           "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]
                           
        lunar_chinese_str = f"{month_prefix}{chinese_months[lunar_month]}{chinese_days[lunar_day]}"

        # 干支计算
        yTG = lunar.getYearGZ()
        mTG = lunar.getMonthGZ()
        dTG = lunar.getDayGZ()
        
        year_gz = self.gan_map[yTG.tg] + self.zhi_map[yTG.dz]
        month_gz = self.gan_map[mTG.tg] + self.zhi_map[mTG.dz]
        day_gz = self.gan_map[dTG.tg] + self.zhi_map[dTG.dz]
        
        # 计算日柱的五行
        day_wuxing = f"天干{self.wuxing_gan[self.gan_map[dTG.tg]]} 地支{self.wuxing_zhi[self.zhi_map[dTG.dz]]}"

        # 拼接豪华万年历字符串
        full_lunar_str = f"{year_gz}年 {month_gz}月 {day_gz}日 (农历{lunar_chinese_str})"

        return {
            "solar_date": date_obj.isoformat(),
            "lunar_date": full_lunar_str,
            "year_gz": year_gz,
            "month_gz": month_gz,
            "day_gz": day_gz,
            "day_wuxing": day_wuxing
        }

# 实例化一个单例供外部文件直接引用
calendar_service = CalendarService()
