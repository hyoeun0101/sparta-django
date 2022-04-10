# from datetime import datetime
#
# from django.test import TestCase
#
# from tabom.models import User
#
#
# class TestAutoNow(TestCase):
#
#     def test_auto_now_field_is_set_when_save(self) -> None:
#         user = User(name='haha')
#         user.save()
#         # updated_at과 created_at에 아무값을 안넣어줬는데 값이 들어가있다는 걸 확인.
#         self.assertIsNotNone(user.updated_at)
#         self.assertIsNotNone(user.created_at)
#
#     # raw sql로 실행해보기
#     def test_auto_now_field_not_set_when_raw_sql_update_executed(self) -> None:
#         # Given
#         from django.db import connection
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "INSERT INTO tabom_user(id,name,updated_at,created_at)"
#                 "VALUES (1,'hihi','1999-01-01 10:10:10', '1999-02-02 10:10:10')"
#             )
#             # When
#             from time import sleep
#             sleep(1)
#             cursor.execute(
#                 "UPDATE tabom_user SET name='changed' WHERE id=1"
#             )
#         # Then
#         user = User.objects.get(id=1)
#         self.assertEqual(user.updated_at, datetime(year=1999, month=1, day=1, hour=10, minute=10, second=10))
