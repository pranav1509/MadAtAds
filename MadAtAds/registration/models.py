from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Domain(models.Model):
    """
    This Model saves the Domain for each company
    """
    DomainId = models.AutoField(primary_key=True) #primary key
    DomainName = models.CharField(max_length = 128)
    Description = models.CharField(max_length = 2048)
    
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.DomainName
    
    class Meta:
        db_table = "Domain"
    
class SubDomain(models.Model):
    """
    This Model saves sub domain of company , Each Domain can have multiplt sub-domain
    """
    
    SubDomainId = models.AutoField(primary_key=True) #primary Key
    Domain = models.ForeignKey(Domain , on_delete=models.CASCADE)
    SubDomainName = models.CharField(max_length = 256)
    Description = models.CharField(max_length = 2048)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.SubDomainName
    
    class Meta:
        db_table = "SubDomain"
        
        
class Company(models.Model):
    """
    This Model Saves COmpany details
    """
    
    CompanyId = models.AutoField(primary_key=True) #primary key
    CompanyName = models.CharField(max_length=1028)
    SubDomain =  models.ForeignKey(SubDomain , on_delete=models.CASCADE)
    Address = models.CharField(max_length=2048)
    PhoneNumber1 = models.CharField(max_length=15)
    PhoneNumber2 = models.CharField(max_length=15)
    WebsiteUrl = models.URLField(unique=True, null=False)
    FBUrl = models.URLField(null=True)
    LinkedinUrl = models.URLField(null=True)
    GooglePlusUrl = models.URLField(null=True)
    TwitterUrl = models.URLField(null=True)
    InstagramUrl = models.URLField(null=True)
    PinterestUrl = models.URLField(null=True)
    RedittUrl = models.URLField(null=True)
    
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.CompanyName
    
    class Meta:
        db_table = "Company"

    
class CompanyUser(models.Model):
    """
    This Models saves details related to company users
    """
    
    UserId = models.AutoField(primary_key=True) #primary key
    FirstName = models.CharField(max_length=128)
    LastName = models.CharField(max_length=128)
    Address = models.CharField(max_length=1024)
    Email = models.EmailField(unique=True,null=False)
    PhoneNumber1 = models.CharField(max_length=15,null=False)
    PhoneNumber2= models.CharField(max_length=15, null=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE) 
    VerifiedUser = models.BinaryField(default=False)
    
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.FirstName + "," + self.LastName
    
    class Meta:
        db_table = "CompanyUser"
    