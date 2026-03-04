import datetime

# sxtwl文档可以参考: https://pypi.org/project/sxtwl/
# 可以通过 pip install sxtwl 安装
try:
    import sxtwl
except ImportError:
    print("错误：未检测到 sxtwl 库。请在激活的虚拟环境中运行: pip install sxtwl")
    exit(1)

def test_calendar(year, month, day):
    # sxtwl 传入公历年月日生成日历对象
    lunar = sxtwl.fromSolar(year, month, day)
    
    # 获取农历日期
    lunar_year = lunar.getLunarYear()
    lunar_month = lunar.getLunarMonth()
    lunar_day = lunar.getLunarDay()
    is_leap = lunar.isLunarLeap()
    
    # 提取干支数组（固定映射）
    Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    
    # 获取年、月、日的干支索引对象
    yTG = lunar.getYearGZ()
    mTG = lunar.getMonthGZ()
    dTG = lunar.getDayGZ()
    
    # 将索引映射到具体的中文字符
    year_gz = Gan[yTG.tg] + Zhi[yTG.dz]
    month_gz = Gan[mTG.tg] + Zhi[mTG.dz]
    day_gz = Gan[dTG.tg] + Zhi[dTG.dz]

    print(f"========== 万年历本地测试 (sxtwl) ==========")
    print(f"输入公历日期: {year}年{month}月{day}日")
    print(f"农历转换结果: {lunar_year}年 {'闰' if is_leap else ''}{lunar_month}月 {lunar_day}日")
    print(f"天干地支:")
    print(f"  [年柱]: {year_gz}")
    print(f"  [月柱]: {month_gz}")
    print(f"  [日柱]: {day_gz}")
    print("============================================")

if __name__ == "__main__":
    # 默认使用当天日期进行测试
    today = datetime.date.today()
    test_calendar(today.year, today.month, today.day)
