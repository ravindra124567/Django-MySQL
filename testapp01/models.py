from django.db import models

class DateTimeRecord(models.Model):
    recorded_date = models.DateField()
    recorded_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recorded_date} - {self.recorded_time}"

    class Meta:
        db_table = 'datetime_records'
        ordering = ['-created_at']