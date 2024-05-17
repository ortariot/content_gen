from sqlalchemy import ForeignKey, LargeBinary, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Subject(Base):
    __tablename__ = 'subject'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    products: Mapped[list['Product']] = relationship(
        back_populates="subject", cascade="all, delete-orphan"
        )
    image: Mapped['Image'] = relationship(back_populates='subject', lazy='selectin')
    
    def __repr__(self) -> str:
        return f'Subject(id={self.id}, name={self.name})'
    

class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(100))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subject.id"))
    subject: Mapped['Subject'] = relationship(back_populates='products')
    posts: Mapped[list['Post']] = relationship(
        back_populates="product", cascade="all, delete-orphan"
        )
    image: Mapped['Image'] = relationship(back_populates='product')

    def __repr__(self) -> str:
        return f'Product(id={self.id}, name={self.name})'


class Post(Base):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped['Product'] = relationship(back_populates='posts')
    image: Mapped['Image'] = relationship(back_populates='post')

    def __repr__(self) -> str:
        return f'Post(id={self.id}, name={self.name})'
    

class Image(Base):
    __tablename__ = 'image'

    id: Mapped[int] = mapped_column(primary_key=True)
    payload: Mapped[bytes] = mapped_column(LargeBinary)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subject.id"), nullable=True)
    subject: Mapped['Subject'] = relationship(back_populates='image')
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=True)
    product: Mapped['Product'] = relationship(back_populates='image')
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), nullable=True)
    post: Mapped['Post'] = relationship(back_populates='image')

    def __repr__(self) -> str:
        return f'Image(id={self.id})'
    

def get_model_from_tablename(tablename):
  for c in Base.registry._class_registry.data.values():
    if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
      return c