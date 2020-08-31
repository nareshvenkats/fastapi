import asyncio
from typing import Generic, MutableMapping, TypeVar

import attr
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

_T = TypeVar("_T")

@attr.s(frozen=True, slots=True, auto_attribs=True)
class _IdEq(Generic[_T]):
    v: _T
    def __eq__(self, other: object):
        return isinstance(other, _IdEq) and self.v is other.v

    def __hash__(self):
        return hash(id(self.v))


class ConnectionManager:
    def __init__(self):
        self.active_connections: MutableSet[_IdEq(WebSocket)] = set()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(_IdEq(websocket))

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(_IdEq(websocket))

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        return await (
            asyncio.gather(
                *(conn.v.send_text(message) for conn in self.active_connections),
                return_exceptions=True
            )
        )


manager = ConnectionManager()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
