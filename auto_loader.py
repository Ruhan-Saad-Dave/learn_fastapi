import importlib
import pathlib
from fastapi import FastAPI, APIRouter

app = FastAPI()

def auto_load_routers():
    # 1. Get the path to the 'api' directory
    api_path = pathlib.Path(__file__).parent / "api"
    
    # 2. Iterate through version folders (v1, v2, etc.)
    for version_dir in api_path.iterdir():
        if version_dir.is_dir():
            version = version_dir.name  # e.g., "v1"
            
            # 3. Iterate through files inside each version folder
            for router_file in version_dir.glob("*.py"):
                if router_file.name == "__init__.py":
                    continue
                
                # Create the import path (e.g., api.v1.books)
                module_path = f"api.{version}.{router_file.stem}"
                module = importlib.import_module(module_path)
                
                # 4. Check if the file has a 'router' object
                if hasattr(module, "router"):
                    endpoint_prefix = f"/api/{version}/{router_file.stem}"
                    app.include_router(
                        module.router, 
                        prefix=endpoint_prefix,
                        tags=[f"{version.upper()} - {router_file.stem.capitalize()}"]
                    )

auto_load_routers()