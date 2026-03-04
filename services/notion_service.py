import os
from notion_client import Client
from dotenv import load_dotenv

class NotionService:
    def __init__(self):
        # 确保在使用前加载了环境变量
        load_dotenv()
        # 初始化 Notion SDK Client
        token = os.getenv("NOTION_TOKEN")
        self.database_id = os.getenv("NOTION_DATABASE_ID")
        
        if not token or not self.database_id:
            raise ValueError("Error: NOTION_TOKEN or NOTION_DATABASE_ID environment variables are missing.")
            
        self.client = Client(auth=token)

    def create_diary_entry(self, solar_date: str, lunar_date: str, year_gz: str, month_gz: str, day_gz: str, content: str = "", tags: list[str] | None = None):
        """
        向指定的 Notion Database 插入一条新的日记记录。
        这里的属性 (Properties) 必须与 Notion 表格中的列名严格对应。
        如果没有事先在 Notion建好对应的列类型，这里可能会报错。我们约定基础列如下：
        - "Title" (Title): 日记标题
        - "Date" (Date): 公历日期
        - "Lunar" (Rich_text): 农历
        - "Ganzhi" (Multi-select): 干支组合标签
        - "Tags" (Multi-select): 用户自定义标签
        """
        if tags is None:
            tags = []
            
        # 组装属性 PayLoad
        properties_payload = {
            # 页面标题 (用户将首列命名为 Date)
            "Date": {
                "title": [
                    {
                        "text": {
                            "content": solar_date
                        }
                    }
                ]
            },
            # 年柱
            "Almanac Year": {
                "rich_text": [
                    {
                        "text": {
                            "content": year_gz
                        }
                    }
                ]
            },
            # 月柱
            "Almanac Month": {
                "rich_text": [
                    {
                        "text": {
                            "content": month_gz
                        }
                    }
                ]
            },
            # 日柱
            "Almanac Day": {
                "rich_text": [
                    {
                        "text": {
                            "content": day_gz
                        }
                    }
                ]
            }
        }

        # 为了不丢失干支数据，既然取消了 Tags，就把它们放进正文头部
        tag_str = ", ".join(tags) if tags else "无"
        full_content = f"【干支气场】{year_gz}年 {month_gz}月 {day_gz}日\n【今日标签】{tag_str}\n\n{content}"
        
        children_blocks = []
        if full_content:
             children_blocks.append({
                 "object": "block",
                 "type": "paragraph",
                 "paragraph": {
                     "rich_text": [
                         {
                             "type": "text",
                             "text": {
                                 "content": full_content
                             }
                         }
                     ]
                 }
             })

        # 调用 API 发送请求
        try:
            response = self.client.pages.create(
                parent={"database_id": self.database_id},
                properties=properties_payload,
                children=children_blocks
            )
            return response
        except Exception as e:
            # 捕获异常，比如用户 Notion 里的列名和我们上面定义的不一致时会引发异常
            print(f"Failed to create Notion Page: {e}")
            raise e

# 暴露实例给外部调用
notion_service = NotionService()
