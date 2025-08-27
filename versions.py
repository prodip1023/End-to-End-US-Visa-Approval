import importlib.metadata

packages = [
"pandas",
"ipykernel",
"numpy",
"matplotlib",
"plotly",
"seaborn",
"scipy",
"scikit-learn",
"imblearn",
"xgboost",
"catboost",
"pymongo",
"from_root",
"evidently",
"dill",
"PyYAML",
"neuro_mf",
"boto3",
"mypy-boto3-s3",
"botocore",
"fastapi",
"uvicorn",
"jinja2",
"python-multipart",

] 

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")
