from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from domain.blog.schemas import BlogCreate, BlogResponse, BlogUpdate
from core.dependencies import get_blog_service

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.post("", response_model=BlogResponse, status_code=201)
def create_blog(
    data: BlogCreate,
    service = Depends(get_blog_service)
):
    try:
        return service.create_blog(data.title, data.content, data.author_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=List[BlogResponse])
def get_all_blogs(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    service = Depends(get_blog_service)
):
    return service.get_all_blogs(skip, limit)

@router.get("/{blog_id}", response_model=BlogResponse)
def get_blog(
    blog_id: int,
    service = Depends(get_blog_service)
):
    try:
        return service.get_blog(blog_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{blog_id}", response_model=BlogResponse)
def update_blog(
    blog_id: int,
    data: BlogUpdate,
    service = Depends(get_blog_service)
):
    try:
        return service.update_blog(blog_id, data.title, data.content)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{blog_id}", status_code=204)
def delete_blog(
    blog_id: int,
    service = Depends(get_blog_service)
):
    try:
        service.delete_blog(blog_id)
        return None
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

