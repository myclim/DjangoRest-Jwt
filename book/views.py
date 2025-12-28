from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from book.serializers import BookSerializers
from book.models import Book


class BookListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        product = get_object_or_404(Book, pk=pk)
        serializer = BookSerializers(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BookSerializers(data=request.data)
        user = request.user

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(
                {
                    "message": "Книга создана успешно",
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                    },
                    "book": serializer.data.get('title'),
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk, user=request.user)
        serializer = BookSerializers(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=pk, user=request.user)
        serializer = BookSerializers(book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookRemoveView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        user = request.user
        book = get_object_or_404(Book, pk=pk, user=user)
        book.delete()
        return Response(
            {"message": "Книга успешно удалена"}, status=status.HTTP_204_NO_CONTENT
        )
