"""
Copyright 2020 kivou.2000607@gmail.com

This file is part of yata.

    yata is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    yata is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with yata. If not, see <https://www.gnu.org/licenses/>.
"""

from django.core.management.base import BaseCommand

from faction.models import ArmoryReport
from faction.models import REPORTS_STATUS
from yata.handy import logdate


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('crontab', type=int)

    def handle(self, *args, **options):
        crontabId = options['crontab']
        print(f"[CRON {logdate()}] START armory report on crontab {crontabId}")
        report = ArmoryReport.objects.filter(computing=True).filter(crontab=crontabId).order_by('update').first()
        if report is not None:
            report.updateReport()
            # type = "error" if state < 0 else "exit"
            # status = REPORT_REVIVES_STATUS.get(state, f"code {state}")
            # print(f"[CRON {logdate()}] {report} {type} code {state}: {status}")
            # report.fillReport()

        print(f"[CRON {logdate()}] END")
