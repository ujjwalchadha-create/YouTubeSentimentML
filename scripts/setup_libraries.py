import subprocess

libraries = [
    "numpy",
    "pandas",
    "nltk",
    "scikit-learn",
    "textblob",
    "matplotlib",
    "seaborn",
    "langdetect",
    "tensorflow",
    "keras",
    "flask",
]

for lib in libraries:
    try:
        __import__(lib)
        print(f"{lib} is installed.")
    except ImportError:
        print(f"{lib} is not installed. Installing now...")
        subprocess.check_call(["pip", "install", lib])
