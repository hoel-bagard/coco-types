from typing import Optional, Generic, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel


class Info(BaseModel):
    year: int
    version: str
    description: str
    contributor: str
    url: str
    date_created: str


class Licence(BaseModel):
    id: int
    name: str
    url: str


class Image(BaseModel):
    id: int
    width: int
    height: int
    file_name: str


TPolygon_segmentation = list[list[float]]


class RLE(BaseModel):
    size: list[int]
    counts: list[int]


class EncodedRLE(BaseModel):
    size: list[int]
    counts: str | bytes


TSegmentation = TypeVar("TSegmentation", TPolygon_segmentation, RLE, EncodedRLE)


class Annotation(GenericModel, Generic[TSegmentation]):
    id: int
    image_id: int
    category_id: int
    # Segmentation can be a polygon, RLE or encoded RLE.
    # Exemple of polygon: "segmentation": [[510.66,423.01,511.72,420.03,...,510.45,423.01]]
    # Exemple of RLE: "segmentation": {"size": [40, 40], "counts": [245, 5, 35, 5, 35, 5, 35, 5, 35, 5, 1190]}
    # Exemple of encoded RLE: "segmentation": {"size": [480, 640], "counts": "aUh2b0X...BgRU4"}
    segmentation: TSegmentation
    area: float
    # The COCO bounding box format is [top left x position, top left y position, width, height].
    # bbox exemple:  "bbox": [473.07,395.93,38.65,28.67]
    bbox: list[float]
    iscrowd: int  # Either 1 or 0


class Category(BaseModel):
    id: int
    name: str
    supercategory: str


class Dataset(BaseModel):
    info: Optional[Info] = None
    licences: Optional[list[Licence]] = None
    images: list[Image]
    annotations: list[Annotation[TPolygon_segmentation] | Annotation[RLE] | Annotation[EncodedRLE]]
    categories: list[Category]