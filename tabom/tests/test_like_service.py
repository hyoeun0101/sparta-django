from django.db import IntegrityError
from django.test import TestCase

from tabom.models import Article, Like, User
from tabom.services.like_service import do_like, undo_like


class TestLikeService(TestCase):
    # Given
    # When
    # Then
    def test_a_user_can_like_an_article(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        like = do_like(user.id, article.id)

        # Then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # Expect
        do_like(user.id, article.id)
        # 에러가 일어나야 성공!!
        with self.assertRaises(IntegrityError):
            do_like(user.id, article.id)

    def test_it_should_raise_exception_when_like_an_user_does_not_exist(self) -> None:
        # Given
        invalid_user_id = 9988
        article = Article.objects.create(title="test_title")

        # Except
        with self.assertRaises(IntegrityError):
            do_like(invalid_user_id, article.id)

    def test_it_should_raise_exception_when_like_an_article_does_not_exist(self) -> None:
        # Given
        user = User.objects.create(name="test")
        invalid_article_id = 9988

        # Except
        with self.assertRaises(IntegrityError):
            do_like(user.id, invalid_article_id)

    def test_like_count_should_increase(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        do_like(user.id, article.id)

        # Then
        self.assertEqual(1, article.like_set.count())

    def test_a_user_can_undo_like(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")
        like = do_like(user.id, article.id)
        # When
        undo_like(user.id, article.id)

        # Then
        with self.assertRaises(Like.DoesNotExist):
            Like.objects.filter(id=like.id).get()
