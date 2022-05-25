import argparse

def main(args: argparse.Namespace) -> None:
    """_summary_

    Args:
        args (argparse.Namespace): _description_
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument()

    _, args = parser.parse_known_args()

    main(args)