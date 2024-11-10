from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=90, null=False)
    description = models.CharField(max_length=350)
    available_groups = models.JSONField()
    created_by_teacher = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'Courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f'{self.name = }. {self.available_groups = }'


class Task(models.Model):
    name = models.CharField(max_length=90, null=False)
    description = models.CharField(max_length=350, null=False)
    for_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    created_by_teacher = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False)
    deadline = models.DateField()
    class Meta:
        db_table = 'Tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.name = }. {self.for_course = }'

class GroupNumber(models.Model):
    name = models.CharField(max_length=90, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'GroupNumbers'
        verbose_name = 'Group Number'
        verbose_name_plural = 'Group Numbers'


class Group(models.Model):
    student = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False)
    group_number = models.ForeignKey(GroupNumber, on_delete=models.CASCADE, null=False)
    students_count = models.PositiveIntegerField(null=False)

    class Meta:
        db_table = 'Groups'
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return f'{self.group_number = }. {self.students_count = }'


class CourseFeedback(models.Model):
    student = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    review = models.CharField(max_length=350)
    rating = models.IntegerField(null=False, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'course_feedbacks'
        verbose_name = 'CourseFeedback'
        verbose_name_plural = 'CourseFeedbacks'

    def __str__(self):
        return f"{self.student = }. {self.course = }"


class TeacherFeedback(models.Model):
    student = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False,
                                related_name='student_feedbacks')
    teacher = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False,
                                related_name='teacher_feedbacks')
    review = models.CharField(max_length=150)
    rating = models.IntegerField(null=False, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teacher_feedbacks'
        verbose_name = 'TeacherFeedback'
        verbose_name_plural = 'TeacherFeedbacks'

    def __str__(self):
        return f"{self.student = }. {self.teacher = }"


class TaskSolution(models.Model):
    student = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False)
    solution_file_url = models.TextField(null=False)
    description = models.CharField(max_length=180)

    class Meta:
        db_table = 'task_solutions'
        verbose_name = 'TaskSolution'
        verbose_name_plural = 'TaskSolutions'

    def __str__(self):
        return f'{self.student = }. {self.task = }'


class SolutionReview(models.Model):
    task = models.ForeignKey(TaskSolution, on_delete=models.CASCADE, null=False)
    teacher = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False)
    rating = models.IntegerField(null=False, validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    review = models.CharField(max_length=350)

    class Meta:
        db_table = 'solution_reviews'
        verbose_name = 'SolutionReview'
        verbose_name_plural = 'SolutionReviews'

    def __str__(self):
        return f'{self.task = }. {self.teacher = }'


class StudentProgress(models.Model):
    student = models.ForeignKey('auth_app.User', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed_tasks = models.IntegerField(default=0)
    total_tasks = models.IntegerField(default=0)
    progress_percentage = models.FloatField()

    class Meta:
        db_table = 'student_progress'
        verbose_name = 'Student Progress'
        verbose_name_plural = 'Student Progress'


class CourseFile(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file_url = models.TextField()
    description = models.CharField(max_length=150)

    class Meta:
        db_table = 'course_files'
        verbose_name = 'Course File'
        verbose_name_plural = 'Course Files'

class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey('auth_app.User', on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'task_comments'
        verbose_name = 'Task Comment'
        verbose_name_plural = 'Task Comments'
