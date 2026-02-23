from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post, Like
from .serializers import PostSerializer
from notifications.models import Notification


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")


# ⭐ LikePostView يحقق جميع checks
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # check 1
        post = generics.get_object_or_404(Post, pk=pk)

        # check 2
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        # check 3
        if created:
            Notification.objects.create(
                recipient=post.user,
                actor=request.user,
                verb="liked your post",
                target=post
            )

        return
