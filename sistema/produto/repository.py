from .models import *

class ProductRepository:

    @staticmethod
    def get_product_by_id(product_id):
        """Retorna os produtos por id"""
        return Product.objects.get(id=product_id)
    
    @staticmethod
    def get_last_product():
        """Retorna o ultimo produto"""
        return Product.objects.order_by('id').last
        
    @staticmethod
    def get_all_products():
        """Retorna todos os produtos"""
        return Product.objects.all()

    @staticmethod
    def create_product(name, description, type, collection, path):
        """Cria um produto"""
        return Product.objects.create(name=name, description=description, type=type, collection=collection, path=path) 

    @staticmethod
    def update_product(id_product, name, description, type, collection, path):
        """Atualizar um produto"""
        try:
            product = ProductRepository.get_product_by_id(id=id_product)
            product.name = name
            product.description = description
            product.type = type
            product.collection = collection
            product.path = path
            product.save()
            return True
        except Product.DoesNotExist:
            return False

    @staticmethod
    def delete_product(id_product):
        """Deletar um produto"""
        try:
            product = Product.objects.get(id=id_product)
            product.delete()
            return True
        except Product.DoesNotExist:
            return False
        
    @staticmethod
    def most_comment():
        return Product.most_commented()
        
    # @staticmethod
    # def search_product(query):
    #     try:
    #         # Primeiro tenta buscar por ID
    #         if query.isdigit():
    #             return Product.objects.filter(id=query)
    #     except ValueError:
    #         pass
        
    #     # Se não for um ID válido, busca por nome (convertendo para maiúsculas)
    #     query_upper = query.upper()
    #     return Product.objects.filter(name__icontains=query_upper)
    

class ProductCostRepository:
    
    @staticmethod
    def get_price_sell():
        return ProductCost.get_price_sell()

class CommentProductRepository:
    @staticmethod
    def create_comment_product(id_product, id_user, comment):
        """ um produto"""
        return CommentProduct.objects.create(id_product=id_product, id_user=id_user, comment=comment)
    
    @staticmethod
    def delete_comment_product(id_comment):
        try:
            comment = CommentProduct.objects.get(id=id_comment)
            comment.delete()
            return True
        except CommentProduct.DoesNotExist:
            return False
    
    @staticmethod
    def get_all_comments_product(id_product):
        return CommentProduct.objects.filter(id_product=id_product)
    
    
class CommentPageRepository:
    @staticmethod
    def create_comment_page(id_user, comment):
        return CommentPage.objects.create(id_user=id_user, comment=comment)

    @staticmethod
    def delete_comment_page(id_comment):
        try:
            comment = CommentPage.objects.get(id=id_comment)
            comment.delete()
            return True
        except CommentPage.DoesNotExist:
            return False
        
    @staticmethod
    def get_all_comments_page():
        return CommentPage.objects.all()