import os
from datetime import datetime
from blacksheep.server import Application
from blacksheep.options import ServerOptions
from blacksheep.server.responses import text


app = Application(options=ServerOptions('0.0.0.0', int(os.environ.get('SERVER_PORT', '44555'))))

@app.route('/')
async def home(request):
    return text(f'Hello, World! {datetime.utcnow().isoformat()}')

app.start()
