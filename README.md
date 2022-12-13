# SUCECO - Banco de Dados de Classificação Sucessional de Árvores

### RUN
docker-compose up

### USEFUL COMMANDS
source activate suceco
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py collectstatic

Melhorias:
- S3 storage
- Internacionalizacao
- Cadastro e autenticacao de colaboradores usando external provider
- Add image field
- Recuperacao de senha
- Email aws
- Melhora estetica
- Testes
- Busca de espécies por trabalho
- Busca de espécies por autor
