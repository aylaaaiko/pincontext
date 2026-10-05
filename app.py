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

            footer a {
                color: #777;
                text-decoration: none;
            }

            footer a:hover {
                text-decoration: underline;
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
                <br><br>
                <a href="/privacy">Política de Privacidade</a>
            </footer>

        </main>
    </body>
    </html>
    """


@app.get("/privacy", response_class=HTMLResponse)
def privacy():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Política de Privacidade — PinContext</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                background: #fafafa;
                color: #171717;

                font-family:
                    system-ui,
                    -apple-system,
                    BlinkMacSystemFont,
                    "Segoe UI",
                    sans-serif;

                line-height: 1.7;
            }

            main {
                width: min(800px, 90%);
                margin: 0 auto;
                padding: 70px 0;
            }

            h1 {
                font-size: 2.8rem;
                line-height: 1.2;
                letter-spacing: -0.04em;
                margin-bottom: 10px;
            }

            h2 {
                margin-top: 45px;
                font-size: 1.35rem;
            }

            p {
                color: #444;
            }

            ul {
                color: #444;
            }

            .updated {
                color: #888;
                font-size: 0.9rem;
                margin-bottom: 50px;
            }

            a {
                color: #333;
            }

            .back {
                display: inline-block;
                margin-bottom: 45px;
                color: #666;
                text-decoration: none;
            }

            .back:hover {
                text-decoration: underline;
            }

            footer {
                margin-top: 70px;
                padding-top: 25px;
                border-top: 1px solid #ddd;
                color: #888;
                font-size: 0.9rem;
            }
        </style>
    </head>

    <body>
        <main>

            <a class="back" href="/">
                ← Voltar para o PinContext
            </a>

            <h1>Política de Privacidade</h1>

            <div class="updated">
                Última atualização: 5 de outubro de 2026
            </div>


            <h2>1. Sobre o PinContext</h2>

            <p>
                O PinContext é um projeto pessoal desenvolvido por
                Ayla Aiko com o objetivo de integrar dados do Pinterest
                a ferramentas de inteligência artificial para análise
                e organização de informações visuais.
            </p>

            <p>
                Nesta fase inicial, o PinContext é utilizado
                exclusivamente pela própria responsável pelo projeto
                para fins pessoais, de pesquisa e desenvolvimento.
            </p>

            <p>
                O PinContext não é afiliado, patrocinado ou endossado
                pelo Pinterest.
            </p>


            <h2>2. Dados acessados</h2>

            <p>
                O PinContext acessa somente os dados da conta do
                Pinterest que forem autorizados pela própria usuária
                por meio do processo oficial de autenticação OAuth.
            </p>

            <p>
                Na primeira versão do projeto, o acesso será limitado
                à leitura dos Pins da própria conta autenticada.
            </p>

            <p>
                O PinContext não solicita acesso a contas de terceiros
                e não pretende acessar dados de outros usuários nesta
                fase do projeto.
            </p>


            <h2>3. Como os dados são utilizados</h2>

            <p>
                Os dados acessados por meio da API do Pinterest são
                utilizados exclusivamente para:
            </p>

            <ul>
                <li>análise pessoal dos Pins;</li>
                <li>pesquisa e experimentação;</li>
                <li>organização e compreensão de informações visuais;</li>
                <li>desenvolvimento da integração entre Pinterest e IA.</li>
            </ul>

            <p>
                Os dados não são vendidos, alugados ou utilizados para
                publicidade.
            </p>


            <h2>4. Compartilhamento de dados</h2>

            <p>
                O PinContext não vende ou compartilha os dados
                acessados da conta do Pinterest com terceiros para
                fins comerciais.
            </p>

            <p>
                Caso funcionalidades futuras envolvam outros serviços
                de inteligência artificial ou terceiros, esta política
                será atualizada antes de tais funcionalidades serem
                disponibilizadas.
            </p>


            <h2>5. Armazenamento e segurança</h2>

            <p>
                O PinContext busca aplicar medidas técnicas adequadas
                para proteger credenciais, tokens de acesso e demais
                informações utilizadas pela integração com o Pinterest.
            </p>

            <p>
                Credenciais e tokens de acesso não devem ser armazenados
                diretamente no código-fonte público do projeto.
            </p>


            <h2>6. Revogação do acesso</h2>

            <p>
                A autorização concedida ao PinContext pode ser revogada
                pela usuária por meio das configurações de aplicativos
                da conta do Pinterest.
            </p>

            <p>
                Após a revogação, o PinContext não poderá continuar
                realizando chamadas à API do Pinterest em nome da
                conta utilizando a autorização revogada.
            </p>


            <h2>7. Alterações nesta política</h2>

            <p>
                Esta Política de Privacidade poderá ser atualizada
                conforme novas funcionalidades sejam adicionadas ao
                PinContext ou conforme os requisitos legais e das
                plataformas utilizadas pelo projeto sejam modificados.
            </p>

            <p>
                A data da última atualização será indicada no início
                desta página.
            </p>


            <h2>8. Contato</h2>

            <p>
                O PinContext é um projeto pessoal de Ayla Aiko.
            </p>

            <p>
                Questões relacionadas a esta Política de Privacidade
                podem ser encaminhadas à responsável pelo projeto por
                meio do canal de contato associado ao aplicativo.
            </p>


            <footer>
                PinContext — Pinterest × AI
            </footer>

        </main>
    </body>
    </html>
    """


@app.get("/health")
def health():
    return {"status": "ok"}