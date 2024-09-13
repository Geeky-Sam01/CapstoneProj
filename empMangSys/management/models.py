from django.db import models
from django.contrib.auth.models import User

# made tables Department and UserProfile for easy access of user's and thier department
class Department(models.Model):
    DeptName = models.CharField(max_length=100)
    DeptID = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.DeptName} {self.DeptID}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department = models.OneToOneField(Department,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Name :{self.user.username} DeptId :{self.department.DeptID} DeptName :{self.department.DeptName}'
