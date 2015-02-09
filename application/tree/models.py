from django.db import models
from django.template.defaultfilters import slugify
import datetime
from easy_thumbnails.fields import ThumbnailerImageField

class Picture(models.Model):
	image = ThumbnailerImageField(upload_to='work-img',blank=True,null=True)
	# tag_person = models.ManyToManyField("TagPerson",blank=True,null=True) # removed to make invers relation with foreign key
	location = models.ManyToManyField("City",blank=True,null=True)
	address = models.ForeignKey('House',blank=True,null=True)
	taken = models.DateField(blank=True,null=True)
	taken_confirmed = models.BooleanField(default=False)
	taken = models.DateField(blank=True,null=True)

	notes = models.TextField(blank=True,null=True)



class Event(models.Model):
	includes = models.ManyToManyField("Person",blank=True,null=True)
	picture = models.ManyToManyField(Picture,blank=True,null=True)
	locations = models.ManyToManyField("City",blank=True,null=True)
	address = models.ForeignKey('House',blank=True,null=True)
	date = models.DateField(blank=True,null=True)
	date_confirmed = models.BooleanField(default=False)
	notes = models.TextField(blank=True,null=True)

class TagPerson(models.Model):
	picture = models.ForeignKey(Picture,blank=True,null=True)
	person = models.ManyToManyField("Person",blank=True,null=True)
	location_x = models.FloatField(default=0,blank=True,null=True)
	location_y = models.FloatField(default=0,blank=True,null=True)
	notes = models.TextField(blank=True,null=True)


