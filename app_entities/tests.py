from django.test import TestCase, Client
from rest_framework.reverse import reverse

from app_accounts.models import User
from app_entities.models import Work


class WorkViewSetTestCase(TestCase):
    def setUp(self) -> None:
        self.work = Work.objects.create(title='test_work', price=0.0)

        self.empty_user = User.objects.create_user(username='empty.user', password='password')
        self.basic_user = User.objects.create_user(username='basic.user', password='password', is_basic_account=True)
        self.agent_user = User.objects.create_user(username='agent.user', password='password', is_agent_account=True)
        self.staff_user = User.objects.create_user(username='staff.user', password='password', is_staff_account=True)
        self.admin_user = User.objects.create_user(username='admin.user', password='password', is_admin_account=True)
        self.super_user = User.objects.create_superuser(username='super.user', password='password')

        self.guest_client = Client()
        self.empty_client = Client()
        self.basic_client = Client()
        self.agent_client = Client()
        self.staff_client = Client()
        self.admin_client = Client()
        self.super_client = Client()

        self.empty_client.force_login(user=self.empty_user)
        self.basic_client.force_login(user=self.basic_user)
        self.agent_client.force_login(user=self.agent_user)
        self.staff_client.force_login(user=self.staff_user)
        self.admin_client.force_login(user=self.admin_user)
        self.super_client.force_login(user=self.super_user)

    def tearDown(self) -> None:
        self.work.hard_delete()

        self.empty_user.delete()
        self.basic_user.delete()
        self.agent_user.delete()
        self.staff_user.delete()
        self.admin_user.delete()
        self.super_user.delete()

    def test_work_list(self):
        url = reverse('work-list')
        assert 200 == self.guest_client.get(url).status_code
        assert 200 == self.empty_client.get(url).status_code
        assert 200 == self.basic_client.get(url).status_code
        assert 200 == self.agent_client.get(url).status_code
        assert 200 == self.staff_client.get(url).status_code
        assert 200 == self.admin_client.get(url).status_code
        assert 200 == self.super_client.get(url).status_code

    def test_work_retrieve(self):
        url = reverse('work-detail', pk=self.work.id)
        assert 200 == self.guest_client.get(url).status_code
        assert 200 == self.empty_client.get(url).status_code
        assert 200 == self.basic_client.get(url).status_code
        assert 200 == self.agent_client.get(url).status_code
        assert 200 == self.staff_client.get(url).status_code
        assert 200 == self.admin_client.get(url).status_code
        assert 200 == self.super_client.get(url).status_code

    def test_work_create(self):
        pass

    def test_work_update(self):
        pass

    def test_work_partial_update(self):
        pass

    def test_work_delete(self):
        pass
