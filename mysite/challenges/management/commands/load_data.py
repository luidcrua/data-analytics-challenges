import csv
from django.core.management.base import BaseCommand
from challenges.models import Idea
from datetime import datetime

class Command(BaseCommand):
    help = 'Uploads ideas from a TSV file'

    def handle(self, *args, **kwargs):
        file_path = 'mysite/fixtures/challenge_data.tsv'

        with open(file_path, newline='', encoding='utf-8') as tsvfile:
            reader = csv.DictReader(tsvfile, delimiter='\t')
            for row in reader:
                try:
                    idea_id = int(row["Idea ID"])
                    submitted_date_time = datetime.strptime(row["Submitted Date/Time"], "%Y-%m-%d %H:%M:%S")
                    idea_status = row["Idea Status"]
                    creator_id = row["Creator ID"]
                    creator_department = row["Creator Department"]
                    times_shared = int(row["Number of times the Idea has been shared"])
                    votes = int(row["Number of Votes"])
                    comments = int(row["Number of Comments"])
                    views = int(row["Number of Views"])
                    keywords = row["Keywords"]

                    # Create or update the Idea record
                    idea, created = Idea.objects.update_or_create(
                        idea_id=idea_id,
                        defaults={
                            'submitted_date_time': submitted_date_time,
                            'idea_status': idea_status,
                            'creator_id': creator_id,
                            'creator_department': creator_department,
                            'times_shared': times_shared,
                            'votes': votes,
                            'comments': comments,
                            'views': views,
                            'keywords': keywords,
                        }
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Created Idea {idea_id}"))
                    else:
                        self.stdout.write(self.style.SUCCESS(f"Updated Idea {idea_id}"))

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error processing row {row}: {e}"))
