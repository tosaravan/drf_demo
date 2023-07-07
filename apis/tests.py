from rest_framework.test import APITestCase

from apis.models import Department, Employee


class BasicTest(APITestCase):
    def test_add_get_drinks(self):
        data = {
            "name": "tea",
            "description": "milk drink"}

        # post / add drink
        self.client.post("/drinks/", data)

        # get api to fetch the drinks
        response = self.client.get("/drinks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["name"], "tea")
        self.assertEqual(response.json()[0]["description"], "milk drink")

    def test_department_model(self):  # model department test
        Department.objects.create(dep_name="accounts", description="accounts department")
        Department.objects.create(dep_name="it", description="software development")

        queryset = Department.objects.all()
        print(queryset)
        for item in queryset:
            print(item.dep_name)

        self.assertEqual(queryset.count(), 2)

    def test_employee_model(self):  # model employee department test
        accounts = Department.objects.create(dep_name="accounts", description="accounts department")
        Department.objects.create(dep_name="it", description="software development")

        Employee.objects.create(fullname="John Major", sex="Male", department=accounts)

        queryset = Employee.objects.all()
        print(queryset)
        for item in queryset:
            print(item.fullname, item.department)

        self.assertEqual(queryset.count(), 1)