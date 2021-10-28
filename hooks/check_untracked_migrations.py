from typing import (
    Optional,
    Sequence,
)
from .utils import (
    get_current_branch,
    get_untracked_files,
    Runner,
)
import re


class CheckRunner(Runner):
    def check(self):
        args = self.parser.parse_args(self.argv)
        current_branch = get_current_branch()
        if args.branches and current_branch not in args.branches:
            print(f"{current_branch} is not present in --branches arg")
            return 1
        untracked_migrations = [
            filename
            for filename in get_untracked_files()
            if re.match(r".*/migrations/.*\.py", filename)
        ]
        if not untracked_migrations:
            return 0
        else:
            print(f"Untracked migration file found: {*untracked_migrations,}")
            return 1


def main(argv: Optional[Sequence[str]] = None) -> int:
    runner = CheckRunner(argv=argv)
    runner.parser.add_argument(
        "--branches", nargs="*", help="Choose which branches to work on"
    )
    return runner.check()


if __name__ == "__main__":
    exit(main())
