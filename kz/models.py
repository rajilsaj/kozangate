from django.db import models

# Event Model


class Events(models.Model):
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=1000)
    startDate = models.DateTimeField(auto_now=True, blank=True)
    endDate = models.DateTimeField(auto_now=False, blank=True)
    allDay = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return "{}-{}-{}-{}-{}".format(self.title, self.description, self.startDate, self.endDate, self.allDay)

# User Model


class Users(models.Model):
    name = models.CharField(max_length=180)
    email = models.CharField(max_length=180)
    phoneNumber = models.CharField(max_length=180)

    def __str__(self):
        return "{}-{}-{}".format(self.name, self.email, self.phoneNumber)

# Calendar Model


class Calendars(models.Model):
    name = models.CharField(max_length=180)
    description = models.CharField(max_length=1000)
    timezone = models.CharField(max_length=180)

    def __str__(self):
        return "{}-{}-{}".format(self.name, self.description, self.timezone)

# User Calendar


class UserCalendar(models.Model):
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True)
    calendar_id = models.ForeignKey(
        Calendars, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}-{}"
        format(self.user_id, self.calendar_id)

# Calendar Event


class CalendarEvents(models.Model):
    calendar_id = models.ForeignKey(
        Calendars, on_delete=models.CASCADE, blank=True, null=True)
    event_id = models.ForeignKey(
        Events, on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=180)

    def __str__(self):
        return "{}-{}-{}".format(self.calendar_id, self.event_id, self.role)

# Notification Model


class Notifications(models.Model):
    effective = models.DateTimeField(auto_now=True, blank=True)
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.effective, self.user_id)

# Event Notification


class EventsNotifications(models.Model):
    notification_id = models.ForeignKey(
        Notifications, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.notification)

# Notification Channel


class NotificationChannel(models.Model):
    method = models.CharField(max_length=180)
    value = models.CharField(max_length=180)
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}-{}-{}".format(self.method, self.value, self.user_id)
