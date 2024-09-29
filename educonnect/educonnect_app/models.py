from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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

    class Meta:
        db_table = 'Tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.name = }. {self.for_course = }'


class Group(models.Model):
    student = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False)
    group_number = models.CharField(max_length=25, null=False)
    students_count = models.IntegerField()

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
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'course_feedbacks'
        verbose_name = 'CourseFeedback'
        verbose_name_plural = 'CourseFeedbacks'

    def __str__(self):
        return f"{self.student = }. {self.course = }"


class TeacherFeedback(models.Model):
    student = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False)
    teacher = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False)
    review = models.CharField(max_length=150)
    rating = models.IntegerField(null=False, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    created_at = models.DateTimeField()
    
    class Meta:
        db_table = 'teacher_feedbacks'
        verbose_name = 'TeacherFeedback'
        verbose_name_plural = 'TeacherFeedbacks'

    def __str__(self):
        return f"{self.student = }. {self.teacher = }"


class TaskSolution(models.Model):
    student = models.ForeignKey('auth_app.User', on_delete=models.CASCADE, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False)
    solution_file = models.FileField(null=False)
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