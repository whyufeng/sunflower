from services.notion_service import notion_service
from services.calendar_service import calendar_service
import datetime

cal_info = calendar_service.get_daily_info(datetime.date.today())
try:
    response = notion_service.create_diary_entry(
        solar_date=cal_info["solar_date"],
        lunar_date=cal_info["lunar_date"],
        year_gz=cal_info["year_gz"],
        month_gz=cal_info["month_gz"],
        day_gz=cal_info["day_gz"],
        content="太阳花命运日记项目正式起航！这是绕开缓存直接发送的纯净版数据测试！",
        tags=["测试", "连通", "破冰"]
    )
    print("Success! Page created:", response.get("url"))
except Exception as e:
    print(f"Failed! Exception: {e}")
