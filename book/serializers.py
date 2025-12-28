from rest_framework import serializers
from book.models import Book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', "title", "content", "created_at", "updated_at"]
        read_only_fields = ["user", "created_at", "updated_at"]

    def validate(self, attrs):
        content = attrs.get('content', '')
        
        if not content:
            raise serializers.ValidationError({"content": "Описание не может быть пустым."})
        
        if len(content) < 10:
            raise serializers.ValidationError({"content": "Описание слишком короткое. Минимум 10 символов."})

        return attrs