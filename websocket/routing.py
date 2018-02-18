from channels.routing import route
from channels_tut.consumers import ws_connect, ws_disconnect
ASGI_APPLICATION = "websocket.routing.application"

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]