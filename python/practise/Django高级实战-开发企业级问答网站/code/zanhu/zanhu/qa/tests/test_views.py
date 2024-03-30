#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

import json
from django.test import RequestFactory
from test_plus.test import CBVTestCase
from django.contrib.messages.storage.fallback import FallbackStorage

from zanhu.qa.models import Question, Answer
from zanhu.qa import views


class BaseQATest(CBVTestCase):

    def setUp(self):
        self.user = self.make_user("user01")
        self.other_user = self.make_user("user02")
        self.question_one = Question.objects.create(
            user=self.user,
            title="问题1",
            content="问题1的内容",
            tags="测试1, 测试2"
        )
        self.question_two = Question.objects.create(
            user=self.user,
            title="问题2",
            content="问题2的内容",
            has_answer=True,
            tags="测试1, 测试2"
        )
        self.answer = Answer.objects.create(
            user=self.user,
            question=self.question_two,
            content="问题2被采纳的回答",
            is_answer=True
        )

        self.request = RequestFactory().get('/fake-url')
        self.request.user = self.user


class TestQuestionListView(BaseQATest):
    """测试问题列表"""

    def test_context_data(self):
        response = self.get(views.QuestionListView, request=self.request)

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(response.context_data['questions'],
                                 map(repr, [self.question_one, self.question_two]), ordered=False)

        self.assertTrue(all(a == b for a, b in zip(response.context_data['questions'], Question.objects.all())))

        self.assertContext('popular_tags', Question.objects.get_counted_tags())
        self.assertContext('active', 'all')


class TestAnsweredQuestionListView(BaseQATest):
    """测试已回答问题列表"""

    def test_context_data(self):
        response = self.get(views.AnsweredQuestionListView, request=self.request)  # 方式一
        # response = views.AnsweredQuestionListView.as_view()(self.request)  # 方式二

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context_data['questions'], [repr(self.question_two)])
        self.assertContext('active', 'answered')  # 对应方式一
        # self.assertEqual(response.context_data['active'], 'answered')  # 对应方式二


class TestUnansweredQuestionListView(BaseQATest):
    """测试未回答问题列表"""

    def test_context_data(self):
        response = self.get(views.UnansweredQuestionListView, request=self.request)  # 方式一
        self.assertEqual(response.status_code, 200)  # 或者 self.response_200(response)
        self.assertQuerysetEqual(response.context_data['questions'], [repr(self.question_one)])
        self.assertContext('active', 'unanswered')


class TestCreateQuestionView(BaseQATest):
    """测试创建问题"""

    def test_get(self):
        response = self.get(views.CreateQuestionView, request=self.request)
        self.response_200(response)

        self.assertContains(response, '标题')
        self.assertContains(response, '编辑')
        self.assertContains(response, '预览')
        self.assertContains(response, '标签')
        self.assertIsInstance(response.context_data['view'], views.CreateQuestionView)

    def test_post(self):
        data = {'title': 'title', 'content': 'content', 'tags': 'tag1,tag2', 'status': 'O'}
        request = RequestFactory().post('/fake-url', data=data)
        request.user = self.user
        # RequestFactory测试含有django.contrib.messages的视图 https://code.djangoproject.com/ticket/17971
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = self.post(views.CreateQuestionView, request=request)
        assert response.status_code == 302
        assert response.url == '/qa/'


class TestQuestionDetailView(BaseQATest):
    """测试问题详情"""

    def get_context_data(self):
        response = self.get(views.QuestionDetailView, request=self.request,
                            pk=self.question_one.id)
        self.response_200(response)
        self.assertEqual(response.context_data['question'], self.question_one)


class TestCreateAnswerView(BaseQATest):
    """测试创建回答"""

    def test_get(self):
        response = self.get(views.CreateAnswerView, request=self.request,
                            question_id=self.question_one.id)
        self.response_200(response)
        self.assertContains(response, '编辑')
        self.assertContains(response, '预览')
        self.assertIsInstance(response.context_data['view'], views.CreateAnswerView)

    def get_post(self):
        request = RequestFactory().post('/fake-url', data={'content': 'content'})
        request.user = self.user
        # RequestFactory测试含有django.contrib.messages的视图 https://code.djangoproject.com/ticket/17971
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = self.post(views.CreateAnswerView, request=request)
        assert response.status_code == 302
        assert response.url == f'/qa/question-detail/{self.question_one.id}'


