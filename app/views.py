from fastapi import APIRouter, BackgroundTasks
from app.models import Event
from app.database import save_event
from app.utils import aggregate_data, generate_plot
from fastapi.responses import FileResponse
import io

router = APIRouter()

@router.post("/events/")
async def collect_event(event: Event, background_tasks: BackgroundTasks):
    background_tasks.add_task(save_event, event)
    return {"status": "accepted"}

@router.get("/aggregate/")
async def get_aggregate_data(timeframe: str):
    aggregated_data = aggregate_data(timeframe)
    return aggregated_data.to_dict()

@router.get("/visualize/{timeframe}/")
async def visualize_data(timeframe: str):
    df = aggregate_data(timeframe)
    img_buf = generate_plot(df)
    return FileResponse(img_buf, media_type="image/png")
