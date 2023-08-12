import argparse
from src.getters import generate_image
from src.dicts import Category, make_hierachy


parser = argparse.ArgumentParser(
        prog='ImageGenerator',
        description='Generate image by DALLE'
)
parser.add_argument('--cat_id', help='category id', type=int)
parser.add_argument('--prompt', help='prompt text', type=str)
parser.add_argument('--api_key', help='api key', type=str)
args = parser.parse_args()

make_hierachy()

result = generate_image(
        cat_id=args.cat_id,
        api_key=args.api_key,
        prompt=args.prompt,
        Category=Category,
)

print(result)
