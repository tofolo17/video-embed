import subprocess

from dotenv import load_dotenv

import os
import argparse

load_dotenv()


def main(args):
    if args.action == "install":
        install()
    elif args.action == "run":
        run()


# Runs the image, mounting the local input/output folders set in .env.
def run():
    try:
        command = [
            "docker",
            "run",
            '--rm',
            "-v",
            f"{os.environ.get('INPUT_PATH')}:{os.environ.get('DOCKER_INPUT')}",
            "-v",
            f"{os.environ.get('OUTPUT_PATH')}:{os.environ.get('DOCKER_OUTPUT')}",
            '-e',
            f'BACKGROUND_FILE={os.environ.get("BACKGROUND_FILE")}',
            '-e',
            f'CAPTION_FILE={os.environ.get("CAPTION_FILE")}',
            '-e',
            f'OUTPUT_FILE={os.environ.get("OUTPUT_FILE")}',
            '-e',
            f'SIZE={os.environ.get("SIZE")}',
            "docker-cv",
        ]

        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        raise Exception(
            "Erro ao executar o container. Você instalou o container?"
        )


def install():
    uninstall()

    try:
        command = [
            "docker",
            "build",
            "--tag",
            "docker-cv",
            ".",
        ]

        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        raise Exception(
            "Erro ao instalar o container. Você tem o Docker instalado? Está executando o comando no diretório correto?"
        )


def uninstall():
    try:
        command = [
            "docker",
            "rmi",
            "docker-cv",
        ]

        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        pass


if __name__ == "__main__":
    # Parse the command line arguments
    parser = argparse.ArgumentParser()

    # Action argument
    parser.add_argument(
        "-a",
        "--action",
        type=str,
        required=True,
        help="The action to be performed ('install' or 'run')",
    )

    # Parse the arguments
    args = parser.parse_args()

    main(args)