class TestQAVote(BaseQATest):

    def setUp(self):
        super(TestQAVote, self).setUp()
        self.request = RequestFactory().post('/fake-url', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        # QueryDict instance is immutable, request.POST是QueryDict对象，不可变
        self.request.POST = self.request.POST.copy()

        self.request.user = self.other_user

    def test_question_upvote(self):
        """赞同问题"""
        self.request.POST['question'] = self.question_one.id
        self.request.POST['value'] = 'U'

        response = views.question_vote(self.request)

        assert response.status_code == 200
        assert json.loads(response.content)['votes'] == 1

    def test_question_downvote(self):
        """反对问题"""
        self.request.POST['question'] = self.question_two.id
        self.request.POST['value'] = 'D'

        response = views.question_vote(self.request)

        assert response.status_code == 200
        assert json.loads(response.content)['votes'] == -1

    def test_answer_upvote(self):
        """赞同问答"""
        self.request.POST['answer'] = self.answer.uuid_id
        self.request.POST['value'] = 'U'

        response = views.answer_vote(self.request)

        assert response.status_code == 200
        assert json.loads(response.content)['votes'] == 1

    def test_answer_downvote(self):
        """反对回答"""
        self.request.POST['answer'] = self.answer.uuid_id
        self.request.POST['value'] = 'D'

        response = views.answer_vote(self.request)

        assert response.status_code == 200
        assert json.loads(response.content)['votes'] == -1

    def test_accept_answer(self):
        """接受回答"""

        self.request.user = self.user  # self.user是提问者
        self.request.POST['answer'] = self.answer.uuid_id

        response = views.accept_answer(self.request)

        assert response.status_code == 200
        assert json.loads(response.content)['status'] == 'true'


# from django.test import Client
# from django.urls import reverse
# from test_plus.test import TestCase
#
# from zanhu.qa.models import Question, Answer
#
#
# class QAViewsTest(TestCase):
#     def setUp(self):
#         self.user = self.make_user("user01")
#         self.other_user = self.make_user("user02")
#         self.client = Client()
#         self.other_client = Client()
#         self.client.login(username="user01", password="password")
#         self.other_client.login(username="user02", password="password")
#         self.question_one = Question.objects.create(
#             user=self.user,
#             title="问题1",
#             content="问题1的内容",
#             tags="测试1, 测试2"
#         )
#         self.question_two = Question.objects.create(
#             user=self.user,
#             title="问题2",
#             content="问题2的内容",
#             has_answer=True,
#             tags="测试1, 测试2"
#         )
#         self.answer = Answer.objects.create(
#             user=self.user,
#             question=self.question_two,
#             content="问题2被采纳的回答",
#             is_answer=True
#         )
#
#     def test_index_questions(self):
#         response = self.client.get(reverse("qa:all_q"))
#         assert response.status_code == 200
#         assert "问题1" in str(response.context["questions"])
#
#     def test_create_question_view(self):
#         current_count = Question.objects.count()
#         response = self.client.post(reverse("qa:ask_question"),
#                                     {"title": "问题标题",
#                                      "content": "问题内容",
#                                      "status": "O",
#                                      "tags": "测试标签"})
#         assert response.status_code == 302
#         new_question = Question.objects.first()
#         assert new_question.title == "问题标题"
#         assert Question.objects.count() == current_count + 1
#
#     def test_answered_questions(self):
#         response = self.client.get(reverse("qa:answered_q"))
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue("问题2" in str(response.context["questions"]))
#
#     def test_unanswered_questions(self):
#         response = self.client.get(reverse("qa:unanswered_q"))
#         assert response.status_code == 200
#         assert "问题1" in str(response.context["questions"])
#
#     def test_answer_question(self):
#         current_answer_count = Answer.objects.count()
#         response = self.client.post(
#             reverse("qa:propose_answer", kwargs={"question_id": self.question_one.id}), {"content": "问题1的回答"}
#         )
#         assert response.status_code == 302
#         assert Answer.objects.count() == current_answer_count + 1
#
#     def test_question_upvote(self):
#         """赞同问题"""
#         response_one = self.client.post(
#             reverse("qa:question_vote"),
#             {"value": "U", "question": self.question_one.id},
#             HTTP_X_REQUESTED_WITH="XMLHttpRequest"
#         )
#         assert response_one.status_code == 200
#
#     def test_question_downvote(self):
#         """反对问题"""
#         response_one = self.client.post(
#             reverse("qa:question_vote"),
#             {"value": "D", "question": self.question_one.id},
#             HTTP_X_REQUESTED_WITH="XMLHttpRequest")
#         assert response_one.status_code == 200
#
#     def test_answer_upvote(self):
#         """赞同回答"""
#         response_one = self.client.post(
#             reverse("qa:answer_vote"),
#             {"value": "U", "answer": self.answer.uuid_id},
#             HTTP_X_REQUESTED_WITH="XMLHttpRequest")
#         assert response_one.status_code == 200
#
#     def test_answer_downvote(self):
#         """反对回答"""
#         response_one = self.client.post(
#             reverse("qa:answer_vote"),
#             {"value": "D", "answer": self.answer.uuid_id},
#             HTTP_X_REQUESTED_WITH="XMLHttpRequest")
#         assert response_one.status_code == 200
#
#     def test_accept_answer(self):
#         """接受回答"""
#         response_one = self.client.post(
#             reverse("qa:accept_answer"),
#             {"answer": self.answer.uuid_id},
#             HTTP_X_REQUESTED_WITH="XMLHttpRequest")
#         assert response_one.status_code == 200

"""
使用TestClient和RequestFactory测试视图的区别
TestClient: 走Django框架的整个请求响应流程，经过WSGI handler、中间件、URL路由、
上下文处理器，返回response，更像是集成测试。特点：使用简单，测试一步到位。
测试用例运行慢，依赖于中间件、URL路由等其它部分

RequestFactory: 生成WSGIRequest供使用，与Django代码无关，单元测试的最佳实践，但使用难度高
"""
