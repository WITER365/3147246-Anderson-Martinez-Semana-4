from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import database
import crud
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, get_db
from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List
from sqlalchemy.orm import Session
import models, schemas, crud
from database import get_db
from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List, Optional
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, Base, get_db
from fastapi import FastAPI
import models
from database import engine
from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List, Optional
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, Base, get_db

app = FastAPI()


database.Base.metadata.create_all(bind=database.engine)

@app.post("/productos", response_model=schemas.ProductoResponse)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(database.get_db)):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@app.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db: Session = Depends(database.get_db)):
    return db.query(models.Producto).all()

@app.get("/productos/{id}", response_model=schemas.ProductoResponse)
def obtener_producto(id: int, db: Session = Depends(database.get_db)):
    producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.put("/productos/{id}", response_model=schemas.ProductoResponse)
def actualizar_producto(id: int, datos: schemas.ProductoCreate, db: Session = Depends(database.get_db)):
    producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    producto.nombre = datos.nombre
    producto.precio = datos.precio
    db.commit()
    return producto

@app.delete("/productos/{id}")
def eliminar_producto(id: int, db: Session = Depends(database.get_db)):
    producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return {"mensaje": "Producto eliminado"}


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}



models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Productos Mejorada")

@app.post("/productos/", response_model=schemas.Producto)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    try:
        return crud.crear_producto(db=db, producto=producto)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/productos/")
def listar_productos(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    productos = crud.obtener_productos(db, skip=skip, limit=limit)
    total = crud.contar_productos(db)
    return {
        "productos": productos,
        "total": total,
        "pagina": skip // limit + 1,
        "por_pagina": limit
    }

@app.get("/productos/buscar/")
def buscar_productos(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    productos = crud.buscar_productos(db, busqueda=q)
    return {
        "busqueda": q,
        "productos": productos,
        "total": len(productos)
    }

@app.get("/productos/{producto_id}", response_model=schemas.Producto)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = crud.obtener_producto(db, producto_id=producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.patch("/productos/{producto_id}", response_model=schemas.Producto)
def actualizar_producto(producto_id: int, producto: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    db_producto = crud.actualizar_producto(db, producto_id=producto_id, producto=producto)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = crud.eliminar_producto(db, producto_id=producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": f"Producto {producto_id} eliminado correctamente"}

@app.get("/productos/stats/resumen")
def estadisticas_productos(db: Session = Depends(get_db)):
    total = crud.contar_productos(db)
    productos = crud.obtener_productos(db, limit=total)

    if not productos:
        return {"total": 0, "precio_promedio": 0, "precio_max": 0, "precio_min": 0}

    precios = [p.precio for p in productos]
    return {
        "total": total,
        "precio_promedio": sum(precios) / len(precios),
        "precio_max": max(precios),
        "precio_min": min(precios)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

models.Base.metadata.create_all(bind=engine)


@app.post("/categorias/", response_model=schemas.Categoria)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db=db, categoria=categoria)

@app.get("/categorias/", response_model=List[schemas.Categoria])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.obtener_categorias(db)

@app.get("/categorias/{categoria_id}", response_model=schemas.CategoriaConProductos)
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.obtener_categoria_con_productos(db, categoria_id=categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria



@app.get("/productos/", response_model=List[schemas.ProductoConCategoria])
def listar_productos_con_categoria(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return crud.obtener_productos_con_categoria(db, skip=skip, limit=limit)

@app.get("/categorias/{categoria_id}/productos/", response_model=List[schemas.ProductoBase])
def productos_por_categoria(categoria_id: int, db: Session = Depends(get_db)):
    productos = crud.obtener_productos_por_categoria(db, categoria_id=categoria_id)
    return productos


Base.metadata.create_all(bind=engine)

@app.post("/autores/", response_model=schemas.Autor)
def crear_autor(autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    db_autor = models.Autor(**autor.dict())
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor

@app.get("/autores/", response_model=List[schemas.Autor])
def listar_autores(db: Session = Depends(get_db)):
    return db.query(models.Autor).all()

@app.get("/autores/{autor_id}", response_model=schemas.AutorConLibros)
def obtener_autor_con_libros(autor_id: int, db: Session = Depends(get_db)):
    autor = db.query(models.Autor).filter(models.Autor.id == autor_id).first()
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return autor


@app.post("/libros/", response_model=schemas.LibroConAutor)
def crear_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    db_libro = models.Libro(**libro.dict())
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro

@app.get("/libros/", response_model=List[schemas.LibroConAutor])
def listar_libros_con_autor(db: Session = Depends(get_db)):
    return db.query(models.Libro).all()


@app.get("/libros/buscar/")
def buscar_libros(
    titulo: Optional[str] = Query(None, description="Buscar por título"),
    autor: Optional[str] = Query(None, description="Buscar por autor"),
    precio_min: Optional[float] = Query(None, description="Precio mínimo"),
    precio_max: Optional[float] = Query(None, description="Precio máximo"),
    db: Session = Depends(get_db)
):
    if titulo:
        libros = crud.buscar_libros_por_titulo(db, titulo)
    elif autor:
        libros = crud.buscar_libros_por_autor(db, autor)
    elif precio_min is not None and precio_max is not None:
        libros = crud.obtener_libros_por_precio(db, precio_min, precio_max)
    else:
        libros = db.query(models.Libro).all()

    return {
        "libros": libros,
        "total": len(libros)
    }


@app.get("/estadisticas/")
def estadisticas_libros(db: Session = Depends(get_db)):
    total_libros = db.query(models.Libro).count()
    total_autores = db.query(models.Autor).count()

    if total_libros > 0:
        precios = [libro.precio for libro in db.query(models.Libro).all()]
        precio_promedio = sum(precios) / len(precios)
        precio_max = max(precios)
        precio_min = min(precios)
    else:
        precio_promedio = precio_max = precio_min = 0

    return {
        "total_libros": total_libros,
        "total_autores": total_autores,
        "precio_promedio": precio_promedio,
        "precio_mas_alto": precio_max,
        "precio_mas_bajo": precio_min
    }
