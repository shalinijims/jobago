
from django.db import models
from django.contrib.auth.models import User
from .models import *


#   base table start here
class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'country'

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=255)
    country_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    class Meta:
        managed =True
        db_table = 'state'

class City(models.Model):
    city_id=models.AutoField(primary_key=True)
    city_name=models.CharField(max_length=255)
    state_id=models.IntegerField()
    is_active = models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'city'


class Institute(models.Model):
    institue_id = models.AutoField(primary_key=True)
    institue_name = models.CharField(max_length=255)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'institute'

class Degree(models.Model):
    degree_id = models.AutoField(primary_key=True)
    degree_name = models.CharField(max_length=255)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'degree'

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'course'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'role'

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'company'

class Industry(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.IntegerField(default=1) # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'industry'


class Functionalarea(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.IntegerField(default=1)# Field name made lowercase.
    industry_id=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'functionalArea'


class Language(models.Model):
    language_id=models.AutoField(primary_key=True,unique=True)
    language_name=models.CharField(max_length=255,null=False)
    is_active=models.IntegerField(default=1,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'language'


#base tables ends here

#job related stuff
class AllJobs(models.Model):
    all_jobs_id = models.AutoField(primary_key=True)
    job_code = models.CharField(max_length=25, blank=True, null=True)
    state = models.IntegerField()
    company_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'all_jobs'




class JobAdditionalField(models.Model):
    job_additional_field_id = models.AutoField(primary_key=True)
    job_detail_id = models.IntegerField()
    parameter = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'job_additional_field'


class JobCategory(models.Model):
    job_category_id = models.AutoField(primary_key=True)
    job_category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'job_category'


class JobDetail(models.Model):
    job_detail_id = models.AutoField(primary_key=True)
    job_code = models.IntegerField()
    apply_link = models.CharField(max_length=255, blank=True, null=True)
    job_url = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    job_experience = models.CharField(max_length=55)
    job_category = models.IntegerField()
    job_location = models.IntegerField()
    language = models.CharField(max_length=155)
    posted_date = models.IntegerField()
    expiry_date = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'job_detail'


class JobLocation(models.Model):
    job_location_id = models.AutoField(primary_key=True)
    city = models.IntegerField()
    state = models.IntegerField()
    country = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'job_location'


class Main(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    job_id = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main'


class ScrappedJobDetail(models.Model):
    job_detail_id = models.AutoField(primary_key=True)
    all_jobs_id = models.IntegerField()
    job_code = models.CharField(max_length=25)
    apply_link = models.CharField(max_length=255, blank=True, null=True)
    job_url = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    job_experience = models.CharField(max_length=55, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    job_category = models.CharField(max_length=255)
    language = models.CharField(max_length=155, blank=True, null=True)
    employment_type = models.CharField(max_length=155, blank=True, null=True)
    contract_type = models.CharField(max_length=155, blank=True, null=True)
    posted_date = models.CharField(max_length=29, blank=True, null=True)
    expiry_date = models.CharField(max_length=29, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'scrapped_job_detail'

class ScrappedAllJobs(models.Model):
    all_jobs_id = models.AutoField(primary_key=True)
    job_code = models.CharField(max_length=25, blank=True, null=True)
    company_id = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scrapped_all_jobs'   


class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField(blank=True, null=True,max_length=11)
    is_active = models.IntegerField()
    profile_complete=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'tblApplicant'


class Professional_detail(models.Model):
    professional_detail_id=models.AutoField(primary_key=True)
    applicant_id = models.IntegerField()
    company_id=models.ForeignKey(Company,models.DO_NOTHING)
    role_id=models.ForeignKey(Role,models.DO_NOTHING)
    salary=models.BigIntegerField(blank=True)
    start_date=models.DateField()
    end_date=models.DateField()
    industry_id=models.ForeignKey(Industry,models.DO_NOTHING)
    funcational_area_id=models.ForeignKey(Functionalarea,models.DO_NOTHING)
    total_experience=models.IntegerField(null=True)
    is_active = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



class Skill_detail(models.Model):
    skill_detail_id=models.AutoField(primary_key=True)
    applicant_id = models.IntegerField()
    skill_name=models.CharField(max_length=255)
    skill_exp=models.IntegerField()
    skill_rating=models.IntegerField()
    is_active = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Resume_detail(models.Model):
    resume_id=models.AutoField(primary_key=True)
    applicant_id = models.IntegerField()
    resume_path=models.TextField()
    cover_letter=models.TextField()
    is_active = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Additional_detail(models.Model):
    additional_id=models.AutoField(primary_key=True)
    applicant_id = models.IntegerField()
    parameter=models.TextField()
    value=models.TextField()
    is_active = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



class Education_details(models.Model):
    education_id=models.AutoField(primary_key=True)
    applicant_id = models.IntegerField()
    batch_start=models.DateField()
    batch_end=models.DateField()
    # institue_id=models.ForeignKey(Institute,models.DO_NOTHING,db_column=Institute.institue_id,null=True)
    # course_id=models.ForeignKey(Course,models.DO_NOTHING,db_column=Course.course_id,null=True)
    # degree_id=models.ForeignKey(Degree,models.DO_NOTHING,db_column=Degree.degree_id,null=True)
    institue_id=models.IntegerField(null=True)
    course_id=models.IntegerField(null=True)
    degree_id=models.IntegerField(null=True)
    is_active=models.IntegerField(default=1,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Personal_detail(models.Model):
    personal_id=models.AutoField(primary_key=True)
    applicant_id=models.IntegerField()
    first_name=models.CharField(max_length=255,null=True)
    last_name=models.CharField(max_length=255,null=True)
    gender=models.CharField(max_length=255,null=True)
    date_of_birth=models.DateTimeField(null=True)
    martial_status=models.IntegerField(null=True)
    # language_id=models.ForeignKey(Language_detail,models.DO_NOTHING,db_column=Language_detail.language_id)
    # city_id=models.ForeignKey(City,models.DO_NOTHING,db_column=City.city_id)
    language_id=models.IntegerField(null=True)
    country_id=models.IntegerField(null=True)
    state_id=models.IntegerField(null=True)
    profile_picture=models.FilePathField(null=True)
    is_active = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)




#by default stuff star
#by default stuff ends







#