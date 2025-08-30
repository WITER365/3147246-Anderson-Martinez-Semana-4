from sqlalchemy.orm import Session
from sqlalchemy import or_
import models, schemas
from sqlalchemy.orm import Session
import models


def crear_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def obtener_producto(db: Session, producto_id: int):
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

def obtener_productos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Producto).offset(skip).limit(limit).all()

def buscar_productos(db: Session, busqueda: str):
    return db.query(models.Producto).filter(
        or_(
            models.Producto.nombre.contains(busqueda),
            models.Producto.descripcion.contains(busqueda)
        )
    ).all()

def actualizar_producto(db: Session, producto_id: int, producto: schemas.ProductoUpdate):
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if db_producto:
        update_data = producto.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_producto, field, value)
        db.commit()
        db.refresh(db_producto)
    return db_producto

def eliminar_producto(db: Session, producto_id: int):
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto

def contar_productos(db: Session):
    return db.query(models.Producto).count()

from sqlalchemy.orm import joinedload


def crear_categoria(db: Session, categoria: schemas.CategoriaCreate):
    db_categoria = models.Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria


def obtener_categorias(db: Session):
    return db.query(models.Categoria).all()


def obtener_categoria(db: Session, categoria_id: int):
    return db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()


def obtener_categoria_con_productos(db: Session, categoria_id: int):
    return db.query(models.Categoria).options(
        joinedload(models.Categoria.productos)
    ).filter(models.Categoria.id == categoria_id).first()


def obtener_productos_con_categoria(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Producto).options(
        joinedload(models.Producto.categoria)
    ).offset(skip).limit(limit).all()


def obtener_productos_por_categoria(db: Session, categoria_id: int):
    return db.query(models.Producto).filter(
        models.Producto.categoria_id == categoria_id
    ).all()


def buscar_libros_por_titulo(db: Session, busqueda: str):
    return db.query(models.Libro).filter(models.Libro.titulo.contains(busqueda)).all()

def buscar_libros_por_autor(db: Session, nombre_autor: str):
    return db.query(models.Libro).join(models.Autor).filter(models.Autor.nombre.contains(nombre_autor)).all()

def obtener_libros_por_precio(db: Session, precio_min: float, precio_max: float):
    return db.query(models.Libro).filter(
        models.Libro.precio >= precio_min,
        models.Libro.precio <= precio_max
    ).all()
