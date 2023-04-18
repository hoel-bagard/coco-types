from typing import TypeAlias, TypedDict, TypeVar

from .coco_object_detection import Annotation, Category, COCO_RLE, Image, Info, Licence, RLE, TPolygonSegmentation

_TSegmentation = TypeVar("_TSegmentation", TPolygonSegmentation, RLE, COCO_RLE)


class AnnotationKP(Annotation[_TSegmentation]):
    keypoints: list[int]
    num_keypoints: int


AnnotationKPAny: TypeAlias = AnnotationKP[TPolygonSegmentation] | AnnotationKP[RLE] | AnnotationKP[COCO_RLE]


class CategoryKP(Category):
    keypoints: list[str]
    skeleton: list[tuple[int, int]]


class DatasetKP(TypedDict):
    info: Info
    licences: list[Licence]
    images: list[Image]
    annotations: list[AnnotationKPAny]
    categories: list[CategoryKP]
