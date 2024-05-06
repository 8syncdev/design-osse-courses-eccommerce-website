import subprocess


# # -------------------------- Course -----------------------------
# subprocess.run('py manage.py loaddata ./gen/fixtures/course/category.json')
# subprocess.run('py manage.py loaddata ./gen/fixtures/course/extent.json')
# subprocess.run('py manage.py loaddata ./gen/fixtures/course/course.json')
# # -------------------------- Lesson -----------------------------
# subprocess.run('py manage.py loaddata ./gen/fixtures/lesson/python.json')

# # -------------------------- User -----------------------------
# subprocess.run('py manage.py loaddata ./gen/fixtures/user/role.json')
# subprocess.run('py manage.py loaddata ./gen/fixtures/user/user.json')
# subprocess.run('py manage.py loaddata ./gen/fixtures/user/userrole.json')


class TestDB:

    list_data = {
        #* Course <- Category | Extent | Course
        'course': {
            'category': 'py manage.py loaddata ./gen/fixtures/course/category.json',
            'extent': 'py manage.py loaddata ./gen/fixtures/course/extent.json',
            'course': 'py manage.py loaddata ./gen/fixtures/course/course.json',
        },
        #* Course <- Lesson
        'lesson': {
            'python': 'py manage.py loaddata ./gen/fixtures/course/lesson/python.json',
        },
        #* Course <- Lesson <- Detail Lesson
        'detail_lesson': {
            'python': 'py manage.py loaddata ./gen/fixtures/course/detail_lesson/python.json',
        },
        #* User -> Userrole <- Role
        'user': {
            'role': 'py manage.py loaddata ./gen/fixtures/user/role.json',
            'user': 'py manage.py loaddata ./gen/fixtures/user/user.json',
            'userrole': 'py manage.py loaddata ./gen/fixtures/user/userrole.json',
        }
    }

    list_run_cmd = [
        #* Role
        'py manage.py loaddata ./gen/fixtures/user/role.json', 
        #* User
        'py manage.py loaddata ./gen/fixtures/user/user.json',
        #* User -> Userrole <- Role
        'py manage.py loaddata ./gen/fixtures/user/userrole.json',
        #* Category
        'py manage.py loaddata ./gen/fixtures/course/category.json',
        #* Extent
        'py manage.py loaddata ./gen/fixtures/course/extent.json',
        #* Course - Category | Extent
        'py manage.py loaddata ./gen/fixtures/course/course.json',
        #* Lesson <- Course
        'py manage.py loaddata ./gen/fixtures/course/lesson/python.json',
        #* Course <- Lesson <- Detail Lesson
        'py manage.py loaddata ./gen/fixtures/course/detail_lesson/python.json',
    ]
    

    @staticmethod
    def create_all_data():
        for cmd in TestDB.list_run_cmd:
            subprocess.run(cmd)

    @staticmethod
    def create_one_data(path_cmd):
        subprocess.run(path_cmd)

if __name__ == '__main__':
    TestDB.create_all_data()