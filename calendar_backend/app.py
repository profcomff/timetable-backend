from fastapi import FastAPI, Query, HTTPException
from sqlalchemy import and_

from connect import timetable, engine

app = FastAPI()


@app.get('/timetable/group/{group_num}')
async def get_timetable_by_group(group_num: str = Query(..., description="Group number")) -> list[dict[str]]:
    s = timetable.select().where(timetable.columns.group == group_num)
    result = engine.execute(s).fetchall()
    if not result:
        raise HTTPException(status_code=404, detail="Timetable not found")
    return result


@app.get('/timetable/teacher/{teacher_name}')
async def get_timetable_by_teacher(teacher_name: str = Query(..., description="Teacher name")) -> list[dict[str]]:
    s = timetable.select().where(timetable.columns.teacher == teacher_name)
    result = engine.execute(s).fetchall()
    if not result:
        raise HTTPException(status_code=404, detail="Timetable not found")
    return result


@app.get('/timetable/audience/{audience_num}')
async def get_timetable_by_place(audience_num: str = Query(..., description="Audience number")) -> list[dict[str]]:
    s = timetable.select().where(timetable.columns.place == audience_num)
    result = engine.execute(s).fetchall()
    if not result:
        raise HTTPException(status_code=404, detail="Timetable not found")
    return result


@app.get('/timetable/group_weeakday/{group},{weekday}')
async def get_timetable_by_group_and_weekday(group: str = Query(..., description="Group number"),
                                             weekday: int = Query(..., description="Weekday")) -> list[dict[str]]:
    s = timetable.select().where(and_(timetable.columns.group == group, timetable.columns.weekday == weekday))
    result = engine.execute(s).fetchall()
    if not result:
        raise HTTPException(status_code=404, detail="Timetable not found")
    return result