from fastapi import FastAPI, BackgroundTasks
import logging

from youtube_watchlater_api.youtube import YoutubeTools

logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project.
                                      # This will get the root logger since no logger in the configuration has this name.
app = FastAPI()


def write_watch_later_playlist():
    yt = YoutubeTools()
    info = yt.watch_later_fast()
    return info


@app.get("/")
def read_root(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_watch_later_playlist)
    file_path = (YoutubeTools.path/"watchlater-21.json")

    return file_path.read_json()['entries']


def start():
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
