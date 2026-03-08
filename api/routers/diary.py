from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import datetime

from services.calendar_service import calendar_service
from services.notion_service import notion_service

router = APIRouter(prefix="/api/diary", tags=["destiny-diary"])


class DiaryEntryRequest(BaseModel):
    date: Optional[str] = None  # 支持用户手动传入 'YYYY-MM-DD'，不传则用今天
    content: str = ""
    tags: List[str] = []

@router.post("/")
async def create_diary(entry: DiaryEntryRequest):
    """
    提交日记：
    1. 根据公历获取干支和农历
    2. 配合用户自己的 tags 和 content，写入 Notion 数据库中
    """
    try:
        # 处理日期
        target_date = datetime.date.today()
        if entry.date:
            target_date = datetime.date.fromisoformat(entry.date)
            
        # 1. 提取干支大数​​据特征
        cal_info = calendar_service.get_daily_info(target_date)
        
        # 2. 调用 Notion 服务将混合数据推送到数据库
        response = notion_service.create_diary_entry(
            solar_date=cal_info["solar_date"],
            lunar_date=cal_info["lunar_date"],
            year_gz=cal_info["year_gz"],
            month_gz=cal_info["month_gz"],
            day_gz=cal_info["day_gz"],
            content=entry.content,
            tags=entry.tags
        )
        
        return {
            "status": "success",
            "message": "Destiny Diary entry saved to Notion.",
            "calendar_used": cal_info,
            "notion_url": response.get("url")
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
