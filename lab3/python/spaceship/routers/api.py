from fastapi import APIRouter
import numpy

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get("/mult-matrices")
def mult_matrices():
    a = numpy.random.rand(10, 10)
    b = numpy.random.rand(10, 10)
    result = numpy.dot(a, b)

    return {
        "a": a.tolist(),
        "b": b.tolist(),
        "product": result.tolist(),
    }