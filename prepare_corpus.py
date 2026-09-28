"""Prepare isolated teaching inputs; never copy evaluations/results into a corpus."""
import argparse
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('run', choices=['starter', 'expanded', 'expanded2'])
args = parser.parse_args()
root = Path(__file__).resolve().parent
names = ['a. opposites.txt', 'b. negation.txt', 'c.music.txt', 'd.studyroutine.txt', 'e.plant.txt', 'f.bakery.txt']
names = names[:{'starter': 0, 'expanded': 2, 'expanded2': 6}[args.run]]
for name in names:
    if not (root / 'teaching_sources' / name).is_file():
        parser.error('Extract teaching-sources.zip first.')
dest = root / 'reproduction_corpus' / args.run
if dest.exists():
    parser.error(f'{dest} already exists; use the existing folder or move it before preparing again.')
dest.mkdir(parents=True)
for name in names:
    shutil.copy2(root / 'teaching_sources' / name, dest / name)
print(f'Prepared {len(names)} source files. Set CORPUS_FOLDER = {str(dest)!r}')
