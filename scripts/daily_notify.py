import os
import sys
import asyncio
import datetime
from dotenv import load_dotenv

# Ensure we can import from the root project directory (services module)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.calendar_service import calendar_service
from services.telegram_service import send_telegram_message

# Load .env variables (useful for local testing)
load_dotenv()

def generate_daily_message() -> str:
    today = datetime.date.today()
    cal_info = calendar_service.get_daily_info(today)
    
    msg = f"🌅 **{cal_info['solar_date']} 每日运势播报**\n\n"
    msg += f"📅 **农历**: {cal_info['lunar_date']}\n"
    msg += f"🌀 **干支**: {cal_info['year_gz']}年 {cal_info['month_gz']}月 {cal_info['day_gz']}日\n"
    msg += f"☯️ **今日五行**: {cal_info['day_wuxing']}\n\n"
    msg += "🌻 *愿你今天像向日葵一样充满阳光与能量！* 🌻"
    
    return msg

async def main() -> bool:
    print(f"[{datetime.datetime.now()}] Starting daily notification script...")
    message = generate_daily_message()
    print("Generated Message:\n", message)
    
    success = await send_telegram_message(message)
    if success:
        print("✅ Notification sent successfully!")
        return True
    else:
        print("❌ Failed to send notification.")
        return False

def lambda_handler(event, context):
    """AWS Lambda entry point"""
    success = asyncio.run(main())
    if success:
        return {"statusCode": 200, "body": "Success"}
    else:
        return {"statusCode": 500, "body": "Failed to send notification"}

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
