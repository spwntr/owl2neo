from owl2neo import make_gist
import sys

owl_file = sys.argv[1]
out_folder = sys.argv[2]
username = sys.argv[3]
github_repo = sys.argv[4]

# Example:
# python run_owl2neo.py NIF-GrossAnatomy.owl gist vsoch owl2neo

make_gist(owl_file, out_folder=out_folder, username=username, repo_name=github_repo)
