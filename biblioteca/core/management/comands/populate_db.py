from django.core.management.base import BaseCommand
from core.models import Categoria, Autor, Livro

class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        categoria_misterio = Categoria.objects.create(nome="Mistério")
        categoria_ficcao = Categoria.objects.create(nome="Ficção")
        categoria_fantasia = Categoria.objects.create(nome="Fantasia")
        categoria_romance = Categoria.objects.create(nome="Romance")

        autor_agatha_christie = Autor.objects.create(nome="Agatha Christie")
        autor_arthur_c_clarke = Autor.objects.create(nome="Arthur C. Clarke")
        autor_arthur_conan_doyle = Autor.objects.create(nome="Arthur Conan Doyle")
        autor_cs_lewis = Autor.objects.create(nome="C.S. Lewis")
        autor_emily_bronte = Autor.objects.create(nome="Emily Brontë")
        autor_george_rr_martin = Autor.objects.create(nome="George R.R. Martin")
        autor_isaac_asimov = Autor.objects.create(nome="Isaac Asimov")
        autor_jrr_tolkien = Autor.objects.create(nome="J.R.R. Tolkien")

    
        Livro.objects.create(
            titulo="Assassinato no Expresso do Oriente",
            autor=autor_agatha_christie,
            categoria=categoria_misterio,
            publicado_em="1934-01-01",
        )
        Livro.objects.create(
            titulo="Orgulho e Preconceito",
            autor=autor_jane_austen,
            categoria=categoria_romance,
            publicado_em="1813-01-28",
        )

        Livro.objects.create(
            titulo="Neuromancer",
            autor=autor_william_gibson,
            categoria=categoria_ficcao,
            publicado_em="1984-07-01",
        )

        Livro.objects.create(
            titulo="O Nome do Vento",
            autor=autor_patrick_rothfuss,
            categoria=categoria_fantasia,
            publicado_em="2007-03-27",
        )

        Livro.objects.create(
            titulo="Duna",
            autor=autor_frank_herbert,
            categoria=categoria_ficcao,
            publicado_em="1965-08-01",
        )
