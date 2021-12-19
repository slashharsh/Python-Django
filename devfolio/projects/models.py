from django.db import models #ALL ABM
import uuid

# Create your models here.
class Project(models.Model): #Class name is basically table name
    title = models.CharField(max_length=200) # these are columns
    description = models.TextField(null=True,blank=True) # Null means DB mai emppty ho skta hai, blank means Form Post karna hai to empty se kar skte hai
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) #
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_code = models.CharField(max_length=2000,null=True,blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  #Due to this funcn on Admin page we get name of records at plcae of objects previously
        return self.title