class City(models.Model):
	city = models.CharField(max_length=500,blank=True,null=True)
	prov_state = models.CharField(max_length=500,blank=True,null=True)
	country = models.CharField(max_length=500,blank=True,null=True)

	local_language_city = models.CharField(max_length=500,blank=True,null=True)
	local_language_prov = models.CharField(max_length=500,blank=True,null=True)
	local_language_country = models.CharField(max_length=500,blank=True,null=True)

	changed_name_to = models.ForeignKey('self',blank=True,null=True, related_name='changednameto')


	lon = models.FloatField(default=0,blank=True,null=True)
	lat = models.FloatField(default=0,blank=True,null=True)	

	slug = models.SlugField(blank=True)
	notes = models.TextField(blank=True,null=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.city)
		super(City, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.city		

class BirthLocation(models.Model):
	#we made this a seperate object because people might be born the same hospital!
	city = models.ForeignKey(City,blank=True,null=True)
	hospital = models.CharField(max_length=500,blank=True,null=True)
	notes = models.TextField(blank=True,null=True)
	
	def __unicode__(self):
		return self.city.city

class House(models.Model):
	street_number = models.CharField(max_length=500,blank=True,null=True)
	street_name = models.CharField(max_length=500,blank=True,null=True)
	neighbourhood = models.CharField(max_length=500,blank=True,null=True)
	apartment_number = models.CharField(max_length=500,blank=True,null=True)
	city = models.ForeignKey(City,blank=True,null=True)
	house_type = models.CharField(max_length=500,blank=True,null=True)
	notes = models.TextField(blank=True,null=True)

	lon = models.FloatField(default=0,blank=True,null=True)
	lat = models.FloatField(default=0,blank=True,null=True)	

	def __unicode__(self):
		return "%s %s %s" %(self.city, self.street_name, self.street_number)

class Livinglocation(models.Model):
	city = models.ForeignKey(City,blank=True,null=True)
	address = models.ForeignKey(House,blank=True,null=True)
	moved_to = models.DateField(blank=True,null=True)
	moved_to_confirmed = models.BooleanField(default=False)
	moved_from = models.DateField(blank=True,null=True)
	moved_from_confirmed = models.BooleanField(default=False)
	notes = models.TextField(blank=True,null=True)
	
	def relatedPerson(self):
		try:
			return Person.objects.get(living_in=self)
		except Exception, e:
			return "no Person owns this yet"

	def __unicode__(self):
		return "%s %s" %(self.relatedPerson() ,self.address)

class Relations(models.Model):
	relationship_types = (
		('m', 'Mother'),
		('f', 'Father'),
		('sm', 'StepMother'),
		('sf', 'StepFather'),
		('gm', 'God Mother'),
		('gf', 'God Farther'),
	)
	relation = models.CharField(max_length=2,choices=relationship_types,default='m')

	adopted = models.BooleanField(default=False)
	parent = models.ForeignKey("Person",blank=True,null=True)
	notes = models.TextField(blank=True,null=True)

	def __unicode__(self):
		return "%s - %s" %(self.relation,self.parent)

class Parnerships(models.Model):
	relationship_types = (
		('m', 'Married'),
		('d', 'Divorced'),
	)
	relation = models.CharField(max_length=2,choices=relationship_types,default='m')
	relation_a = models.ForeignKey("Person", related_name='person_a')
	relation_b = models.ForeignKey("Person", related_name='person_b')

	attended_by = models.ManyToManyField("Person",blank=True,null=True, related_name='attendedby')
	photos = models.ManyToManyField(Picture,blank=True,null=True)


	locations = models.ManyToManyField("City",blank=True,null=True)
	address = models.ForeignKey(House,blank=True,null=True)
	date = models.DateField(blank=True,null=True)
	date_confirmed = models.BooleanField(default=False)
	date_end = models.DateField(blank=True,null=True)
	date_end_confirmed = models.BooleanField(default=False)		

class FamilyName(models.Model):
	name = models.CharField(max_length=500,blank=True,null=True)
	name_native = models.ForeignKey('self',blank=True,null=True)

	slug = models.SlugField(blank=True)
	notes = models.TextField(blank=True,null=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.name)
		super(FamilyName, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class Language(models.Model):
	language = models.CharField(max_length=500,blank=True,null=True)
	slug = models.SlugField(blank=True)
	notes = models.TextField(blank=True,null=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.language)
		super(Language, self).save(*args, **kwargs)	

	def __unicode__(self):
		return self.language


class School(models.Model):
	school_name = models.CharField(max_length=500,blank=True,null=True)
	city = models.ForeignKey(City,blank=True,null=True)

	def __unicode__(self):
		return self.school_name

class Education(models.Model):
	startDate = models.DateField(blank=True,null=True)
	startDate_confirmed = models.BooleanField(default=False)
	endDate = models.DateField(blank=True,null=True)
	endDate_confirmed = models.BooleanField(default=False)
	school = models.ForeignKey(School,blank=True,null=True)
	education_level = models.CharField(max_length=500,blank=True,null=True)
	subject = models.CharField(max_length=500,blank=True,null=True)
	completed = models.BooleanField(default=False)
	notes = models.TextField(blank=True,null=True)
	person = models.ForeignKey('Person',blank=True,null=True, related_name='related_person_education')

	def __unicode__(self):
		return "%s %s %s" %(self.startDate,self.endDate,self.school.school_name)

class Company(models.Model):
	title =  models.CharField(max_length=500,blank=True,null=True)
	established = models.CharField(max_length=500,blank=True,null=True) 
	notes = models.TextField(blank=True,null=True)

class Work(models.Model):
	start = models.DateField(blank=True,null=True)
	start_confirmed = models.BooleanField(default=False)	
	end = models.DateField(blank=True,null=True)
	end_confirmed = models.BooleanField(default=False)
	job_title = models.CharField(max_length=500,blank=True,null=True)
	notes = models.TextField(blank=True,null=True)
	at = models.ForeignKey(Company,blank=True,null=True)
	person = models.ForeignKey('Person')

class Cemetary(models.Model):
	street_number = models.CharField(max_length=500,blank=True,null=True)
	street_name = models.CharField(max_length=500,blank=True,null=True)
	city = models.ForeignKey(City,blank=True,null=True)


class Person(models.Model):
	brith = models.DateField(blank=True,null=True)
	birth_location = models.ForeignKey(BirthLocation,blank=True,null=True,unique=True)
	brith_confirmed = models.BooleanField(default=False)		
	death = models.DateField(blank=True,null=True)
	death_city = models.ForeignKey(City,blank=True,null=True)
	burial_type = models.CharField(max_length=500,blank=True,null=True)
	cemetary = models.ManyToManyField(Cemetary,blank=True,null=True)
	plot = models.CharField(max_length=500,blank=True,null=True)
	plot_lon = models.FloatField(default=0,blank=True,null=True)
	plot_lat = models.FloatField(default=0,blank=True,null=True)

	death_confirmed = models.BooleanField(default=False)


	sex =  models.CharField(max_length=1,choices=(("m","male"),("f","female")),default='m')

	name_given = models.CharField(max_length=500,blank=True,null=True)
	name_given_birth = models.CharField(max_length=500,blank=True,null=True)
	name_nickname_1 = models.CharField(max_length=500,blank=True,null=True)
	name_nickname_2 = models.CharField(max_length=500,blank=True,null=True) 	
	name_middle = models.CharField(max_length=500,blank=True,null=True)
	name_family = models.ForeignKey(FamilyName,blank=True,null=True)
	name_birth_family = models.ForeignKey(FamilyName,blank=True,null=True, related_name='birthfamilyname')

	living_in =  models.ManyToManyField(Livinglocation,blank=True,null=True)

	parents = models.ManyToManyField(Relations,blank=True,null=True)

	# education = models.ManyToManyField(Education,blank=True,null=True)

	slug = models.SlugField(blank=True)
	notes = models.TextField(blank=True,null=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.name_given)
		super(Person, self).save(*args, **kwargs)		

	def __unicode__(self):
		return "%s %s" %(self.name_given,self.name_family)

