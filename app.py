from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>PinContext — Pinterest × AI</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                min-height: 100vh;

                display: flex;
                align-items: center;
                justify-content: center;

                font-family:
                    system-ui,
                    -apple-system,
                    BlinkMacSystemFont,
                    "Segoe UI",
                    sans-serif;

                background: #fafafa;
                color: #171717;
            }

            main {
                width: min(680px, 90%);
                text-align: center;
            }

            h1 {
                margin: 0;
                font-size: 4rem;
                letter-spacing: -0.05em;
            }

            .tagline {
                margin-top: 12px;
                font-size: 1.35rem;
                color: #666;
            }

            .description {
                margin: 32px auto;
                max-width: 540px;

                line-height: 1.7;
                color: #555;
            }

            .button {
                display: inline-block;

                padding: 14px 28px;

                border-radius: 999px;

                background: #111;
                color: white;

                text-decoration: none;
                font-weight: 600;

                transition:
                    transform 0.2s,
                    opacity 0.2s;
            }

            .button:hover {
                transform: translateY(-2px);
                opacity: 0.85;
            }

            footer {
                margin-top: 70px;

                font-size: 0.85rem;
                color: #999;
            }
        </style>
    </head>

    <body>
        <main>

            <h1>PinContext</h1>

            <div class="tagline">
                Pinterest × AI
            </div>

            <p class="description">
                Connect your Pinterest to your AI.
                Give your AI access to the visual context
                you've built and let it understand your pins,
                boards and interests.
            </p>

            <a class="button" href="#">
                Connect Pinterest
            </a>

            <footer>
                Your Pinterest. Your AI.
            </footer>

        </main>
    </body>
    </html>
    """


@app.get("/health")
def health():
    return {"status": "ok"}