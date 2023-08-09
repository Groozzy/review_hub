from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .permissions import IsAuthorOrReadOnly
from reviews.models import Reviews, Titles
from .serializers import CommentsSerializer, ReviewsSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    """Вьюсет для публикации."""
    serializer_class = ReviewsSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_title(self):
        title = get_object_or_404(Titles, pk=self.kwargs.get('title_id'))
        return title

    def get_queryset(self):
        new_queryset = self.get_title().reviews.select_related('author')
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())


class CommentsViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментариев."""
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_review(self):
        review = get_object_or_404(Reviews, pk=self.kwargs.get('review_id'))
        return review

    def get_queryset(self):
        new_queryset = self.get_review().comments.select_related('author')
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review())
