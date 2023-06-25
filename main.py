import argparse
from src.getters import generate_image


parser = argparse.ArgumentParser(
        prog='ImageGenerator',
        description='Generate image by DALLE'
)
parser.add_argument('--cat_id', help='category id', type=int)
parser.add_argument('--prompt', help='prompt text', type=str)
parser.add_argument('--api_key', help='api key', type=str)
args = parser.parse_args()

result = generate_image(
        cat_id=args.cat_id,
        api_key=args.api_key,
        prompt=args.prompt
)

print(result)
