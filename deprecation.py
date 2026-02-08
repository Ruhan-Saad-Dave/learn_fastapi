from fastapi import APIRouter, Response, Depends
from datetime import datetime

router = APIRouter()

# 1. Define a dependency that adds the warning headers
def deprecation_warning(response: Response):
    # Standard Header: Date when the version was deprecated
    response.headers["Deprecation"] = "Friday, 01 Aug 2025"
    # Standard Header: Date when the version will be SHUT DOWN (Sunset)
    response.headers["Sunset"] = "Sunday, 01 Mar 2026"
    # Friendly message for developers
    response.headers["X-API-Warning"] = "V1 is deprecated. Please migrate to V2 by March 2026."

# 2. Apply it to the entire router
# Every endpoint in this file will now send these headers
router = APIRouter(dependencies=[Depends(deprecation_warning)])

@router.get("/books")
def get_books():
    """
    WARNING: This endpoint is deprecated. 
    Use /api/v2/books instead.
    """
    return [{"id": 1, "title": "Legacy Book"}]