# video-embed

> 🇧🇷 [Português](#o-que-você-encontrará-neste-repositório) · 🇺🇸 [English](#what-will-you-find-in-this-repository)

## O que você encontrará neste repositório?

Ferramenta feita **sob encomenda** entre **março e abril de 2023** (chamada internamente de "PyCaption") para montar
vídeos verticais de redes sociais: ela pega um vídeo de **legenda** gravado sobre fundo verde e o sobrepõe a um vídeo
de **fundo**, gerando um vídeo final em 1080×1920 com o áudio da legenda.

Como funciona (`app/`):

1. lê os dois vídeos quadro a quadro com OpenCV e os redimensiona para o tamanho de saída;
2. faz o *chroma key*: converte o quadro da legenda para o espaço de cor LAB e aplica o limiar de Otsu no canal A, que
   separa o verde do resto, mantendo só o texto/emoji da legenda sobre o fundo;
3. comprime o resultado com ffmpeg (H.264) e acrescenta o áudio extraído do vídeo de legenda.

Tudo roda dentro de um contêiner **Docker**, para que o resultado seja o mesmo em qualquer máquina; o `handler.py`
constrói a imagem e executa o contêiner montando as pastas de entrada e saída.

### Estrutura

```
├── handler.py              # instala (docker build) e roda (docker run) o contêiner
├── Dockerfile              # Python + ffmpeg
├── .env.example            # caminhos, nomes dos arquivos e tamanho de saída
└── app/
    ├── main.py             # fluxo: ler → sobrepor → comprimir → adicionar áudio
    ├── environment/        # leitura das variáveis e checagem dos arquivos de entrada
    └── utils/              # vídeo (captura, escrita, compressão), imagem (chroma key) e áudio
```

### Ferramentas

Python 3, OpenCV, NumPy, ffmpeg, Docker e python-dotenv.

### Como usar

É preciso ter o [Docker](https://docs.docker.com/get-docker/) instalado e rodando.

```bash
git clone https://github.com/tofolo17/video-embed.git
cd video-embed
pip install python-dotenv
mkdir input output
cp .env.example .env   # ajuste INPUT_PATH e OUTPUT_PATH para os caminhos absolutos dessas pastas
```

Coloque na pasta `input/` um vídeo de fundo (`background.mp4`) e um vídeo de legenda sobre fundo verde (`caption.mp4`),
ou ajuste os nomes no `.env`. Então:

```bash
python handler.py --action install   # constrói a imagem docker-cv
python handler.py --action run       # gera output/output.mp4
```

> Os vídeos de exemplo usados no desenvolvimento eram de terceiros e foram removidos da versão pública.

---

## What will you find in this repository?

A tool **commissioned by a client** between **March and April 2023** (internally called "PyCaption") to build vertical
social-media videos: it takes a **caption** video recorded over a green screen and overlays it on a **background**
video, producing a final 1080×1920 video with the caption's audio.

How it works (`app/`):

1. reads both videos frame by frame with OpenCV and resizes them to the output size;
2. does the *chroma key*: converts the caption frame to the LAB color space and applies Otsu's threshold on the A
   channel, which separates green from everything else, keeping only the caption's text/emoji over the background;
3. compresses the result with ffmpeg (H.264) and adds the audio extracted from the caption video.

Everything runs inside a **Docker** container so the output is the same on any machine; `handler.py` builds the image
and runs the container, mounting the input and output folders.

### Structure

```
├── handler.py              # installs (docker build) and runs (docker run) the container
├── Dockerfile              # Python + ffmpeg
├── .env.example            # paths, file names and output size
└── app/
    ├── main.py             # flow: read → overlay → compress → add audio
    ├── environment/        # reads the variables and checks the input files
    └── utils/              # video (capture, writing, compression), image (chroma key) and audio
```

### Tools

Python 3, OpenCV, NumPy, ffmpeg, Docker and python-dotenv.

### How to use

[Docker](https://docs.docker.com/get-docker/) must be installed and running.

```bash
git clone https://github.com/tofolo17/video-embed.git
cd video-embed
pip install python-dotenv
mkdir input output
cp .env.example .env   # set INPUT_PATH and OUTPUT_PATH to those folders' absolute paths
```

Put a background video (`background.mp4`) and a caption video over a green screen (`caption.mp4`) in `input/`, or change
the names in `.env`. Then:

```bash
python handler.py --action install   # builds the docker-cv image
python handler.py --action run       # writes output/output.mp4
```

> The sample videos used during development belonged to third parties and were removed from the public version.
