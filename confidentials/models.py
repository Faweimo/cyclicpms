from django.db import models

# Create your models here.

class BankDetail(models.Model):

    user_id                 = models.IntegerField(editable=False)
    full_name               = models.CharField(max_length=255)
    bank_name               = models.CharField(max_length=255)
    account_number          = models.CharField(max_length=255)
    bvn                     = models.CharField(max_length=255)
    sort_code               = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Bank Detail")
        verbose_name_plural = ("Bank Details")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("BankDetail_detail", kwargs={"pk": self.pk})


class PersonalInfo(models.Model):

    user_id                     = models.IntegerField(editable=False)    
    full_name                   = models.CharField(max_length=255)
    dob                         = models.DateField(blank=True,null=True)    
    dob_attach                  = models.FileField(upload_to='confidentials',blank=True,null=True)
    dob_verify                  = models.BooleanField(default=False)
    parmanent_home_address      = models.CharField(max_length=200)
    parmanent_address_verify    = models.BooleanField(default=False)
    contact_address             = models.CharField(max_length=255)
    contact_verify              = models.BooleanField(default=False)
    phone_number                = models.CharField(max_length=100)
    phone_number_2              = models.CharField(max_length=100)    
    pension_house               = models.CharField(max_length=200)
    pension_number              = models.CharField(max_length=200)
    PAYEE_ID                    = models.CharField(max_length=200)
    NHF_ID                      = models.CharField(max_length=200)
    employment_date             = models.DateTimeField()

    class Meta:
        verbose_name = ("Personal Info")
        verbose_name_plural = ("Personal Infos")

    def __str__(self):
        return self.name


class Education(models.Model):

    user_id                     = models.IntegerField(editable=False)    
    full_name                   = models.CharField(max_length=255)
    institution                 = models.CharField(max_length=200)
    date_from                   = models.DateTimeField()
    date_to                     = models.DateTimeField(blank=True,null=True)
    date_current                = models.BooleanField(default=False)
    degree                      = models.CharField(max_length=200)
    degree_authenticate         = models.BooleanField(default=False)
    degree_attach               = models.FileField(upload_to='confidentials')
    course                      = models.CharField(max_length=200)
    nysc_current                = models.BooleanField(default=False)
    nysc_ongoing                = models.BooleanField(default=False)
    nysc_authenticate           = models.BooleanField(default=False)
    nysc_attach                 = models.FileField(upload_to='confidentials')
    members_body                = models.CharField(max_length=200)
    membership_number           = models.CharField(max_length=100)
    membership_class            = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("Education")
        verbose_name_plural = ("Educations")

    def __str__(self):
        return self.institution

    def get_absolute_url(self):
        return reverse("Education_detail", kwargs={"pk": self.pk})
  