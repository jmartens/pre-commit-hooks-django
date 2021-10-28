from os.path import basename, dirname
from subprocess import run, CalledProcessError
from typing import (
    Optional,
    Sequence,
)
from .utils import Runner
import glob


class CheckRunner(Runner):
    def check(self):
        for module in glob.glob("**/manage.py", recursive=True):
            try:
                run(f"python {module} makemigrations --check --dry-run", check=True)
            except CalledProcessError:
                print(f"{basename(dirname(module))} contains un-applied migrations")
                return 1
        return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    runner = CheckRunner(argv)
    return runner.check()


if __name__ == "__main__":
    exit(main())
