from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Subcategory, Product
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer


class CategoryView(APIView):

    def get(self, request):
        """
        GET API - this api returns all categories
        """
        try:
            categories = Category.objects.all()
        except Category.DoesNotExist:
            return Response({"message": "no categories found", "data":[]}, status=status.HTTP_404_NOT_FOUND)

        categories_data = CategorySerializer(categories, many=True)
        return Response({"message": "data found", "data": categories_data.data}, status=status.HTTP_200_OK)


class SubCategoryView(APIView):

    def get(self, request):
        """
        GET API - this api returns all categories
        """
        category_name = request.GET.get("category", "")
        if not category_name:
            return Response({"message": "category name is missing or blank in query parameters",
                             "data": []}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        try:
            category = Category.objects.get(name=category_name)
            sub_categories = Subcategory.objects.filter(category_id=category.id)
        except Category.DoesNotExist:
            return Response({"message": "no sub categories found", "data":[]}, status=status.HTTP_404_NOT_FOUND)

        sub_categories_data = SubCategorySerializer(sub_categories, many=True)
        return Response({"message": "data found", "data": sub_categories_data.data}, status=status.HTTP_200_OK)


class ProductView(APIView):

    def get(self, request):
        """
        GET API to get product list
        """
        category_name = request.GET.get("category", "")
        subcategory_name = request.GET.get("subcategory", "")
        if not category_name and not subcategory_name:
            return Response({"message": "category name or subcategory name is missing or blank in query parameters",
                             "data": []}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        elif category_name:
            try:
                category = Category.objects.get(name=category_name)
                products = Product.objects.filter(category_id=category.id)
            except Category.DoesNotExist:
                return Response({"message": "no products found", "data": []}, status=status.HTTP_404_NOT_FOUND)
            products_data = ProductSerializer(products, many=True)

        else:
            try:
                subcategory = Subcategory.objects.get(name=subcategory_name)
                products = Product.objects.filter(subcategory=subcategory.id)
            except Subcategory.DoesNotExist:
                return Response({"message": "no products found", "data": []}, status=status.HTTP_404_NOT_FOUND)
            products_data = SubCategorySerializer(products, many=True)

        return Response({"message": "data found", "data": products_data.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        POST API to add product
        """
        data = request.data
        if not data:
            return Response({"message": "no data in request payload"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            print("yes")
            serializer.save()
            return Response({"message": "product added successfully"}, status=status.HTTP_201_CREATED)